from django.conf import settings as settings
from typing import Any

pytestmark: Any

def test_user_get_absolute_url(user: settings.AUTH_USER_MODEL) -> Any: ...
