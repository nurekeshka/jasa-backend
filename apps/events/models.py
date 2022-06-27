from .exceptions import validate_organization_type
from .constants import organization_types
from .constants import contact_types
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='name')
    description = models.TextField(verbose_name='description')
    type = models.CharField(max_length=3, choices=organization_types,
                            default=organization_types[0], verbose_name='type',
                            validators=[validate_organization_type])

    class Meta:
        verbose_name = 'organization'
        verbose_name_plural = 'organizations'
        ordering = ('type', 'name')
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    type = models.CharField(max_length=3, choices=contact_types, verbose_name='type')
    value = models.TextField(verbose_name='value')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name='organization')

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ('organization', 'type')
    
    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    organization = models.ForeignKey(Organization, null=True, on_delete=models.SET_NULL, verbose_name='organization')
    tags = models.ManyToManyField(Tag, verbose_name='tags')

    date = models.DateField(verbose_name='date')
    start = models.TimeField(verbose_name='start')
    end = models.TimeField(verbose_name='end')

    longitude = models.FloatField(verbose_name='longitude')
    latitude = models.FloatField(verbose_name='latitude')

    class Meta:
        verbose_name = 'event'
        verbose_name_plural = 'events'
        ordering = ('organization', 'date', 'name')
    
    def __str__(self):
        return self.name
