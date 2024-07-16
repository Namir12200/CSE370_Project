

from django.http import HttpResponse


# Create your views here.
# search/views.py
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from course.models import Course


class search(ListView):
    model = Course
    template_name = 'search/searchcourse.html'
    context_object_name = 'courses'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if not query:
            return Course.objects.none()
        object_list = Course.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
        return object_list


# def search(request):
#     return render(request, 'search/searchcourse.html')
