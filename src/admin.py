from django.contrib.admin.sites import AlreadyRegistered
from django.contrib import admin
from django.apps import apps
from django.contrib.auth.hashers import make_password

from .models import (
    DownloadPolicy,
    Member,
    Subscription,
    Notice,
    Slide,
    Election,
    Candidate,
    PasswordResetRequest,
)


@admin.register(PasswordResetRequest)
class PasswordResetRequestAdmin(admin.ModelAdmin):
    def set_requested_password(self, request, queryset):
        queryset.update(done=True)
        for req in queryset:
            member = Member.objects.get(passport=req.passport)
            user = member.user
            print(req.new_password)
            user.password = make_password(req.new_password)
            user.save()

    set_requested_password.short_description = "Reset with requested password."

    exclude = ["new_password"]
    list_display = ["phone", "passport", "done"]
    list_filter = ["done"]
    search_fields = ["phone", "passport"]
    actions = [set_requested_password]


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    def make_member_approved(self, request, queryset):
        queryset.update(is_approved=True)
        for member in queryset:
            user = member.user
            user.is_active = True
            user.save()

    def make_member_unapproved(self, request, queryset):
        queryset.update(is_approved=False)
        for member in queryset:
            user = member.user
            user.is_active = False
            user.save()

    make_member_approved.short_description = "Update Member to Approve"
    make_member_unapproved.short_description = "Update Member to Unapproved"

    list_display = [
        "full_name",
        "passport",
        "member_type",
        "phone",
        "zilla",
        "is_approved",
    ]
    list_filter = ["is_approved", "member_type"]
    search_fields = ["passport", "phone", "user__email"]
    actions = [
        make_member_approved,
        make_member_unapproved,
    ]


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
    list_display = ["title"]
    list_filter = ["is_active", "created_at"]


class CandidateInLine(admin.TabularInline):
    model = Candidate
    extra = 1


@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "description"]}),
    ]
    inlines = [CandidateInLine]


@admin.register(DownloadPolicy)
class DownloadPolicyAdmin(admin.ModelAdmin):
    class Media:
        js = ("js/admin/policies.js",)


""" 
    register all the models from this app
"""
app_models = apps.get_app_config("src").get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
