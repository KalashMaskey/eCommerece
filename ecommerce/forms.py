from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()
class ContactForm(forms.Form):
    name = forms.CharField(max_length=256,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder":"Full Name"
                }
                )
            )
    email = forms.EmailField(widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'Email'
            }
    ))
    content = forms.CharField(widget = forms.Textarea(
            attrs={
            'class':'form-control',
            'placeholder': 'Your Message'
            }
            )
        )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "gmail.com" in email:
            raise forms.ValidationError("Provide Valid Email")
        return email

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    def clean_username(self):
          username = self.cleaned_data.get('username')
          qs = User.objects.filter(username=username)
          if qs.exists():
              raise forms.ValidationError("Username is already taken")
          return username
    def clean(self):
          data = self.cleaned_data
          password = self.cleaned_data.get('password')
          password2 = self.cleaned_data.get('password2')
          if password2 != password:
              raise forms.ValidationError("Passwords Must Match")
          return data
