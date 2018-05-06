# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.db import models

from .utils import code_generator
User = settings.AUTH_USER_MODEL

# Create your models here.
def upload_location(instance, filename):
    username = instance.user.username
    return "profiles/avatar/%s/%s_%s" % (username, username, filename)


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating
    ``created`` and ``modified`` fields.
    """

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

class Profile(TimeStampedModel):
    user = models.OneToOneField(User, primary_key=True)
    activation_key = models.CharField(max_length=120, blank=True, null=True)
    activated = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to=upload_location,
                               blank=True,
                               height_field="height_field",
                               width_field="width_field",
                               default="")
    height_field = models.IntegerField(default=0, blank=True, null=True)
    width_field = models.IntegerField(default=0, blank=True, null=True)
    telefono = models.CharField(max_length=250, blank=True, null=True)
    direccion = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def send_activation_email(self):
        current_site = Site.objects.get_current().domain
        if not self.activated:
            self.activation_key = code_generator()
            self.save()
            path_ = reverse('activate', kwargs={"code": self.activation_key})

            # Send email
            subject = "Activa tu cuenta"
            from_email = settings.DEFAULT_FROM_EMAIL
            message = "Activa tu cuenta aquí: {}".format(path_)
            recipient_list = [self.user.email, ]
            html_message = "<p>Activa tu cuenta aquí: <a href='http://{}{}'>Activation link</a></p>".format(
                current_site, path_)
            sent_mail = send_mail(subject,
                                  message,
                                  from_email,
                                  recipient_list,
                                  fail_silently=False,
                                  html_message=html_message)
            return sent_mail




