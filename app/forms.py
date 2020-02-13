from django import forms
from app.models import User
from app.models import Admin


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'email',
            'password'
        ]


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = [
            'name',
            'email',
            'password'
        ]


class loginform(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
