
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

# Register your models here.
from .models.person import Person
from .models.user import User
from .models.hierarchy_type import HierarchyType
from .models.hierarchy import Hierarchy
from .models.menu import Menu
from .models.user_hierarchy_group import UserHierarchyGroup
from .models.user_hierarchy_permission import UserHierarchyPermission
from .models.person import Religion, Ethnicity, Occupation, EducationLevel
from .models.person import PensionScheme
from .models.person_address import PersonAddressType, PersonAddress
from .models.person_document import DocumentType, PersonDocument
from .models.person_phone import PersonPhoneType, PersonPhone


admin.site.register(ContentType)


class PermissionAdmin(admin.ModelAdmin):
    list_display = ("codename", "name", "content_type")
    search_fields = ("codename", "name", "content_type__app_label")

admin.site.register(Permission, PermissionAdmin)

'''
admin.site.register(Hierarchy)
admin.site.register(HierarchyType)

admin.site.register(UserHierarchyGroup)
admin.site.register(UserHierarchyPermission)
admin.site.register(Menu)
'''
admin.site.register(Person)
admin.site.register(Religion)
admin.site.register(Ethnicity)
admin.site.register(Occupation)
admin.site.register(EducationLevel)
admin.site.register(PensionScheme)

admin.site.register(PersonAddressType)
admin.site.register(PersonAddress)

admin.site.register(DocumentType)
admin.site.register(PersonDocument)

admin.site.register(PersonPhoneType)
admin.site.register(PersonPhone)

# forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


CHOICES = (('ON', 'ON'),
           ('OFF', 'OFF'),
           )


class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User  # get_user_model()


class MyUserChangeForm(UserChangeForm):
    description = forms.CharField(
        label=_('Description'), required=False, initial='edit',
        widget=forms.Textarea)
    # is_staff = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta(UserChangeForm.Meta):
        model = User  # get_user_model()


class MyUserAdmin(UserAdmin):

    """ """
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'),
         {'fields': ('email',)}),
        (_('Permissions'), {'fields': ('is_active', 'description', 'is_staff',
                                       'is_superuser', 'groups',
                                       'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    form = MyUserChangeForm
    add_form = MyUserCreationForm

    list_display = ('username', 'email',
                    'first_name', 'last_name', 'is_staff', )  # 'status'

    list_filter = ('is_staff', 'is_superuser',
                   'is_active', 'groups', 'date_joined')

    #date_hierarchy = 'date_joined'

    def status(self, obj):
        return obj.status

    status.admin_order_field = 'status'
    status.short_description = 'status'

    # raw_id_fields = ('person',)

    '''
    def save_model(self, request, obj, form, change):
        if obj.pk:
            if obj.is_active:
                if UserStatus.objects.filter(user=obj.pk).count() > 0:
                    if UserStatus.objects.filter(user=obj.pk).latest('id').status != ON:
                        UserStatus.objects.create(
                            status=ON,
                            description=form.cleaned_data['description'], user=obj)
                else:  # no tiene registros en UserStatus
                    UserStatus.objects.create(
                        status=ON,
                        description=form.cleaned_data['description'], user=obj)
            else:
                if UserStatus.objects.filter(user=obj.pk).count() > 0:
                    if UserStatus.objects.filter(user=obj.pk).latest('id').status != OFF:
                        UserStatus.objects.create(
                            status=OFF,
                            description=form.cleaned_data['description'], user=obj)
                else:
                    UserStatus.objects.create(
                        status=OFF,
                        description=form.cleaned_data['description'], user=obj)
        obj.save()
    '''

    def get_queryset(self, request):
        qs = super(MyUserAdmin, self).get_queryset(request)
        # qr = qs.with_status()  # add 'status' colum
        # print qr
        return qs

    '''
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == 'status':
            kwargs['choices'] = (
                (ON, 'Accepted'),
                (OFF, 'Denied'),
                (True, 'Denied'),
                (False, 'Denied'),
                (None, 'Denied'),
                (0, 'Denied'),
                (1, 'Denied'),
                ('0', 'Denied'),
                ('1', 'Denied'),
                ('True', 'Denied'),
                ('False', 'Denied'),
            )
        # db_field['status'].choices = (
        #     (ON, 'Accepted'),
        #     (OFF, 'Denied'),
        # )
        return super(MyUserAdmin, self).formfield_for_choice_field(db_field,
            request, **kwargs)
    '''
admin.site.register(User, MyUserAdmin)
