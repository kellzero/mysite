from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostViews.as_view(), name='home'),
    path('posts/',views.PostViews.as_view(), name='post-list'),
]