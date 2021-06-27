from django.urls import path

from apps.users import views

urlpatterns = [
    path("users", views.UsersList.as_view(), name="users"),
    path("users/<int:pk>/", views.UserDetail.as_view(), name="user-detail"),
    path("user/create", views.UserCreate.as_view(), name="user-create"),
    path("user/<int:pk>/", views.UserUpdate.as_view(), name="user-update"),
    path("user/<int:pk>/delete/", views.UserDelete.as_view(), name="user-delete"),
]
