from django.urls import path, include
from .views import EnrollCourseView, UnenrollCourse, EnrollCourseDetailView
from coursePayment.views import PaymentCreateView

urlpatterns = [
    path("", EnrollCourseView.as_view(), name="enrolled-courses"),
    path("<int:pk>/", EnrollCourseDetailView.as_view(), name="enrolled-course-detail"),
    path("<int:pk>/delete/", UnenrollCourse.as_view(), name="unenroll-course"),
    path("<int:pk>/purchase/", PaymentCreateView.as_view(), name="purchase-course"),
]