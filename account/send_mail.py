from django.core.mail import send_mail

HOST = 'localhost:8000'


def send_confirmation_email(user, code):
    link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здрайствуйте, активируйте ваш аккаунт!',
        f'Что активировать ваш аккаунт нужно перейти по ссылке ниже:'
        f'\n{link}'
        f'\nСсылка работает один раз!',
        'damirbekovbakberdi32@gmail.com',
        [user],
        fail_silently=False,
    )
