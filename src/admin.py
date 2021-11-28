from django.contrib.admin.sites import AlreadyRegistered
from django.contrib import admin
from django.apps import apps

from .models import Member, Subscription, Notice, Slide


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
        "passport",
        "member_type",
        "phone",
        "zilla",
        "upazilla",
        "country",
    ]
    list_filter = ["member_type", "country"]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["member", "amount", "month", "year", "payment_date"]
    list_filter = ["month", "year"]


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
    list_filter = ["is_active", "created_at"]


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ["name", "caption", "photo"]
    list_filter = ["is_active", "created_at"]


""" 
    register all the models from this app
"""
app_models = apps.get_app_config("src").get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
