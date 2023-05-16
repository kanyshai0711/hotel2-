from django.core.mail import send_mail
from main import settings

def send_activation_code(email, activation_code):
    message = f'Вы зарегистрировались на нашем сайте. Пройдите активацию аккаунта\n Код активации: {activation_code}'
    send_mail(
        'Активация аккаунта', 
        message,
        'test@gmail.com',
        [email]
    )
