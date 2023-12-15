from django.apps import AppConfig
from django.core.signals import setting_changed
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import projectmodel

@receiver(post_save, sender = projectmodel)
def projectmodel_savehandler(sender, instance, created, **kwargs):
    if created:
        a = "New project was created"
        print(a)