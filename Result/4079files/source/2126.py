# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
import re

from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from game.contrib.calculate import calculate_score, score_gain
from game.interactive_shocks.models import InteractiveShocksRound
from game.interactive_static.models import InteractiveStaticRound
from game.round.models import Round


def validate_comma_separated_integer_list(val, sep=',', code='invalid'):
    regex = re.compile('^[0-2](?:%(sep)s[0-2])*\Z' % {'sep': re.escape(sep),
                                                      })
    if regex.fullmatch(val):
        return val
    raise ValidationError('List supplied is not correct', code=code)


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    game_type = models.CharField(_('User Type'), max_length=10)
    avatar = models.URLField(null=True)
    user_level = models.CharField(max_length=10, null=True, blank=True)  # level should be either 'e', 'm', or 'h'
    kicked = models.BooleanField(default=False)
    prompted = models.SmallIntegerField(default=0)
    exited = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    @property
    def get_avatar(self):
        return 'images/avatars/{}'.format(self.avatar)

    def __get_user_cls(self):
        if self.game_type == 'control':
            cls = Round
        elif self.game_type == 'dynamic':
            cls = InteractiveShocksRound
        elif self.game_type == 'static':
            cls = InteractiveStaticRound
        else:
            raise NotImplemented('Not Implemented')
        return cls

    @property
    def get_score(self):
        played_rounds = self.__get_user_cls().objects.filter(user=self).order_by('round_order')
        return calculate_score(played_rounds)

    @property
    def get_score_and_gain(self):
        played_rounds = self.__get_user_cls().objects.filter(user=self).order_by('round_order')
        if self.game_type == 'dynamic' or self.game_type == 'static':
            count = played_rounds.count() - 1
            played_rounds = played_rounds[:count]
        return score_gain(played_rounds)

    @property
    def level(self):
        return self.user_level

    @level.setter
    def level(self, val):
        if val in ['e', 'm', 'h']:
            self.user_level = val
            self.save()
        else:
            raise TypeError('level must be e, m, or h')


class UserTypes(models.Model):
    types = models.CharField(max_length=1000, validators=[validate_comma_separated_integer_list])

    def __str__(self):
        return 'vector: {}'.format(self.types)

    class Meta:
        verbose_name_plural = 'UserTypes'
