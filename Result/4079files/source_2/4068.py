from django.urls import reverse

from falmer.auth.models import MagicLinkToken


def create_magic_link_for_user(user, next_view):
    magic = MagicLinkToken.create_for_user(user)

    return reverse('auth-magic_link', kwargs={'token': magic.token})
