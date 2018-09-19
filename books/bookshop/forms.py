from django import forms
from .models import Category, Product, Comment, Author
    # , Image

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



class SearchForm(forms.Form):
    name = forms.CharField(max_length=64)


class CommentAddForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder':'Cześć, jeżeli masz jakieś przemyślenia odnośnie tej książki, '
                                                           'to inni czytelnicy czekają na Twój wpis..'}
        ))

    class Meta:
        model = Comment
        fields = ('text',)





