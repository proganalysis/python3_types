# (generated with --quick)

from typing import Any

BaseMixin: Any
ReprMixin: Any
RoleMixin: Any
UniqueConstraint: Any
UserMixin: Any
db: Any

class Permission(Any, Any, Any):
    description: Any
    name: Any
    users: Any

class Role(Any, Any, Any, Any):
    description: Any
    name: Any
    users: Any

class User(Any, Any, Any, Any):
    active: Any
    confirmed_at: Any
    current_login_at: Any
    current_login_ip: Any
    email: Any
    last_login_at: Any
    last_login_ip: Any
    login_count: Any
    password: Any
    permissions: Any
    roles: Any
    user_profile: Any
    username: Any
    def has_permission(self, permission) -> bool: ...

class UserPermission(Any, Any):
    permission: Any
    permission_id: Any
    user: Any
    user_id: Any

class UserProfile(Any, Any):
    dob: Any
    first_name: Any
    gender: Any
    last_name: Any
    profile_picture: Any
    user: Any
    user_id: Any

class UserRole(Any, Any):
    role: Any
    role_id: Any
    user: Any
    user_id: Any
