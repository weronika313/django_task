from django.views.generic.list import ListView
from .models import CustomUser


class UsersList(ListView):
    model = CustomUser
    template_name = 'users/user_list.html'
    context_object_name = 'users'