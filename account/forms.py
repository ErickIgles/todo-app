from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'
                }
        ))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nomed de usuário'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Senha'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control',  'placeholder': 'Confirme a senha'})
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está em uso.')
        return email

