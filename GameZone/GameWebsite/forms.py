# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
# from .models import Profile

# class ProfilePicForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('username','email' ,"profile_image" )
#         labels = {
#             'username': 'Username',
#             'email': 'Email address',
#             'profile_image': 'Update profile picture',
#         }

#         widgets = {
#             'username' : forms.TextInput(attrs={'class' : 'form-control'}),
#             'email' : forms.EmailInput(attrs={'class' : 'form-control'}),
#         }
from django import forms

from django.contrib.auth.models import User
from .models import Profile


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['pic']