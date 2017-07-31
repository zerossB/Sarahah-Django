from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required

from .forms import RegisterUserForm

# Create your views here.


@login_required
def dashboard(request):
    template_name = "accounts/dashboard.html"
    return render(request, template_name)


def register(request):
    template_name = "accounts/register.html"
    if request.method == "POST":
        form = RegisterUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username,
                password=form.cleaned_data['password1']
            )
            messages.success(
                request, 'Register now, just use our platform!')
            login(request, user)
            return redirect('account:dashboard')
    else:
        form = RegisterUserForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)
