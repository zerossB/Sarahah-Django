from django.shortcuts import render, redirect, get_object_or_404

from .models import Messages

# Create your views here.
def favoriteMessage(request, idMessage):
    if request.method == "POST":
        message = get_object_or_404(Messages, pk=idMessage)
        favr = message.favorite
        print( message.favorite )
        message.favorite = not favr
        print( message.favorite )
        message.save()
        return redirect("account:dashboard")
    else:
        return redirect("account:dashboard")