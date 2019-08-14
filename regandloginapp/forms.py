from django import forms
from .models import Regmodel
class Regform(forms.ModelForm):
    class Meta:
        model=Regmodel
        widgets={'password':forms.PasswordInput(), 'conform_password':forms.PasswordInput()}
        fields=['user_name','password','conform_password','first_name','last_name','date_of_birth','mobile_number','email_id']

class Login(forms.Form):
    user_name=forms.CharField(max_length=20)
    password=forms.CharField(widget=forms.PasswordInput())
