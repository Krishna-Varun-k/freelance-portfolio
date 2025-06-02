from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('search/', views.search_freelancers, name='search'),
    path('create-service/', views.create_service, name='create_service'),
    path('create-project/', views.create_project, name='create_project'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
