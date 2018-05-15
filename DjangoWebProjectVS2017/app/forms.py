"""
Definition of forms.
"""

from django import forms
from app.models import Question,Choice,User
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class FormPregunta (forms.ModelForm):

        class Meta:
            fields = ('question_text','choice_text','choice_text','choice_text',)

class QuestionForm(forms.ModelForm):
        tema = forms.CharField(widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
            }
        ))

        question_text = forms.CharField(widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
            }
        ))

        respCorrecta = forms.IntegerField(widget=forms.NumberInput(
           attrs={
               'class' : 'form-control', 'type' :'Number',
            }
        ))

        class Meta:
                model = Question
                fields = ('question_text','tema','respCorrecta',)
            

class ChoiceForm(forms.ModelForm):

        class Meta:
            model = Choice
            fields = ('choice_text',)

class UserForm(forms.ModelForm):

        class Meta:
            model = User
            fields = ('email','nombre',)

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
