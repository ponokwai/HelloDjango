from django import forms
from hello.models import LogMessage

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("first_name","last_name","age","message",)   # NOTE: the trailing comma is required
