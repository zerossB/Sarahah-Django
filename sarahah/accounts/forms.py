from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, password_validation

User = get_user_model()


class RegisterUserForm(forms.ModelForm):

    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    class Meta:
        model = User
        fields = ['username', 'name', 'email', 'profilePic']


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'profilePic')

class RemoveProfileForm(forms.Form):
    really = forms.BooleanField(
        label=("I'm sure I want to delete my account"),
        required=True,
        help_text=("Are you sure you want to delete your account?"),
    )
