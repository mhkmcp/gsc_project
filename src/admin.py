from django.contrib.admin.sites import AlreadyRegistered
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.apps import apps

from .forms import GroupAdminForm

from .models import (
    DownloadPolicy,
    Member,
    Subscription,
    Notice,
    Slide,
    Election,
    Candidate,
    Commission,
)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    def add_to_election_commission(self, request, queryset):
        election_commission = get_object_or_404(Commission, name="Election Commission")
        queryset.update(election_commission_member=election_commission)

    def remove_from_election_commission(self, request, queryset):
        queryset.update(election_commission_member=None)

    def make_member_approved(self, request, queryset):
        queryset.update(is_approved=True)

    def make_member_unapproved(self, request, queryset):
        queryset.update(is_approved=False)

    make_member_approved.short_description = "Update Member to Approve"
    make_member_unapproved.short_description = "Update Member to Unapproved"
    add_to_election_commission.short_description = "Add Member to Election Commission"
    remove_from_election_commission.short_description = (
        "Remove Member from Election Commission"
    )

    list_display = [
        "full_name",
        "passport",
        "member_type",
        "phone",
        "zilla",
        "election_commission",
        "is_approved",
    ]
    list_filter = [
        "is_approved",
        "member_type",
    ]
    search_fields = ["passport", "phone", "user__email"]
    actions = [
        make_member_approved,
        make_member_unapproved,
        add_to_election_commission,
        remove_from_election_commission,
    ]

    def election_commission(self, x):
        if x.election_commission_member:
            return True
        else:
            return "-"


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
