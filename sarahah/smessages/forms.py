from django import forms

from .models import Messages

class SendMessage(forms.ModelForm):
    message = forms.CharField(
        label='Message',
        max_length=255,
        widget=forms.Textarea,
        help_text="You have 255 characters remainings"
    )

    class Meta:
        model = Messages
        fields = ('message',)
