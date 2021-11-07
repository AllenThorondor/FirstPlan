from django.db.models.signals import post_save
from .models import Lane, Flash
from django.dispatch import receiver
#from .models import Profile

"""
@receiver(post_save, sender=Lane)
def create_flash(sender, instance, created, **kwargs):
    if created:
        Flash.objects.create(lane=instance)

@receiver(post_save, sender=Lane)
def save_flash(sender, instance, **kwargs):
    instance.flash.save()
"""
