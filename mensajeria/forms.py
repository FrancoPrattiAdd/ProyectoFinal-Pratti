# mensajeria/forms.py
from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['emisor', 'receptor', 'body'] 
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  
        }
