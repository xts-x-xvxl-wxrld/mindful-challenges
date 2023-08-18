from django import forms
from .models import CustomUser, Reflection, CustomChallenge
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation, get_user_model, authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UsernameField
from django.utils.text import capfirst


UserModel = get_user_model()


class CustomAuthenticationForm(forms.Form):

    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'placeholder': 'Username', 'class': 'django-form-input'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'placeholder': 'Password', 'class': 'django-form-input'}),
    )

    error_messages = {
        'invalid_login': _(
            "Please enter a correct %(username)s and password. Note that both "
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

        # Set the max length and label for the "username" field.
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)
        username_max_length = self.username_field.max_length or 254
        self.fields['username'].max_length = username_max_length
        self.fields['username'].widget.attrs['maxlength'] = username_max_length
        if self.fields['username'].label is None:
            self.fields['username'].label = capfirst(self.username_field.verbose_name)

        for key, field in self.fields.items():
            field.label = ""

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user(self):
        return self.user_cache

    def get_invalid_login_error(self):
        return ValidationError(
            self.error_messages['invalid_login'],
            code='invalid_login',
            params={'username': self.username_field.verbose_name},
        )


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'django-form-input', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'django-form-input', 'placeholder': 'Email'}),
        }

    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }

    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'placeholder': 'Password', 'class': 'django-form-input'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'placeholder': 'Repeat password', 'class': 'django-form-input'}),
        strip=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True

        for key, field in self.fields.items():
            field.label = ""

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


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

            'benefits': forms.TextInput(
                attrs={'class': 'django-form-text', 'placeholder': 'Enter: Benefits', 'label': ''}),

            'time_duration': forms.TextInput(
                attrs={'class': 'django-form-input', 'placeholder': 'Enter: Time Duration', 'label': ''}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""