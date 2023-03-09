from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Raiting, RaitingStar


class RaitingForm(forms.ModelForm):
    star = forms.ModelChoiceField(
        queryset=RaitingStar.objects.all(),
        widget=forms.RadioSelect,
        empty_label=None,)

    class Meta:
        model=Raiting
        fields = ('star',)
