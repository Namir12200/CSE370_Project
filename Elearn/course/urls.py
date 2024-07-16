from django.urls import path, include
from .views import CourseListView, CourseCreateView, CourseUpdateView, CourseDetailView, CourseDeleteView
from enrollment.views import CreateEnrollmentView
from coursePayment.views import StudentExamListView, StudentExamDetailView, st_exam_questions, st_exam, save_quiz_view, exam_result
from users.views import home as home_view
from . import views
urlpatterns = [
    path('', CourseListView.as_view(), name="course-home"),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name="course-detail"),
    path('course/new/', CourseCreateView.as_view(), name="course-create"),
    path('course/<int:pk>/update/',
         CourseUpdateView.as_view(), name="course-update"),
    path('course/<int:pk>/delete/',
         CourseDeleteView.as_view(), name="course-delete"),
    path('course/<int:course_pk>/', include('content.urls')),
    path('course/<int:pk>/enroll/',
         CreateEnrollmentView.as_view(), name="course-enroll"),
    path("course/<int:pk>/forum/", include('forum.urls')),
    path('course/<int:pk>/exam/', include("exam.urls")),
    path('course/<int:course_pk>/st_exam/',
         StudentExamListView.as_view(), name="st-exam"),
    path('course/<int:course_pk>/st_exam/<int:pk>/',
         StudentExamDetailView.as_view(), name="st-exam-detail"),
    path('course/<int:course_pk>/st_exam/<int:pk>/st_question_list/questions/',
         st_exam_questions, name="st-exam-questions"),
    path('course/<int:course_pk>/st_exam/<int:pk>/st_question_list/',
         st_exam, name="st-exam"),
    path('course/<int:course_pk>/st_exam/<int:pk>/st_question_list/save/',
         save_quiz_view, name="st-exam-save"),
    path('course/<int:course_pk>/st_exam/<int:pk>/results/',
         exam_result, name="exam-result"),
]
