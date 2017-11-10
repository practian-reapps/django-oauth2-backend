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


class DocumentType(models.Model):
    """
    Tabla para documenttype
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    code = models.CharField(
        capfirst(_('code')),  max_length=15
    )

    name = models.CharField(
        capfirst(_('name')),  max_length=60
    )

    class Meta:
        verbose_name = _("document type")
        verbose_name_plural = _("documents type")
        permissions = (
            ('list_documenttype', 'Can list documenttype'),
            ('get_documenttype', 'Can get documenttype'),
        )

    def __str__(self):
        return self.name


class PersonDocument(models.Model):
    """
    Tabla para persondocument
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    document_type = models.ForeignKey(
        DocumentType, related_name='persondocument_set',
    )
    document_number = models.CharField(
        capfirst(_('document number')),  max_length=100
    )
    expiration_date = models.DateField(
        capfirst(_('expiration date')), null=True, blank=True,
    )
    comments = models.TextField(
        blank=True, null=True
    )
    person = models.ForeignKey(
        Person, related_name='persondocument_set',
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
        verbose_name = _("person document")
        verbose_name_plural = _("persons document")
        permissions = (
            ('list_persondocument', 'Can list persondocument'),
            ('get_persondocument', 'Can get persondocument'),
        )

    def __str__(self):
        return '%s: %s' % (self.document_type.code,
                           self.document_number)
