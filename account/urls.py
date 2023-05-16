from django.urls import path
from .views import RegistrationView, ActivationView, LoginView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
]