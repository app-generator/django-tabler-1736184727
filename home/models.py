# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    extended1_id = models.TextField(max_length=255, null=True, blank=True)
    extended1_name = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Book(models.Model):

    #__Book_FIELDS__
    title = models.TextField(max_length=255, null=True, blank=True)
    figure = models.TextField(max_length=255, null=True, blank=True)
    publish date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    how much updates = models.IntegerField(null=True, blank=True)

    #__Book_FIELDS__END

    class Meta:
        verbose_name        = _("Book")
        verbose_name_plural = _("Book")


class Updates(models.Model):

    #__Updates_FIELDS__
    bookid = models.ForeignKey(book, on_delete=models.CASCADE)

    #__Updates_FIELDS__END

    class Meta:
        verbose_name        = _("Updates")
        verbose_name_plural = _("Updates")


class Customers(models.Model):

    #__Customers_FIELDS__
    id = models.TextField(max_length=255, null=True, blank=True)
    project_key = models.ForeignKey(projects, on_delete=models.CASCADE)

    #__Customers_FIELDS__END

    class Meta:
        verbose_name        = _("Customers")
        verbose_name_plural = _("Customers")


class Projects(models.Model):

    #__Projects_FIELDS__
    started = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Projects_FIELDS__END

    class Meta:
        verbose_name        = _("Projects")
        verbose_name_plural = _("Projects")



#__MODELS__END
