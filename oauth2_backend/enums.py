"""
Enums de la app
"""
from django.utils.translation import ugettext_lazy as _
from django.utils.text import capfirst

APP_001 = 'APP_001'
APP_002 = 'APP_002'
APP_003 = 'APP_003'
APP_004 = 'APP_004'
APP_005 = 'APP_005'
APP_006 = 'APP_006'
APP_007 = 'APP_007'
APP_008 = 'APP_008'
APP_009 = 'APP_009'
APP_010 = 'APP_010'

WEB = 'WEB'
ADMISION = 'ADMISION'
BACKEND = 'BACKEND'
OTHER = 'OTHER'
MODULE_CHOICES = (
    (APP_001, 'APP_001'),
    (APP_002, 'APP_002'),
    (APP_003, 'APP_003'),
    (APP_004, 'APP_004'),
    (APP_005, 'APP_005'),
    (APP_006, 'APP_006'),
    (APP_007, 'APP_007'),
    (APP_008, 'APP_008'),
    (APP_009, 'APP_009'),
    (APP_010, 'APP_010'),

    (OTHER, capfirst(_('other'))),
    (BACKEND, 'Backend Manager'),
    (ADMISION, 'Admisión'),
    (WEB, 'Web informativa'),
)


HIERARCHY_TYPE_CHOICES = (
    ('INSTITUCION', 'Institucion'),
    ('FILIAL', 'Filial'),
    ('FACULTAD', 'Facultad'),
    ('ESCUELA', 'Escuela'),
    ('CARRERA', 'Carrera'),
    ('DEPARTAMENTO_ACAD', 'Departamento acad.'),
    (OTHER, capfirst(_('other'))),
)

MALE = 'MALE'
FEMALE = 'FEMALE'
GENDER_CHOICES = (
    (MALE, _('Male')),
    (FEMALE, _('Female')),
    (OTHER, capfirst(_('other'))),
)

SINGLE = 'SINGLE'
MARRIED = 'MARRIED'
WIDOWED = 'WIDOWED'
DIVORCED = 'DIVORCED'
REGISTERED_PARTNERSHIP = 'REGISTERED_PARTNERSHIP'
MARITAL_STATUS_CHOICES = (
    (SINGLE, _('Masculino')),
    (MARRIED, capfirst(_('Married'))),
    (WIDOWED, capfirst(_('Widowed'))),
    (DIVORCED, capfirst(_('Divorced'))),
    (REGISTERED_PARTNERSHIP, capfirst(_('Registered partnership'))),
    (OTHER, capfirst(_('other'))),
)
