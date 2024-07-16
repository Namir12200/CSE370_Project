from django.urls import path
from .views import view_forum

urlpatterns = [
    path("<int:pk>/", view_forum, name='course_forum'),
    path('forum/', view_forum, name='course_forum')
]
