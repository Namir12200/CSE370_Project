from django.urls import path
from .views import QuestionListView, QuestionCreateView, QuestionDeleteView, QuestionDetailView, QuestionUpdateView

urlpatterns = [
    path("", QuestionListView.as_view(), name="question_list"),
    path("<int:qs_id>/", QuestionDetailView.as_view(), name="question-detail"),
    path("<int:qs_id>/delete", QuestionDeleteView.as_view(), name="question_delete"),
    path("<int:qs_id>/update", QuestionUpdateView.as_view(), name="question_update"),
    path("new/", QuestionCreateView.as_view(), name="question_create"),
]