from typing import Any, Dict, List, Optional

from django import forms
from django.contrib.auth.password_validation import validate_password

from ticketeer.apps.users.models import User


class LoginForm(forms.Form):
    identifier = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Anda'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password Anda'}))

    def authenticate(self) -> Optional[User]:
        identifier = self.cleaned_data.get('identified')
        password = self.cleaned_data.get('password')
        
        try:
            user = User.objects.get(email=identifier)
            
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        return None


class RegistrationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nama Lengkap'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email Anda'}))
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Konfirmasi Password')
    
    def clean_password(self) -> str:
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password
    
    def clean(self) -> Dict[str, Any]:
        data = super().clean()
        if self.errors:
            return data
        
        email = data.get('email')
        password = data.get('password')
        password2 = data.get('password2')

        if User.objects.filter(email=email).exists():
            self.add_error('email', forms.ValidationError('Akun dengan email ini telah tersedia.', 'duplicate_email'))

        if password != password2:
            self.add_error('password2', forms.ValidationError('Password does not match.', 'password_mismatch'))

        return data
    
    def save(self) -> User:
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        return User.objects.create_user(
            name=name, email=email, password=password
        )
