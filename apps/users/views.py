from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView

from .forms import UserForm
from .models import CustomUser


class UsersList(ListView):
    model = CustomUser
    template_name = "users/user_list.html"
    context_object_name = "users"


class UserDetail(DetailView):
    model = CustomUser
    template_name = "users/user_detail.html"
    context_object_name = "user"


class UserUpdate(UpdateView):
    model = CustomUser
    template_name = "users/user_update.html"
    form_class = UserForm
    paginate_by = 10
    success_url = reverse_lazy("users")


class UserDelete(DeleteView):
    model = CustomUser
    template_name = "users/user_confirm_delete.html"
    success_url = reverse_lazy("users")


class UserCreate(CreateView):
    model = CustomUser
    template_name = "users/user_create.html"
    form_class = UserForm
    success_url = reverse_lazy("users")
