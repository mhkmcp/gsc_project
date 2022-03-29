from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.forms.models import inlineformset_factory

from .models import Candidate, Contact, Election, Member, PasswordResetRequest


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False, label="ইমেইল (Optional)")
    password1 = forms.CharField(
        label="পাসওয়ার্ড",
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label="পাসওয়ার্ড নিশ্চিত",
        strip=False,
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]
        labels = {"email": "ইমেইল"}


class PasswordResetForm(forms.ModelForm):
    new_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = PasswordResetRequest
        exclude = ["done"]


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(required=False, label="ইমেইল (Optional)")

    class Meta:
        model = User
        fields = ["email"]
        labels = {"email": "ইমেইল"}


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "phone", "subject", "message"]
        widgets = {
            "message": forms.Textarea(
                attrs={
                    "rows": "5",
                },
            ),
        }


MEMBER_TYPES = (
    ("g", "সাধারণ সদস্য"),
    ("l", "আজীবন সদস্য"),
    ("f", "প্রতিষ্ঠাতা সদস্য"),
)


class MemberForm(forms.ModelForm):
    member_type = forms.ChoiceField(label="সদস্যের ধরন", choices=MEMBER_TYPES)

    class Meta:
        model = Member
        exclude = [
            "user",
            "is_approved",
        ]
        labels = {
            "full_name": "নাম",
            "father_name": "বাবার নাম",
            "mother_name": "মায়ের নাম",
            "passport": "পাসপোর্ট",
            "date_of_birth": "জন্ম তারিখ",
            "phone": "মোবাইল/ফোন নং",
            "member_type": "সদস্যের ধরন",
            "village": "গ্রাম",
            "post_office": "পোস্ট অফিস",
            "upazilla": "উপজেলা",
            "zilla": "জেলা",
            "country": "দেশ (বর্তমান অবস্থানরত)",
            "image": "ছবি",
            "is_agreed": "অঙ্গীকারনামা",
        }

        widgets = {
            "date_of_birth": forms.DateInput(
                attrs={
                    "type": "date",
                },
            ),
        }


month_choice = (
    (1, "জানুয়ারী"),
    (2, "ফেব্রুয়ারী"),
    (3, "মার্চ"),
    (4, "এপ্রিল"),
    (5, "মে"),
    (6, "জুন"),
    (7, "জুলাই"),
    (8, "অগাস্ট"),
    (9, "সেপ্টেম্বর"),
    (10, "অক্টোবর"),
    (11, "নভেম্বর"),
    (12, "ডিসেম্বর"),
)


class QueryForm(forms.Form):
    month = forms.ChoiceField(
        label="Select a Month", choices=month_choice, widget=forms.Select
    )
    year = forms.IntegerField(min_value=2000, max_value=3000)


class LoginForm(forms.Form):
    passport = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "পাসপোর্ট"}), label=""
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "পাসওয়ার্ড"}), label=""
    )


class ElectionForm(forms.ModelForm):
    class Meta:
        model = Election
        fields = ["name"]


class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"


CandidateFormFormSet = inlineformset_factory(
    Election, Candidate, form=CandidateForm, fields=["user"], extra=1, can_delete=True
)
