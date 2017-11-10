import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst, get_text_list
from django.dispatch import receiver
from django.db.models import signals
from unicodedata import normalize
from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS
from ..enums import GENDER_CHOICES, MARITAL_STATUS_CHOICES

# models
# others


class Religion(models.Model):
    """
    Tabla para religion
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    code = models.CharField(
        capfirst(_('code')),  max_length=15
    )
    name = models.CharField(
        capfirst(_('name')),  max_length=60
    )
    is_adventist = models.BooleanField(
        capfirst(_('is adventist')), default=False
    )

    class Meta:
        verbose_name = _("religion")
        verbose_name_plural = _("religions")
        permissions = (
            ('list_religion', 'Can list religion'),
            ('get_religion', 'Can get religion'),
        )

    def __str__(self):
        return self.name


class Ethnicity(models.Model):
    """
    Tabla para ethnicity
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    code = models.CharField(
        capfirst(_('code')),  max_length=15
    )

    name = models.CharField(
        capfirst(_('name')),  max_length=60
    )

    class Meta:
        verbose_name = _("ethnicity")
        verbose_name_plural = _("ethnicitys")
        permissions = (
            ('list_ethnicity', 'Can list ethnicity'),
            ('get_ethnicity', 'Can get ethnicity'),
        )

    def __str__(self):
        return self.name


class Occupation(models.Model):
    """
    Tabla para occupation
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    code = models.CharField(
        capfirst(_('code')),  max_length=15
    )

    name = models.CharField(
        capfirst(_('name')),  max_length=60
    )

    class Meta:
        verbose_name = _("occupation")
        verbose_name_plural = _("occupation")
        permissions = (
            ('list_occupation', 'Can list occupation'),
            ('get_occupation', 'Can get occupation'),
        )

    def __str__(self):
        return self.name


class EducationLevel(models.Model):
    """
    Tabla para educationlevel
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    code = models.CharField(
        capfirst(_('code')),  max_length=15
    )

    name = models.CharField(
        capfirst(_('name')),  max_length=60
    )

    class Meta:
        verbose_name = _("education level")
        verbose_name_plural = _("educations level")
        permissions = (
            ('list_educationlevel', 'Can list educationlevel'),
            ('get_educationlevel', 'Can get educationlevel'),
        )

    def __str__(self):
        return self.name


class PensionScheme(models.Model):
    """
    Tabla para pensionscheme
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    code = models.CharField(
        capfirst(_('code')),  max_length=15
    )

    name = models.CharField(
        capfirst(_('name')),  max_length=60
    )

    class Meta:
        verbose_name = _("pension scheme")
        verbose_name_plural = _("pensions scheme")
        permissions = (
            ('list_pensionscheme', 'Can list pensionscheme'),
            ('get_pensionscheme', 'Can get pensionscheme'),
        )

    def __str__(self):
        return self.name


class Person(models.Model):

    """
    Tabla para persons
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    national_id_doc = models.CharField(
        capfirst(_('national identity document or tax identification number')),
        max_length=20,
        null=True, blank=True,
        help_text=_(
            'national identity document(DNI) or tax identification number(RUC)'
        ),
    )  # extend person documents in DocumentPersonType
    first_name = models.CharField(
        capfirst(_('first name or legal name')), max_length=50,
        help_text=_(
            'primer nombre or legal name'
        ),
    )
    other_names = models.CharField(
        capfirst(_('other names')), max_length=50, null=True, blank=True,
        help_text=_(
            'otros nombres'
        ),
    )
    last_name = models.CharField(
        capfirst(_('last name')), max_length=50, null=True, blank=True,
        help_text=_(
            'apellido paterno'
        ),
    )
    mother_last_name = models.CharField(
        capfirst(_('mother\'s last name')), max_length=50,
        null=True, blank=True,
        help_text=_(
            'apellido materno'
        ),
    )
    acronym = models.CharField(
        capfirst(_('acronym')), max_length=30, null=True, blank=True,
        help_text=_(
            'acronym'
        ),
    )
    photo = models.ImageField(
        capfirst(_('photo')), upload_to='persons',
        default='persons/default.png', null=True, blank=True,
        help_text=_(
            'photo or logo'
        ),
    )
    acronym = models.CharField(
        capfirst(_('acronym')), max_length=50, null=True, blank=True,
        help_text=_(
            'acronym'
        ),
    )
    birth_date = models.DateField(
        _('birth date'), null=True, blank=True
    )
    birth_place = models.TextField(
        capfirst(_('birth place')), null=True, blank=True,
        help_text=_('birth place'),
    )
    ubigeo = models.CharField(
        capfirst(_('ubigeo')), max_length=15, null=True, blank=True,
        help_text=_('ubigeo'),
    )
    marital_status = models.CharField(
        capfirst(_('marital status')), max_length=50, null=True, blank=True,
        help_text=_('marital status'), choices=MARITAL_STATUS_CHOICES
    )
    gender = models.CharField(
        capfirst(_('gender')), max_length=10, null=True, blank=True,
        help_text=_('gender M/F'), choices=GENDER_CHOICES
    )
    blood_type = models.CharField(
        capfirst(_('blood type')), max_length=50, null=True, blank=True,
        help_text=_('blood type'),
    )
    email = models.CharField(
        capfirst(_('email')), max_length=50, null=True, blank=True,
        help_text=_('email'),
    )

    religion = models.ForeignKey(
        Religion, related_name='person_set', null=True, blank=True,
    )
    baptism_date = models.DateField(
        _('baptism date'), null=True, blank=True
    )
    decease_date = models.DateField(
        _('decease date'), null=True, blank=True
    )
    father = models.ForeignKey(
        'self', related_name='person_father', null=True, blank=True
    )
    mother = models.ForeignKey(
        'self', related_name='person_mother', null=True, blank=True
    )
    spouse = models.ForeignKey(
        'self', related_name='person_spouse', null=True, blank=True
    )
    ethnicity = models.ForeignKey(
        Ethnicity, related_name='person_set', null=True, blank=True,
    )
    occupation = models.ForeignKey(
        Occupation, related_name='person_set', null=True, blank=True,
    )
    education_level = models.ForeignKey(
        EducationLevel, related_name='person_set', null=True, blank=True,
    )
    pension_scheme = models.ForeignKey(
        PensionScheme, related_name='person_set', null=True, blank=True,
    )

    region_code = models.CharField(
        capfirst(_('region code')), max_length=10, null=True, blank=True,
    )
    time_zone_info_id = models.CharField(
        capfirst(_('time zone info id')), max_length=100,
        null=True, blank=True,
    )

    is_adventist = models.BooleanField(
        capfirst(_('is adventist')), default=True
    )
    is_legal_entity = models.BooleanField(
        capfirst(_('is legal entity')), default=False
    )
    country_residence_code = models.CharField(
        capfirst(_('country residence code')), max_length=20,
        null=True, blank=True,
        help_text=_(
            'country residence code'
        ),
    )

    status = models.IntegerField(
        capfirst(_('status')), default=1,
        help_text=_(
            'status: 0: eliminado, 1: sin validar, 2: validado'
        ),
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
    # colocar debajo tus nuevos campos

    class Meta:
        verbose_name = capfirst(_('person'))
        verbose_name_plural = capfirst(_('persons'))
        '''
        unique_together = (
            ('first_name', 'other_names', 'last_name', 'mother_last_name',
                'national_id_doc'),
            ('national_id_doc'),
        )
        '''

    def __str__(self):
        return '%s %s (%s)' % (self.first_name,
                               self.last_name,
                               self.national_id_doc)
