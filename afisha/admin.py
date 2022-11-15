from django.contrib.admin import (
    ModelAdmin,
    register,
)
from afisha.models import Event


@register(Event)
class EventAdmin(ModelAdmin):
    pass
# Register your models here.
