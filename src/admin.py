from django.contrib import admin
from .models import Member, Subscription, Notice, Slide


class MemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'passport', 'member_type', 'phone', 'city', 'country']
    list_filter = ['member_type', 'country']


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['member', 'amount', 'month', 'year', 'payment_date']
    list_filter = ['month', 'year']


class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['is_active', 'created_at']


class SlideAdmin(admin.ModelAdmin):
    list_display = ['name', 'caption', 'photo']
    list_filter = ['is_active', 'created_at']


admin.site.register(Member, MemberAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Slide, SlideAdmin)




