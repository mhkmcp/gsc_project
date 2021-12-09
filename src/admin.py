from django.contrib.admin.sites import AlreadyRegistered
from django.contrib import admin
from django.apps import apps

from .models import (
    DownloadPolicy,
    Member,
    Subscription,
    Notice,
    Slide,
    Election,
    Candidate,
)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    def make_member_approved(self, request, queryset):
        queryset.update(is_approved=True)

    def make_member_unapproved(self, request, queryset):
        queryset.update(is_approved=False)

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
    list_filter = [
        "is_approved",
        "member_type",
    ]
    actions = [make_member_approved, make_member_unapproved]


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
        # css = {
        #     "all": ()
        # }
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
