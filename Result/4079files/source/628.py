from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django_extensions.db.models import TimeStampedModel


class Resource(TimeStampedModel):
    """
    Describes a group of URL addressable resources
    """
    year = models.IntegerField(verbose_name=_('Year'), null=True, blank=True)
    name = JSONField(verbose_name=_('name'), null=True, blank=True)
    description = JSONField(null=True, blank=True, verbose_name=_('description'))
    pubtype = models.ForeignKey('PublicationType', verbose_name=_("Type"))

    author = models.ManyToManyField('Author', blank=True)
    organization = models.ManyToManyField('Organization', blank=True)
    tag = models.ManyToManyField('Tag', blank=True)

    cover = models.ImageField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)


class Link(TimeStampedModel):
    """
    Link to an internal or external resource
    """
    cover = models.ImageField(max_length=200, blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    resource = models.ForeignKey('Resource')
    url = models.URLField(blank=True, null=True)
    file = models.FileField(max_length=200, blank=True, null=True)


class PublicationType(TimeStampedModel):
    """
    Describes an object based on its type (eg newsletter, report...)
    """

    # def __str__(self):
    #     return u'{}'.format(self.name)

    id = models.TextField(primary_key=True)
    name = JSONField()
    description = JSONField(null=True, blank=True)

    class Meta:
        verbose_name_plural = _("Publication Types")
        ordering = ('name',)


class Author(TimeStampedModel):
    name = JSONField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name.get('name', '')

    class Meta:
        verbose_name_plural = _("Authors")
        ordering = ('name',)


class Organization(TimeStampedModel):
    name = models.TextField()
    acronyms = JSONField(null=True, blank=True)
    description = JSONField(null=True, blank=True)
    contact = JSONField(null=True, blank=True)
    type = models.ForeignKey('OrganizationType', verbose_name=_('Organization Type'), null=True, blank=True)


class Tag(TimeStampedModel):
    name = JSONField()
    description = JSONField(null=True, blank=True)


class OrganizationType(TimeStampedModel):
    id = models.TextField(primary_key=True)
    name = JSONField()
    description = JSONField(null=True, blank=True)
