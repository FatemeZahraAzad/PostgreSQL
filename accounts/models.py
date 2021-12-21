from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import related


class CustomUser(AbstractUser):
    pass


class Change(models.Model):
    Reference = models.CharField(max_length=100)
    Choices = (("Pending","Pending"),("In Progress","In Progress"),("Closed","Closed"))
    Status = models.CharField(choices=Choices, default=1, max_length=11)
    user = models.ForeignKey(CustomUser,on_delete = models.CASCADE , related_name = 'change')
    class Meta:
        ordering = ['Status']

class ClosedChange(Change):
    class Meta:
        proxy = True
        verbose_name = u"Closed Changes"