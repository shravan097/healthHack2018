
from django.db import models
# Create your models here.
from django.forms import ModelForm,forms
from django import forms
from django.db import models
from datetime import date
import os


# Create your models here.

class File(models.Model):
    yearOfBirth = models.IntegerField(blank=False)
    gender = models.CharField(max_length=6, blank=False)

    symptom = models.CharField(max_length=1000,blank=False)


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['yearOfBirth','gender','symptom']