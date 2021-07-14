from django.contrib import admin
from .models import Group, User, Event, UserGroup # brings in your Post model from the models.py file
# Register your models here.
my_models = [Group, User, Event, UserGroup]
admin.site.register(my_models)
