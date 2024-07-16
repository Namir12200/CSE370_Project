from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Course
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import Teacher, Student
from enrollment.models import Enrollment
from django.db.models import Q
from django.views.generic import ListView
# Create your views here.


class CourseListView(ListView):
    model = Course
    template_name = "course/course_list.html"
    context_object_name = "courses"

    def get_queryset(self):
        if self.request.user.is_authenticated:
            student_id = get_object_or_404(Student, user=self.request.user)
            enrolled_courses = Enrollment.objects.filter(student_id=student_id)
            teacher_id = get_object_or_404(Teacher, user=self.request.user)

            enrollment_list = []
            for enrolled_course in enrolled_courses:
                enrollment_list.append(enrolled_course.course_id.id)

            chosen_courses = Course.objects.all().exclude(
                id__in=enrollment_list).exclude(owner=teacher_id)

            return chosen_courses
        else:
            return Course.objects.all()


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = "course/course_detail.html"


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ["title", "fees", "description", "timeline"]
    success_url = "/"

    def form_valid(self, form):
        form.instance.owner = Teacher.objects.filter(
            user=self.request.user).first()
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    fields = ["title", "description", "timeline", "fees"]
    success_url = "/"

    def form_valid(self, form):
        form.instance.owner = Teacher.objects.filter(
            user=self.request.user).first()
        return super().form_valid(form)

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.owner.user:
            return True
        return False


class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    success_url = "/"

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.owner.user:
            return True
        return False


class CourseSearchView(ListView):
    model = Course
    template_name = 'course/course_search.html'
    context_object_name = 'courses'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Course.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return object_list


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {'course': course}
    return render(request, 'course_detail.html', context)
