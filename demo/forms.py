from django import forms
from django.contrib.auth.models import User
from .models import Email,Moblie
class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('id','email')
class MobileForm(forms.ModelForm):
        class Meta:
           model =Moblie
           fields = ('email_id','moblie')    
