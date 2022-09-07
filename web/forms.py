from django import forms
from web.models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput

class ContactForms(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'name':TextInput(attrs={'placeholder':"اسمك هنا", 'name':"name"}),
            'phone':TextInput(attrs={'placeholder':"هاتفك هنا",'name':"phone"}),
            'email':TextInput(attrs={'placeholder':"بريدك الإلكتروني هنا",'name':"email"}),
            'subject':TextInput(attrs={'placeholder':"الموضوع هنا",'name':"subject"}),
            'message':Textarea(attrs={'placeholder':"رسالة",'class':"custom-textarea",'name':"message",'rows':"3"}),
         }  