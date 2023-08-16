from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):

    def __str__(self):
        return self.username


class Challenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    benefits = models.TextField()
    time_duration = models.CharField(max_length=50)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    completed_by = models.ManyToManyField(get_user_model(), through='Reflection')

    def __str__(self):
        return self.title


class Reflection(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    reflection_text = models.CharField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reflection by {self.user.username} on {self.challenge.title}"


class CustomChallenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    benefits = models.TextField()
    time_duration = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title