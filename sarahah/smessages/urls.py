from django.conf.urls import url, include

from .views import favoriteMessage


urlpatterns = [
    url(r'favorite/(?P<idMessage>[\w0-9_-]+)/', favoriteMessage, name='favorite'),
]
