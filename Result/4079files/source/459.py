from django.db import models
from django.utils.translation import ugettext_lazy as _

from configfactory.models.managers import EnvironmentManager
from configfactory.shortcuts import is_base_environment


class Environment(models.Model):

    name = models.CharField(max_length=128, verbose_name=_('name'))

    alias = models.SlugField(unique=True, verbose_name=_('alias'))

    order = models.SmallIntegerField(verbose_name=_('order'), default=0)

    fallback = models.ForeignKey(
        to='self',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='environments',
        verbose_name=_('fallback environment')
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_('active'),
        help_text=_(
            'Designates whether this environment should be treated as active. '
            'Unselect this instead of deleting environments.'
        ),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('creation datetime')
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('modification datetime')
    )

    objects = EnvironmentManager()

    class Meta:
        verbose_name = _('environment')
        verbose_name_plural = _('environments')
        ordering = ('order', 'name',)

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.alias,

    @property
    def is_base(self):
        return is_base_environment(self.alias)
