from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import MemberForm, CustomUserCreationForm, LoginForm
from django.contrib import messages
from .models import *


def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Success")
            return redirect("home")

        else:
            messages.info(request, "Login Failed!")
            return redirect("home")

    context = {
        "login_form": LoginForm,
        "notices": Notice.objects.filter(is_active=True).order_by("-id"),
        "slides": Slide.objects.all(),
    }
    return render(request, "pages/home.html", context)


def logout_user(request):
    logout(request)
    return redirect("home")


# about us


def introduction(request):
    context = {"notices": Notice.objects.filter(is_active=True).order_by("-id")}
    return render(request, "pages/about-us/introduction.html", context)


def purpose(request):
    context = {"notices": Notice.objects.filter(is_active=True).order_by("-id")}
    return render(request, "pages/about-us/purpose.html", context)


def president_speech(request):
    context = {"notices": Notice.objects.filter(is_active=True).order_by("-id")}
    return render(request, "pages/about-us/president_speech.html", context)


def courtesy_speech(request):
    return render(request, "pages/about-us/courtesy_speech.html")


# committee


def adviser(request):
    advisory_members = AdvisoryMember.objects.filter(is_active=True)
    context = {"advisory_members": advisory_members}
    return render(request, "pages/commiittee/adviser.html", context)


def management(request):
    advisory_members = AdvisoryMember.objects.filter(is_active=True)
    context = {"advisory_members": advisory_members}
    return render(request, "pages/commiittee/management.html", context)


def general(request):
    return render(request, "pages/commiittee/general.html")


def election(request):
    return render(request, "pages/commiittee/election.html")


# member


def requirements(request):
    return render(request, "pages/member/requirements.html")


def how_to_be_member(request):
    return render(request, "pages/member/how_to_be_member.html")


def admission_form(request):
    if request.method == "POST":
        member_form = MemberForm(request.POST, request.FILES or None)  # member form
        user_creation_form = CustomUserCreationForm(request.POST or None)  # signup form

        if user_creation_form.is_valid() and member_form.is_valid():
            # create new Member
            member = member_form.save(commit=False)

            # create new User
            user = user_creation_form.save(commit=False)
            passport = member_form.cleaned_data.get("passport")
            username = passport[:6]
            user.username = username
            user.is_active = False
            user.save()

            # save member
            member.user = user
            member.save()

            messages.success(request, "Member was registered successfully.")
            return redirect("admission_form")
        else:
            print(user_creation_form.errors.as_data)
            print(member_form.errors.as_data)
    else:
        member_form = MemberForm()
        user_creation_form = CustomUserCreationForm()

    context = {"member_form": member_form, "user_form": user_creation_form}

    return render(request, "pages/member/admission_form.html", context=context)


def member_list(request):
    members = Member.objects.filter(
        member_type__in=["f", "l", "g"], is_approved=True
    ).order_by("-id")

    context = {
        "founding_members": members.filter(member_type="f"),
        "lifetime_members": members.filter(member_type="l"),
        "general_members": members.filter(member_type="g"),
    }
    return render(request, "pages/member/member_list.html", context)


def member_detail(request, pk):
    member = get_object_or_404(Member, pk=pk, is_approved=True)
    context = {"member": member}
    return render(request, "pages/member/member_detail.html", context)


def general_member(request):
    members = Member.objects.filter(member_type="g", is_approved=True).order_by("-id")
    context = {"members": members}
    return render(request, "pages/member/general_member.html", context)


def lifetime_member(request):
    members = Member.objects.filter(member_type="l", is_approved=True).order_by("-id")
    context = {"members": members}
    return render(request, "pages/member/lifetime_member.html", context)


def founding_member(request):
    members = Member.objects.filter(member_type="f", is_approved=True).order_by("-id")
    context = {"members": members}
    return render(request, "pages/member/founding_member.html", context)


def member_info(request):
    return render(request, "pages/member/member_info.html")


def member_share(request):
    return render(request, "pages/member/member_share.html")


def collection_info(request):
    return render(request, "pages/member/yearly_collection_info.html")


def audit_report(request):
    return render(request, "pages/member/audit_report.html")


def blood_group_dob(request):
    return render(request, "pages/member/dob_bg.html")


# deposit


def financial(request):
    return render(request, "pages/deposit/financial_institute.html")


def other_way(request):
    return render(request, "pages/deposit/other_way.html")


# development


def scholarship(request):
    return render(request, "pages/development/scholarship.html")


def training(request):
    return render(request, "pages/development/training.html")


def treatment(request):
    return render(request, "pages/development/treatment.html")


# Union


def history(request):
    return render(request, "pages/union/history.html")


def employees(request):
    return render(request, "pages/union/employees.html")


def at_a_glance(request):
    return render(request, "pages/union/at-a-glance.html")


def union_info(request):
    return render(request, "pages/union/info.html")


def freedom_fighter(request):
    return render(request, "pages/union/freedom-fighters.html")


def village(request):
    return render(request, "pages/union/villages.html")


def principal_list(request):
    return render(request, "pages/union/principal.html")


def institute_president_list(request):
    return render(request, "pages/union/institute-president.html")


def hospital_commiunity_center(request):
    return render(request, "pages/union/hospital-and-commiunity-center.html")


def institute(request):
    return render(request, "pages/union/institutes.html")


# Union institutes


def sonatia(request):
    return render(request, "pages/union/institute/sonatia.html")


# contact
def contact(request):
    return render(request, "pages/contact.html")
