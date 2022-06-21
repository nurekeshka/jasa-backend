from .constants import organization_types
from .constants import contact_types
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='name')
    type = models.CharField(max_length=3, choices=organization_types, default=organization_types[0], verbose_name='type')

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
