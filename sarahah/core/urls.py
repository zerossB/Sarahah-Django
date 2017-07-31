from django.conf.urls import url, include

from .views import home, aboutus, contact


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^about-us/$', aboutus, name='about'),
    url(r'^contact/$', contact, name='contact'),
]
