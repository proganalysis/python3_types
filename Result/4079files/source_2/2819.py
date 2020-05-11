from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from solo.admin import SingletonModelAdmin

from .models import (
    Asset, Cashdesk, CashdeskSession, EventSettings, Item, ItemMovement,
    ListConstraint, ListConstraintEntry, ListConstraintProduct, Preorder,
    PreorderPosition, Product, ProductItem, Quota, TimeConstraint, Transaction,
    TransactionPosition, User, WarningConstraint, WarningConstraintProduct,
)


class EventSettingsAdminForm(forms.ModelForm):
    class Meta:
        model = EventSettings
        exclude = []
        widgets = {
            'invoice_address': forms.widgets.Textarea,
            'invoice_footer': forms.widgets.Textarea,
            'receipt_address': forms.widgets.Textarea,
            'receipt_footer': forms.widgets.Textarea,
        }


@admin.register(EventSettings)
class EventSettingsAdmin(SingletonModelAdmin):
    form = EventSettingsAdminForm


@admin.register(User)
class AuthorAdmin(BaseUserAdmin):
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('username', 'password', 'auth_token')}),
        ('Personal info', {'fields': ('firstname', 'lastname')}),
        (
            'Permissions',
            {
                'fields': (
                    'is_active',
                    'is_superuser',
                    'is_backoffice_user',
                    'is_troubleshooter',
                )
            },
        ),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (
            None,
            {'classes': ('wide',), 'fields': ('username', 'password1', 'password2')},
        ),
    )
    list_display = (
        'username',
        'firstname',
        'lastname',
        'is_active',
        'is_superuser',
        'is_backoffice_user',
        'is_troubleshooter',
    )
    list_filter = (
        'is_active',
        'is_superuser',
        'is_backoffice_user',
        'is_troubleshooter',
    )
    search_fields = ('firstname', 'lastname', 'username')
    ordering = ('username',)
    filter_horizontal = []


class ProductItemInline(admin.TabularInline):
    model = ProductItem
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_visible')
    list_filter = ('is_visible', 'requires_authorization')
    search_fields = ('name',)
    inlines = (ProductItemInline,)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'initial_stock')
    search_fields = ('name',)


@admin.register(Cashdesk)
class CashdeskAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip_address', 'printer_queue_name', 'is_active')
    search_fields = ('name',)
    list_filter = ('is_active',)


class ItemMovementInline(admin.TabularInline):
    model = ItemMovement
    extra = 1


@admin.register(CashdeskSession)
class CashdeskSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'cashdesk', 'user', 'start', 'end')
    list_filter = ('start', 'end', 'cashdesk', 'user')
    inlines = (ItemMovementInline,)


@admin.register(Quota)
class QuotaAdmin(admin.ModelAdmin):
    list_display = ('name', 'size')


@admin.register(TimeConstraint)
class TimeConstriantAdmin(admin.ModelAdmin):
    list_display = ('name', 'start', 'end')


class ListConstraintProductInline(admin.TabularInline):
    model = ListConstraintProduct
    extra = 1


@admin.register(ListConstraint)
class ListConstriantAdmin(admin.ModelAdmin):
    list_display = ('name',)
    exclude = ('products',)
    inlines = (ListConstraintProductInline,)


@admin.register(ListConstraintEntry)
class ListConstraintAdmin(admin.ModelAdmin):
    list_display = ('name', 'identifier', 'list')
    list_filter = ('list',)
    search_fields = ('name', 'identifier')


class PreorderPositionInline(admin.TabularInline):
    model = PreorderPosition
    extra = 1


@admin.register(Preorder)
class PreorderAdmin(admin.ModelAdmin):
    list_filter = ('is_paid',)
    list_display = ('order_code', 'is_paid')
    search_fields = ('order_code',)
    inlines = (PreorderPositionInline,)


class WarningConstraintProductInline(admin.TabularInline):
    model = WarningConstraintProduct
    extra = 1


@admin.register(WarningConstraint)
class WarningConstriantAdmin(admin.ModelAdmin):
    list_display = ('name',)
    exclude = ('products',)
    inlines = (WarningConstraintProductInline,)


class TransactionPositionInline(admin.TabularInline):
    model = TransactionPosition
    fields = (
        'type',
        'value',
        'tax_rate',
        'tax_value',
        'product',
        'reverses',
        'listentry',
        'preorder_position',
        'authorized_by',
    )

    def get_readonly_fields(self, request, obj=None):
        return TransactionPositionInline.fields

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'datetime', 'session')
    fields = ('id', 'datetime', 'session', 'cash_given')
    inlines = (TransactionPositionInline,)

    def get_readonly_fields(self, request, obj=None):
        return TransactionAdmin.fields

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.unregister(Group)

admin.site.register(Asset)
