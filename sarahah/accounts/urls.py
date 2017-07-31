from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.views import login, logout

#from .views import register, dashboard, edit, changePassword, password_reset, password_reset_confirm
from .views import dashboard, register

urlpatterns = [
    url(r'^login/$', login, {'template_name':'accounts/login.html'}, name="login"),
    url(r'^logout/$', logout, {'next_page':'core:home'}, name="logout"),
    url(r'^$', dashboard, name="dashboard"),
    url(r'^register/', register, name="register"),
]