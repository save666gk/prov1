from django import forms
from .models import Post
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm


class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = '__all__'

   def clean(self):
       cleaned_data = super().clean()
       title = cleaned_data.get("title")
       text = cleaned_data.get("text")

       if text == title:
           raise ValidationError(
               "Описание не должно быть идентичным названию."
           )

       return cleaned_data


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        return user

