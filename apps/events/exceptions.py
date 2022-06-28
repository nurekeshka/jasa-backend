from django.core.exceptions import ValidationError
from .constants import organization_types


def validate_organization_type(value: str):
    if value not in list(map(lambda x: x[0], organization_types)):
        raise ValidationError('Invalid organization type: %s' % value)
