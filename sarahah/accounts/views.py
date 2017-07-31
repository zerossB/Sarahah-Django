from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .forms import RegisterUserForm, EditUserForm, RemoveProfileForm
from .models import User

from sarahah.smessages.forms import SendMessage
from sarahah.smessages.models import Messages

# Create your views here.


@login_required
def dashboard(request):
    template_name = "accounts/dashboard.html"
    received = request.user.received.all().order_by('-date_joined')
    send = request.user.sender.all().order_by('-date_joined')
    favorites = request.user.received.filter(favorite=True).order_by('-date_joined')

    context = {
        'received': received,
        'sender': send,
        'favorites': favorites
    }
    return render(request, template_name, context)


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


@login_required
def settings(request, setting):
    template_name = "accounts/settings.html"
    template = "accounts/security/_default.html"
    context = {}
    if setting == "profile":
        form = EditUserForm(instance=request.user)
        context['form'] = form
        template = "accounts/security/_" + setting + ".html"
    elif setting == "changePassword":
        form = PasswordChangeForm(request.user)
        context['form'] = form
        template = "accounts/security/_" + setting + ".html"
    elif setting == "removeProfile":
        form = RemoveProfileForm()
        context['form'] = form
        messages.warning(
            request, "Are you sure that you want to delete your account? Deleting the account is irreversible!"
        )
        template = "accounts/security/_" + setting + ".html"
    else:
        messages.error(request, "Error 404, area does not exist")

    context['template'] = template
    context['setting'] = setting
    return render(request, template_name, context)


@login_required
def editProfile(request):
    if request.method == "POST":
        form = EditUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile successfully edited")
            return redirect('account:dashboard')
    else:
        messages.error(request, "Error 404, Not accessible method")


@login_required
def changePassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('account:dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        messages.error(request, "Error 404, Not accessible method")


@login_required
def removeProfile(request):
    if request.method == "POST":
        form = RemoveProfileForm(request.POST)
        user = get_object_or_404(User, pk=request.user.pk)
        if form.is_valid():
            logout(request)
            user.delete()
            messages.success(request, '')
            return redirect('core:home')
    else:
        messages.error(request, "Error 404, Not accessible method")


def pubProfile(request, profile):
    template_name = "accounts/pubProfile.html"
    received = get_object_or_404(User, username=profile)

    if request.method == "POST":
        form = SendMessage(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.received = received
            if request.user.is_authenticated  :
                form.sender = request.user
            else:
                form.sender = User.objects.all()[0]
            form.save()
            messages.success(
                request, 'Message sent successfully!')
            return redirect('pubProfile', received.username)
    else:
        form = SendMessage()

    context = {
        'received': received,
        'form': form
    }
    return render(request, template_name, context)
