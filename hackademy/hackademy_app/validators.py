from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_url(value):
    if 'https://github.com/' not in str(value):
        raise ValidationError(
            _('%(value)s IS INVALID URL! IT NEEDS TO BE WITH GITHUB DOMAIN'),
            params={'value': value},
        )
