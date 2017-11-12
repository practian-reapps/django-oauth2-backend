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


class PersonPhoneType(models.Model):
    """
    Tabla para personphonetype
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    code = models.CharField(
        capfirst(_('code')),  max_length=15
    )

    name = models.CharField(
        capfirst(_('name')),  max_length=60
    )

    class Meta:
        verbose_name = _("person phone type")
        verbose_name_plural = _("person phone type")
        permissions = (
            ('list_personphonetype', 'Can list personphonetype'),
            ('get_personphonetype', 'Can get personphonetype'),
        )

    def __str__(self):
        return self.name


class PersonPhone(models.Model):
    """
    Tabla para personphone
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    person_phone_type = models.ForeignKey(
        PersonPhoneType, related_name='personphone_set',
    )

    area_code = models.CharField(
        capfirst(_('area code')), max_length=5, null=True, blank=True,
        help_text=_('area code'),
    )
    local_number = models.CharField(
        capfirst(_('local number')), max_length=20, null=True, blank=True,
        help_text=_('local number'),
    )

    is_default = models.BooleanField(
        capfirst(_('is default')), default=False
    )
    is_sms_receiver = models.BooleanField(
        capfirst(_('is SMS receiver')), default=False
    )

    person = models.ForeignKey(
        Person, related_name='personphone_set',
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
        verbose_name = _("person phone")
        verbose_name_plural = _("persons phone")
        permissions = (
            ('list_personphone', 'Can list personphone'),
            ('get_personphone', 'Can get personphone'),
        )

    def __str__(self):
        return '%s: %s%s' % (self.person_phone_type.code,
                             self.area_code, self.local_number)
