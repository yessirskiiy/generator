from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import UserLogin, Generator, UserRegistration, random_number_api

urlpatterns = [
    path('', Generator.as_view(), name='generator_page'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', LogoutView.as_view(next_page='generator_page'), name='logout'),
    path('api/random/', random_number_api, name='random_number_api'),

    # path('login/', UserLogin.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # path('registration/', UserRegistration.as_view(), name='registration'),

]
