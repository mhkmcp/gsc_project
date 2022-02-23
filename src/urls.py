from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("logout", logout_user, name="logout"),
    path("intro", introduction, name="intro"),
    path("purpose", purpose, name="purpose"),
    path("president-speech", president_speech, name="president_speech"),
    path("courtesy-speech", courtesy_speech, name="courtesy_speech"),
    path("adviser", adviser, name="adviser"),
    path("management", management, name="management"),
    path("general", general, name="general"),
    path("election", election, name="election"),
    path("election/<int:pk>", election_details, name="election_details"),
    path("vote/<int:election_id>", vote, name="vote"),
    # member
    path("requirements", requirements, name="requirements"),
    path("how-to-be-member", how_to_be_member, name="how_to_be_member"),
    path("admission-form", admission_form, name="admission_form"),
    path("member-list", member_list, name="member_list"),
    path("member-detail/<int:pk>", member_detail, name="member_detail"),
    path("general-member", general_member, name="general_member"),
    path("lifetime-member", lifetime_member, name="lifetime_member"),
    path("honorary-member", founding_member, name="founding_member"),
    path("member-info", member_info, name="member_info"),
    path("member-share", member_share, name="member_share"),
    #  downloads
    path("policies", policies, name="policies"),
    #
    path("collection-info", collection_info, name="collection_info"),
    path("audit-report", audit_report, name="audit_report"),
    path("blood-group-dob", blood_group_dob, name="blood_group_dob"),
    path("financial", financial, name="financial"),
    path("other-way", other_way, name="other_way"),
    path("education-scholarship", education_scholarship, name="education_scholarship"),
    path("treatment", treatment, name="treatment"),
    path("training", training, name="training"),
    # Union
    path("union/history/", history, name="union_history"),
    path("union/employees/", employees, name="union_employees"),
    path("union/at-a-glance/", at_a_glance, name="union_at_a_glance"),
    path("union/info/", union_info, name="union_info"),
    path("union/freedom-fighter/", freedom_fighter, name="union_freedom_fighter"),
    path("union/villages/", village, name="union_village"),
    path("union/head-of-institutes/", principal_list, name="union_principal_list"),
    path(
        "union/president-of-institutes/",
        institute_president_list,
        name="union_institute_president",
    ),
    path(
        "union/hospitals-and-community-centers/",
        hospital_commiunity_center,
        name="union_hospital_community_center",
    ),
    path("union/institutes/", institute, name="union_institutes"),
    # union/institute
    path("union/institute/sonatia/", sonatia, name="institute_sonatia"),
    # contact
    path("contact/", contact, name="contact"),
    # profile
    path("profile/", profile, name="profile"),
    path("profile/edit/", profile_edit, name="profile_edit"),
]
