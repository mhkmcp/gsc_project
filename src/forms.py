from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import Member


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['full_name', 'passport',  'date_of_birth', 'city', 'country', 'member_type']
        # exclude = ()


month_choice = (
    (1, 'জানুয়ারী'),
    (2, 'ফেব্রুয়ারী'),
    (3, 'মার্চ'),
    (4, 'এপ্রিল'),
    (5, 'মে'),
    (6, 'জুন'),
    (7, 'জুলাই'),
    (8, 'অগাস্ট'),
    (9, 'সেপ্টেম্বর'),
    (10, 'অক্টোবর'),
    (11, 'নভেম্বর'),
    (12, 'ডিসেম্বর')
)


class QueryForm(forms.Form):
    month = forms.ChoiceField(label='Select a Month', choices=month_choice, widget=forms.Select)
    year = forms.IntegerField(min_value=2000, max_value=3000)


class LoginForm(forms.ModelForm):
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'password']
