from django.contrib import admin
from . import models 
from django import forms
from .models import Bet
# Register your models here.

admin.site.register(models.Bet)