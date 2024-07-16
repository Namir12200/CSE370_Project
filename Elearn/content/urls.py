from django.urls import path
from .views import ContentListView, ContentDetailView, ContentCreateView, ContentUpdateView, ContentDeleteView


urlpatterns = [
    path('content/', ContentListView.as_view(), name="content-list"),
    path('content/detail/<int:pk>/', ContentDetailView.as_view(), name="content-detail"),
    path('content/update/<int:pk>/', ContentUpdateView.as_view(), name="content-update"),
    path('content/new/', ContentCreateView.as_view(), name="content-create"),
    path('content/delete/<int:pk>/', ContentDeleteView.as_view(), name="content-delete"),
]