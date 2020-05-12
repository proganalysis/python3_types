from bitpoll.poll.models import Poll as Poll
from django.contrib.auth.models import AbstractUser as AbstractUser
from typing import Any

register: Any

def poll_can_edit(poll: Poll, user: AbstractUser) -> bool: ...
def poll_is_owner(poll: Poll, user: AbstractUser) -> bool: ...
