from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostViews.as_view(), name='home'),
    path('posts/',views.PostViews.as_view(), name='post-list'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]