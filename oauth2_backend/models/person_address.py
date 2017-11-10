import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst, get_text_list
from django.dispatch import receiver
from django.db.models import signals
from unicodedata import normalize
from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS

# models
from .person import Person


class PersonAddressType(models.Model):
    """
    Tabla para personaddresstype
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    code = models.CharField(
        capfirst(_('code')),  max_length=15
    )

    name = models.CharField(
        capfirst(_('name')),  max_length=60
    )

    class Meta:
        verbose_name = _("person address type")
        verbose_name_plural = _("person address type")
        permissions = (
            ('list_personaddresstype', 'Can list personaddresstype'),
            ('get_personaddresstype', 'Can get personaddresstype'),
        )

    def __str__(self):
        return self.name


class PersonAddress(models.Model):
    """
    Tabla para personaddress
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    person_address_type = models.ForeignKey(
        PersonAddressType, related_name='personaddress_set',
    )
    zip_postal_code = models.CharField(
        capfirst(_('zip postal code')),  max_length=20
    )
    ubigeo = models.CharField(
        capfirst(_('ubigeo')), max_length=15, null=True, blank=True,
        help_text=_('ubigeo'),
    )
    address_main = models.TextField(
        blank=True, null=True
    )
    address_alt = models.TextField(
        blank=True, null=True
    )
    is_mailing_address = models.BooleanField(
        capfirst(_('is mailing address')), default=False
    )

    person = models.ForeignKey(
        Person, related_name='personaddress_set',
    )

    created_at = models.DateTimeField(
        _('created at'), auto_now_add=True
    )
    updated_at = models.DateTimeField(
        _('updated at'), auto_now=True, blank=True, null=True
    )
    registered_by = models.TextField(
        blank=True, null=True
    )

    class Meta:
        verbose_name = _("person address")
        verbose_name_plural = _("persons address")
        permissions = (
            ('list_personaddress', 'Can list personaddress'),
            ('get_personaddress', 'Can get personaddress'),
        )

    def __str__(self):
        return '%s: %s' % (self.person_address_type.code,
                           self.ubigeo)
