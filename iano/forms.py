from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from mainapp.models import User







class student(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( 'full_name', 'email','phone','username', 'password1', 'password2', )
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_group_leader = True
        if commit:
            user.save()
        return user

class teacher(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ( 'full_name', 'email','phone','username', 'password1', 'password2', )
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_group_leader = True
        if commit:
            user.save()
        return user