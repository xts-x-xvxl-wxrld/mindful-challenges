from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser, Reflection, CustomChallenge


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'django-form-input'}),
            'email': forms.TextInput(attrs={'class': 'django-form-input'}),
        }


class ReflectionForm(forms.ModelForm):
    class Meta:
        model = Reflection
        fields = ['reflection_text']
        widgets = {
            'reflection_text': forms.TextInput(
                attrs={'class': 'django-form-text', 'placeholder': 'Enter: Reflection', 'label': ''}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class CustomChallengeForm(forms.ModelForm):
    class Meta:
        model = CustomChallenge
        fields = ['title', 'description', 'benefits', 'time_duration']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'django-form-input', 'placeholder': 'Enter: Title', 'label': ''}),

            'description': forms.TextInput(
                attrs={'class': 'django-form-text', 'placeholder': 'Enter: Description of the challenge', 'label': ''}),

            'benefits': forms.Textarea(
                attrs={'class': 'django-form-text', 'placeholder': 'Enter: Benefits', 'label': ''}),

            'time_duration': forms.TextInput(
                attrs={'class': 'django-form-input', 'placeholder': 'Enter: Time Duration', 'label': ''}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""