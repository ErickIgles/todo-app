from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class UserForm(forms.ModelForm):

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome de usuário'
            }
        ),
        label='Nome de Usuário'
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'
            }
        ))

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha'
            }
        ),
        label='Degite um senha'
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme a senha'
            }
        ),
        label='Confirme a senha'
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]

    def clean_email(self):

        email = self.cleaned_data.get('email')

        email_resultado = User.objects.filter(email=email).exists()

        if email_resultado:

            raise forms.ValidationError('Este e-mail já está em uso.')

        return email

    def clean_username(self):

        username = self.cleaned_data.get('username')

        username_resultado = User.objects.filter(username=username).exists()

        if username_resultado:

            raise forms.ValidationError(
                'Nome de usuário indisponível.'
            )

        return username

    def clean(self):

        cleaned_data = super().clean()

        password1 = self.cleaned_data.get('password1')

        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:

            self.add_error(
                'password2',
                'Senhas não são parecidas'
            )

        return cleaned_data

    def save(self, commit=True):

        username = self.cleaned_data.get('username')

        password1 = self.cleaned_data.get('password1')

        email = self.cleaned_data.get('email')

        usuario = User.objects.create_user(
            username=username,
            password=password1,
            email=email
        )

        if commit:

            usuario.save()

        return usuario


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        ),
        label='Digite o seu nome de usuário'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        label='Digite a sua senha'
    )
