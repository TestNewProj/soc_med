from django import forms
from .models import Post, Comment, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['title', 'content', 'tags']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text'] 
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control', # Стиль Бутстрапа
                'rows': 3,
                'placeholder': 'Ваш комментарий...'
            }),
        }

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']