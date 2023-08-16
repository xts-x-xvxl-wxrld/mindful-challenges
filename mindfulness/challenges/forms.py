from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser, Reflection, CustomChallenge


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class ReflectionForm(forms.ModelForm):
    class Meta:
        model = Reflection
        fields = ['reflection_text']
        widgets = {
            'reflection_text' : forms.Textarea(attrs={'rows': 1, 'cols': 28, }),
        }


class CustomChallengeForm(forms.ModelForm):
    class Meta:
        model = CustomChallenge
        fields = ['title', 'description', 'benefits', 'time_duration']
        widgets = {
            'title': forms.Textarea(attrs={'rows': 1, 'cols': 28}),
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 28}),
            'benefits': forms.Textarea(attrs={'rows': 3, 'cols': 28}),
            'time_duration': forms.Textarea(attrs={'rows': 1, 'cols': 28}),
        }