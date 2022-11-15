from django.db import models
from django.db.models import (
    Model,
    CharField,
    TextField,
    SlugField,
    BooleanField,
    DateTimeField,
DateField,
TimeField,
)
from djmoney.models.fields import MoneyField
from django.db import models
class Category(Model):
    title = CharField(
        'категория',
        max_length=200
    )
    slug = SlugField(
        'URL',
    )
class Event(Model):
    title = CharField(
        'название',
        max_length=200,
    )
    description = TextField(
        'описание',
        blank=True,
    )
    age = TextField(
        'возраст',
    )
    slug = SlugField(
        'URL',
    )
    date = DateTimeField(
        'дата события',
    )
    category=models.ManyToManyField(Category)
    is_public = BooleanField(
        'опубликовано',
        default=True,
    )
    created = DateTimeField(
        'создано',
        auto_now_add=True,
    )
    updated = DateTimeField(
        'обновлено',
        auto_now=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'событие'
        verbose_name_plural = 'события'

class Date(Model):
    event=models.ManyToManyField(Event)
    date = DateField(
        'дата события',
    )
    time = TimeField(
        'время события',
    )
    price = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency='RUB'
    )
    adress = TextField(
        'адрес',
    )