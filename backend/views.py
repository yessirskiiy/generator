import random

from django.http import JsonResponse
from django.views.generic import ListView, FormView

from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy

from backend.models import RandomNumber


def random_number_api(request):
    random_number = random.randint(1, 100)
    data = {
        'random_number': random_number
    }
    return JsonResponse(data)


class Generator(ListView, LoginRequiredMixin):
    template_name = 'backend/generator.html'
    context_object_name = 'number'

    def get_queryset(self):
        return None


class UserLogin(LoginView):
    next_page = 'generator_page'
    fields = '__all__'
    template_name = 'backend/login.html'


class UserRegistration(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('generator_page')
    template_name = 'backend/registration.html'

    def form_valid(self, form):
        user = form.save()
        if form.is_valid():
            login(self.request, user)
        return super(UserRegistration, self).form_valid(form)
