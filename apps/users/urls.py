from django.urls import path

from apps.users import views

urlpatterns = [
    path('users', views.UsersList.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]