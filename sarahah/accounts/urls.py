from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.views import login, logout


from .views import dashboard, register, settings, editProfile, changePassword, removeProfile

urlpatterns = [
    url(r'^$', dashboard, name="dashboard"),
    url(r'^login/$', login, {'template_name':'accounts/login.html'}, name="login"),
    url(r'^logout/$', logout, {'next_page':'core:home'}, name="logout"),
    url(r'^register/', register, name="register"),
    url(r'^settings/(?P<setting>[\w0-9_-]+)/', settings, name="settings"),

    url(r'^edit/', editProfile, name="editProfile"),
    url(r'^cgdPassword/', changePassword, name="changePassword"),
    url(r'^rmvProfile/', removeProfile, name="removeProfile"),
]
