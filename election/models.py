from django.db import models
from django.contrib.auth.models import User


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


class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return str(self.user)
