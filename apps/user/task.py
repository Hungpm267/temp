
from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task

@shared_task
def gui_thong_bao_co_user_moi(username, user_email):
    subject = f"Cảm ơn bạn đã tạo tài khoản tên là {username}"
    message = f"Chúc bạn vạn sự như ý"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)
    print(f"gửi email tới {user_email} thành công")
    return "Hoàn thành task gửi mail chào newbie"

