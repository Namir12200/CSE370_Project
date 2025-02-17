"""
URL configuration for Elearn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from search import views as search_views
from forum import views as forum_views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('search/', search_views.search, name='searchcourse'),
    # path('courses/', course_view.Course, name='courses'),
    path('profile/', users_views.profile, name='profile'),
    path('contact/', users_views.contact, name='contact'),
    path('search/', search_views.search.as_view(), name='searchcourse'),
    path('about/', users_views.about, name='about'),
    path('home/', users_views.home, name='home'),
    # path('forum/', include('forum.urls')),
    path('forum/', forum_views.view_forum, name='course_forum'),
    path('admin/', admin.site.urls),
    path('', include("course.urls")),
    path('register/', users_views.register, name="register"),
    path('login/', LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('enrolled/', include('enrollment.urls')),
    path('purchased/', include('coursePayment.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
