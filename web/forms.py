from django import forms
from web.models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput

class ContactForms(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'name':TextInput(attrs={'placeholder':"Your name here", 'name':"name"}),
            'phone':TextInput(attrs={'placeholder':"Your phone here",'name':"phone"}),
            'email':TextInput(attrs={'placeholder':"Your email here",'name':"email"}),
            'subject':TextInput(attrs={'placeholder':"Subject here",'name':"subject"}),
            'message':Textarea(attrs={'placeholder':"Message",'class':"custom-textarea",'name':"message",'rows':"3"}),
         }  