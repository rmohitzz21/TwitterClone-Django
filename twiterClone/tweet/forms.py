from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        # widgets = {
        #     'text': forms.Textarea(attrs={'rows': 2}),
        # }

class UserRegistarationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# field is used to specify the fields that we want to include in the form. In this case, we are including the text and photo fields from the Tweet model.
# UserCreationForm is a built-in form provided by Django for user registration. We are extending it to add an email field.
# model : user is the model that we are using for the form.