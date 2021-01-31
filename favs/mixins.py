from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginOnlyView(LoginRequiredMixin):

    login_url = reverse_lazy("users:login")
