from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Member


@receiver(post_save, sender=Member)
def active_user(sender, instance, created, **kwargs):
    print("fired ===")
    if not created:
        print("notcreated ===")
        member_obj = instance
        if member_obj.is_approved:
            print("approved ===")
            user = member_obj.user
            print("user === 1 ==>", user.is_active)
            user.is_active = True
            print("user === 2 ==>", user.is_active)
            user.save()
            print("user === 3 ==>", user.is_active)
        else:
            print("unapproved ===")
            user = member_obj.user
            user.is_active = False
            user.save()
