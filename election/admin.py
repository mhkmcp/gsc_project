from django.contrib.admin.sites import AlreadyRegistered
from django.contrib import admin
from django.apps import apps

from .models import Candidate, Election


class CandidateInLine(admin.TabularInline):
    model = Candidate
    extra = 1


@admin.register(Election)
class ElectionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "description"]}),
    ]
    inlines = [CandidateInLine]


""" 
    register all the models from this app
"""
app_models = apps.get_app_config("election").get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
