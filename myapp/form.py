from django.forms import ModelForm
from .models import *


class form_form(ModelForm):
    class Meta:
        model=form
        fields='__all__'


class employe_form(ModelForm):
    class meta:
        model=employe
        fields="__all__"
