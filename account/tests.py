from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from .views import RegistrationView, LoginView, ChangePasswordView, ForgotPasswordCompleteView, ForgotPasswordView
from .models import User

class UserTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            email = 'test@gmail.com',
            password = '12345',
            is_active = True
        )
        
    # def test_register(self):
    #     data = {
    #         'email': 'abdirashitovakanyshai99@gmail.com',
    #         'password': '123456',
    #         'password_confirm': '123456',
    #         'name': 'test',
    #         'last_name': 'TEST'
    #     }
    #     request = self.factory.post('register/', data, format='json')
    #     view = RegistrationView.as_view()
    #     response = view(request)
    #     print(response)
    #     assert response.status_code == 200

    def test_login(self):
        data = {
            'email':'abdirashitovakanyshai99@gmail.com',
            'password': '123456'
        }
        request = self.factory.post('login/', data, format='json')
        view = LoginView.as_view()
        response = view(request)
        print(response)
        assert response.status_code == 200
        assert 'token' in response.data



