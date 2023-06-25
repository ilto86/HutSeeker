# from django.contrib.auth import get_user_model
# from django.core.mail import send_mail
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
#
# UserModel = get_user_model()
#
#
# @receiver(signal=post_save, sender=UserModel)
# def send_email_on_successful_sign_up(instance, created, **kwargs):
#     if not created:
#         return None
#
#     username = instance.email.split('@')[0]
#
#     email_content = render_to_string('accounts/email-greeting.html', {'user': instance, "username": username})
#
#     send_mail(
#         subject='Welcome to our backend Page!',
#         message=strip_tags(email_content),
#         html_message=email_content,
#         from_email=None or 'info.huthub@mail.com',
#         recipient_list=(instance.email,),
#     )
