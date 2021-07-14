from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  active = models.BooleanField(default=True)
  viewed_tutorial = models.BooleanField(default=False, blank=True)

class Group(models.Model):
  owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_groups')
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=1000)
  members = models.ManyToManyField(User, through='UserGroup', related_name='all_members')

  def __str__(self):
    return f"Title: {self.title}"

class Event(models.Model):
  group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='events')
  name = models.CharField(max_length=200)
  date = models.DateTimeField()
  description = models.TextField(max_length=1000)
  image_url = models.CharField(max_length=250)

  def __str__(self):
    return f"{self.name}"

class UserGroup(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
