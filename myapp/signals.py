# myapp/signals.py
#from django.db.models.signals import post_save
#from django.dispatch import receiver
#from django.contrib.auth.models import User
#from .models import UserProfile

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
  #  if created:
 #       UserProfile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.userprofile.save()

from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our Platform!'
        message = f'Thank you for registering, {instance.username}! Keep following our page for updates.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        send_mail(subject, message, email_from, recipient_list)

