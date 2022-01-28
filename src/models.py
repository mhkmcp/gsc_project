from datetime import date, datetime

from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


choice = (
    ("g", "General Member"),
    ("l", "Lifetime Member"),
    ("f", "Founding Member"),
    ("a", "Admin"),
)


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="member")
    full_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    zilla = models.CharField(max_length=63)
    upazilla = models.CharField(max_length=63)
    country = models.CharField(max_length=127)
    image = models.ImageField(upload_to="member/images")
    phone = models.CharField(max_length=32)
    passport = models.CharField(max_length=63)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to="img/members")
    member_type = models.CharField(choices=choice, max_length=24)
    fb_link = models.URLField(blank=True, default="")
    whatsapp_number = models.CharField(max_length=32, blank=True, default="")

    is_agreed = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = ""
        verbose_name_plural = "Members"

    def __str__(self):
        return self.full_name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


month_choice = (
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December"),
)


class Subscription(models.Model):
    member = models.ForeignKey(
        Member, on_delete=models.CASCADE, related_name="subscription"
    )
    amount = models.FloatField(default=0.0, blank=False, null=False)
    month = models.IntegerField(
        choices=month_choice, default=0, blank=False, null=False
    )
    year = models.CharField(
        max_length=10, default=datetime.now().year, blank=False, null=False
    )
    is_active = models.BooleanField(default=True)
    payment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.member.full_name + " Paid at " + str(self.payment_date)


class Slide(models.Model):
    photo = models.FileField(upload_to="slides")
    title = models.CharField(max_length=255, blank=True, null=True)
    text = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Notice(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AdvisoryMember(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    image = models.ImageField(upload_to="advisory_members/")
    facebook = models.URLField(default="", blank=True, null=True)
    linkedin = models.URLField(default="", blank=True, null=True)

    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EducationScholarship(models.Model):
    name = models.CharField(max_length=255)
    number = models.PositiveIntegerField(blank=True, null=True, default=0)
    monthly_amount = models.PositiveIntegerField(blank=True, null=True, default=0)
    yearly_amount = models.PositiveIntegerField(blank=True, null=True, default=0)
    description = models.TextField(default="")

    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MedicalAssistance(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    venue = models.CharField(max_length=255, blank=True, null=True, default="")
    budget = models.PositiveIntegerField(blank=True, null=True, default=0)
    description = models.TextField(blank=True, null=True, default="")

    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class TrainingAssistance(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(blank=True, null=True, default=0)
    classes = models.CharField(max_length=255, blank=True, null=True, default="")
    total_trainee = models.PositiveIntegerField(blank=True, null=True, default=0)
    description = models.TextField(default="")

    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Election(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="", blank=True, null=True)

    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def user_can_vote(self, user):
        """
        Return False if user already voted
        """
        user_votes = user.vote_set.all()
        qs = user_votes.filter(election=self)
        if qs.exists():
            return False
        return True


class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.election)


class DownloadPolicy(models.Model):
    content = models.TextField(blank=True, null=True, default="")

    class Meta:
        verbose_name_plural = "Download Policies"

    def __str__(self):
        return self.content[:50]
