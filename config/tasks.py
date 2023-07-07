from django.core.mail import send_mail
from account.send_mail import send_confirmation_email
from .celery import app


@app.task
def send_confirmation_email_task(user, code):
    send_confirmation_email(user, code)

@app.task
def send_notification_task(user, order_id, price):
    send_mail(
        'Уыедомление о создании заказа!',
        f'''Вы создали заказ №{order_id}, ожидайте звонок!
        Полная стоимость вашего заказа: {price}. 
        Спасибо за то что выбрали нас!'''
        'from@exmple.com'
        [user],
        fail_silently=False
    )
