from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .views import index, approve, unapprove

# app_name = 'staff'

urlpatterns = [
    path('', index, name='staff-index'),
    path('approve/<int:member_id>', approve, name='approve'),
    path('unapprove/<int:member_id>', unapprove, name='unapprove'),
]
