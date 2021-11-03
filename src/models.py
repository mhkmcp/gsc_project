from datetime import date, datetime

from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

choice = (
    ("g", "General Member"),
    ("l", "Lifetime Member"),
    ("f", "Founding Member"),
    ("a", "Admin"),
)


class Member(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, related_name="member"
    )
    full_name = models.CharField(max_length=255, blank=True, default="")
    father_name = models.CharField(max_length=255, blank=True, default="")
    mother_name = models.CharField(max_length=255, blank=True, default="")
    zilla = models.CharField(max_length=63, blank=True, default="")
    upazilla = models.CharField(max_length=63, blank=True, default="")
    country = models.CharField(max_length=127, blank=True, default="")
    image = models.ImageField(upload_to="member/images", blank=True, null=True)
    phone = models.CharField(max_length=32, blank=True, default="")
    whatsapp_number = models.CharField(max_length=32, blank=True, default="")
    fb_link = models.URLField(blank=True, default="")
    passport = models.CharField(max_length=63, blank=True, default="")
    date_of_birth = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, default="")
    image = models.ImageField(upload_to="img/members", blank=True, null=True)
    member_type = models.CharField(choices=choice, max_length=24, default="")
    is_agreed = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Members"

    def __str__(self):
        return self.full_name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


month_choice = (
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December"),
)


class Subscription(models.Model):
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="subscription"
    )
    amount = models.FloatField(default=0.0, blank=False, null=False)
    month = models.IntegerField(
        choices=month_choice, default=0, blank=False, null=False
    )
    year = models.CharField(
        max_length=10, default=datetime.now().year, blank=False, null=False
    )
    is_active = models.BooleanField(default=True)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.member.full_name + " Paid at " + str(self.payment_date)


class Slide(models.Model):
    caption = models.CharField(max_length=255, blank=True, null=True)
    photo = models.FileField(upload_to="slides")
    name = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Notice(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
