from django.core.validators import RegexValidator
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError('Phone number must contain only numeric digits.')
    if len(value) != 11:
        raise ValidationError('Phone number must contain 11 digits')

def validate_name_format(value):
    pattern = r'^[A-Za-z\s]*$'
    if not re.match(pattern, value):
        raise ValidationError('Name must contain only letters and spaces.')
    