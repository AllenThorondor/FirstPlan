from django.contrib import admin
from .models import (
    Collection,
    CollectionImage,
    Person,
    PersonImage,
    Event,
    EventImage)
# Register your models here.
admin.site.register(Collection)
admin.site.register(CollectionImage)
admin.site.register(Person)
admin.site.register(PersonImage)
admin.site.register(Event)
admin.site.register(EventImage)
