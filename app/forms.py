from django import forms
from django.db import models
from django.db.models import fields
from app.models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'