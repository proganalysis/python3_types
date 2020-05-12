# (generated with --quick)

from typing import Any, Tuple

Asset: Any
AuthorAdmin: Any
BaseUserAdmin: Any
Cashdesk: Any
CashdeskAdmin: Any
CashdeskSession: Any
CashdeskSessionAdmin: Any
EventSettings: Any
EventSettingsAdmin: Any
Group: Any
Item: Any
ItemAdmin: Any
ItemMovement: Any
ListConstraint: Any
ListConstraintAdmin: Any
ListConstraintEntry: Any
ListConstraintProduct: Any
ListConstriantAdmin: Any
Preorder: Any
PreorderAdmin: Any
PreorderPosition: Any
Product: Any
ProductAdmin: Any
ProductItem: Any
Quota: Any
QuotaAdmin: Any
SingletonModelAdmin: Any
TimeConstraint: Any
TimeConstriantAdmin: Any
Transaction: Any
TransactionAdmin: Any
TransactionPosition: Any
User: Any
WarningConstraint: Any
WarningConstraintProduct: Any
WarningConstriantAdmin: Any
admin: Any
forms: Any

class EventSettingsAdminForm(Any):
    Meta: type

class ItemMovementInline(Any):
    extra: int
    model: Any

class ListConstraintProductInline(Any):
    extra: int
    model: Any

class PreorderPositionInline(Any):
    extra: int
    model: Any

class ProductItemInline(Any):
    extra: int
    model: Any

class TransactionPositionInline(Any):
    fields: Tuple[str, str, str, str, str, str, str, str, str]
    model: Any
    def get_readonly_fields(self, request, obj = ...) -> Tuple[str, str, str, str, str, str, str, str, str]: ...
    def has_add_permission(self, request) -> bool: ...
    def has_delete_permission(self, request, obj = ...) -> bool: ...

class WarningConstraintProductInline(Any):
    extra: int
    model: Any
