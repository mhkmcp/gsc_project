from django.contrib.auth.decorators import login_required
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from django.db.models import Count

from .forms import (
    CandidateFormFormSet,
    ContactForm,
    ElectionForm,
    MemberForm,
    CustomUserCreationForm,
    LoginForm,
)
from django.contrib import messages
from .models import *


def index(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST or None)
        if login_form.is_valid():
            member = get_object_or_404(
                Member, passport=login_form.cleaned_data.get("passport")
            )
            if member:
                if member.is_approved:
                    user = authenticate(
                        request,
                        username=member.user.username,
                        password=login_form.cleaned_data.get("password"),
                    )
                    if user is not None:
                        login(request, user)
                        messages.success(request, "Login Success")
                    else:
                        messages.info(request, "Login Failed!")
                else:
                    messages.warning(request, "Member is not approved.")
            else:
                messages.error(request, "Member not found")

            return redirect("home")
        else:
            messages.error(request, "Invalid form data")
            return redirect("home")

    context = {
        "login_form": LoginForm(),
        "slides": Slide.objects.all(),
    }
    return render(request, "pages/home.html", context)


def logout_user(request):
    logout(request)
    return redirect("home")


# about us


def introduction(request):
    context = {}
    return render(request, "pages/about-us/introduction.html", context)


def purpose(request):
    context = {}
    return render(request, "pages/about-us/purpose.html", context)


def president_speech(request):
    context = {}
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
    elections = Election.objects.filter(is_active=True).order_by("-created_at")
    election_member = False
    member_of_commision = request.user.groups.filter(
        name="Election Commission"
    ).exists()
    if member_of_commision:
        election_member = True
    form = ElectionForm()
    formset = CandidateFormFormSet()

    if request.method == "POST":
        # print(request.POST)
        form = ElectionForm(request.POST or None)
        formset = CandidateFormFormSet(request.POST or None)

        if form.is_valid() and formset.is_valid():
            election_instance = form.save(commit=False)
            # election_instance.save()

            formset = formset.save(commit=False)

            # import pdb

            # pdb.set_trace()

            for candidate in formset:
                candidate.election = election_instance
                print("candidate ==>", candidate)
                # candidate.save()

            messages.success(request, "Election saved successfully.")

    context = {
        "elections": elections,
        "election_member": election_member,
        "formset": formset,
        "form": form,
    }
    return render(request, "pages/commiittee/election.html", context)


@login_required(login_url="election")
def election_details(request, pk):
    election = get_object_or_404(Election, pk=pk)
    candidates = (
        election.candidate_set.all()
        .annotate(count_vote=Count("vote"))
        .order_by("-count_vote")
    )

    user_cant_vote = False
    if not election.user_can_vote(request.user):
        user_cant_vote = True

    context = {
        "election": election,
        "candidates": candidates,
        "user_cant_vote": user_cant_vote,
    }

    return render(request, "pages/commiittee/election_details.html", context)


@login_required
def vote(request, election_id):
    election = get_object_or_404(Election, pk=election_id)
    selected_candidate = election.candidate_set.get(pk=request.POST.get("candidate"))

    if not election.user_can_vote(request.user):
        messages.error(request, "You already voted this election")
    else:
        if selected_candidate:
            new_vote = Vote(
                voter=request.user, election=election, candidate=selected_candidate
            )
            new_vote.save()
            messages.success(request, "Voted successfully.")
        else:
            messages.error(request, "You didn't vote.")
            return redirect(reverse("election_details", args=(election.pk,)))

    return HttpResponseRedirect(reverse("election_details", args=(election.pk,)))


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
            username = passport
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


def education_scholarship(request):
    scholarships = EducationScholarship.objects.filter(is_active=True)
    context = {"scholarships": scholarships}
    return render(request, "pages/development/education_scholarship.html", context)


def training(request):
    trainings = TrainingAssistance.objects.filter(is_active=True)
    context = {"trainings": trainings}
    return render(request, "pages/development/training.html", context)


def treatment(request):
    treatments = MedicalAssistance.objects.filter(is_active=True)
    context = {"treatments": treatments}
    return render(request, "pages/development/treatment.html", context)


# Download


def policies(request):
    content = DownloadPolicy.objects.all().first()
    context = {"content": content}
    return render(request, "pages/downloads/policies.html", context)


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
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Thank you for your interest. We will get back to you soon"
            )
            return redirect("contact")
        else:
            messages.error(request, "Invalid form data.")
            form = ContactForm()

    context = {"form": form}
    return render(request, "pages/contact.html", context)
