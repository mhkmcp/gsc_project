from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from src.models import Member, Subscription
from .decorators import allowed_users
from src.forms import *


import os
from twilio.rest import Client


def send_message(phone, name, username, password):
    # Download the helper library from https://www.twilio.com/docs/python/install
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = 'AC9d43fe23f7a0afc12122647e4ef1bfe1'
    auth_token = '0158e75ae8f15b87d29fe80e5a2794a8'
    client = Client(account_sid, auth_token)
    print('client: ', client)

    message = client.messages \
        .create(
            body=f"Hello {name}, Your BCPISKP Account has been activated. Please login with Username = {username} and "
                 f"Password = {password}",
            from_='+15867880604',
            to=phone
        )

    print('Message SID: ', message.sid)


@allowed_users(allowed_roles=['admin'])
def index(request):
    if request.method == 'POST':
        query_form = QueryForm(request.POST)
        if query_form.is_valid():
            month = query_form.cleaned_data.get('month')
            year = query_form.cleaned_data.get('year')

            subscriptions = Subscription.objects.filter(month=month, year=year)

            total_count = Member.objects.all().count()
            paid_count = subscriptions.count()
            not_paid_count = total_count - paid_count

            context = {
                'members': Member.objects.all(),
                'query_form': QueryForm(),
                'subscriptions': subscriptions,
                'count_not_paid': not_paid_count,
                'count_paid': paid_count
            }
            return render(request, 'staff/index.html', context)
    else:
        context = {
            'members': Member.objects.all(),
            'query_form': QueryForm()
        }
    return render(request, 'staff/index.html', context)


# @login_required(loggin_url='login')
@allowed_users(allowed_roles=['admin'])
def approve(request, member_id):
    member = Member.objects.get(id=member_id)
    message = None
    try:
        Member.objects.filter(id=member_id).update(is_approved=True)
        send_message(member.phone, member.full_name, member.user.username, member.date_of_birth)
        message = f'Message has been sent to {member.full_name}'
    except Exception as ex:
        Member.objects.filter(id=member_id).update(is_approved=False)
        print("Error Memeber Approve: ", ex)
        message = f'Message sending Failed {member.full_name}'

    context = {
        'members': Member.objects.all(),
        'query_form': QueryForm(),
        'message': message
    }
    return render(request, 'staff/index.html', context)


@allowed_users(allowed_roles=['admin'])
def unapprove(request, member_id):
    member = Member.objects.get(id=member_id)
    message = None
    try:
        Member.objects.filter(id=member_id).update(is_approved=False)
        # send_message(member.phone, member.full_name, member.user.username, member.date_of_birth)
        message = f'Message has been sent to {member.full_name}'
    except Exception as ex:
        # Member.objects.filter(id=member_id).update(is_approved=False)
        message = f'Message sending Failed {member.full_name}'

    context = {
        'members': Member.objects.all(),
        'query_form': QueryForm(),
        'message': message
    }
    return render(request, 'staff/index.html', context)
