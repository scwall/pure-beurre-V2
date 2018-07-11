from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.



class Categorie(models.Model):
    name = models.CharField(max_length=150)
    id_category = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    user_product = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='favourite_product')
    categorie = models.ManyToManyField(Categorie, related_name='products')
    name = models.CharField(max_length=150)
    link_http = models.URLField()
    link_picture = models.URLField()
    description = models.TextField()
    nutrition_grade = models.CharField(max_length=1)
    saturated_fat_100g = models.FloatField(null=True)
    carbohydrates_100g = models.FloatField(null=True)
    energy_100g = models.FloatField(null=True)
    sugars_100g = models.FloatField(null=True)
    sodium_100g = models.FloatField(null=True)

    def __str__(self):
        return self.name

# class SignUpForm(UserCreationForm):
#     username = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
#
#     class Meta:
#         model = User
#         fields = ("nom d'utilisateur", 'Prénom', 'Nom', 'email', 'mot de passe', 'retapper le mot de passe', )