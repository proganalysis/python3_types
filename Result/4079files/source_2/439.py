from django.contrib.contenttypes.models import ContentType

from configfactory import constants
from configfactory.models import LogEntry
from configfactory.utils.db import model_to_dict


def log_action(action=None, action_type=None, user=None, instance=None, object_repr=None, old_data=None, new_data=None):

    if not action and not action_type:
        raise ValueError('action or action_type must be defined.')

    if old_data is None:
        old_data = {}

    if new_data is None:
        new_data = {}

    content_type = None
    object_id = None

    if instance:
        content_type = ContentType.objects.get_for_model(instance)
        object_id = instance.pk
        if object_repr is None:
            object_repr = str(instance)

    log = LogEntry()
    log.action = action
    log.action_type = action_type
    log.user = user
    log.content_type = content_type
    log.object_id = object_id
    log.object_repr = object_repr
    log.old_data = old_data
    log.new_data = new_data
    log.save()

    return log


def log_create_object(instance, user=None, fields=None, exclude=None):

    return log_action(
        action_type=constants.LOG_ACTION_TYPE_CREATE,
        instance=instance,
        new_data=model_to_dict(
            instance=instance,
            fields=fields,
            exclude=exclude
        ),
        user=user,
    )


def log_update_object(instance, old_data=None, new_data=None, user=None, object_repr=None, fields=None, exclude=None):

    if new_data is None:
        new_data = model_to_dict(
            instance=instance,
            fields=fields,
            exclude=exclude
        )

    return log_action(
        action_type=constants.LOG_ACTION_TYPE_UPDATE,
        user=user,
        instance=instance,
        object_repr=object_repr,
        old_data=old_data,
        new_data=new_data,
    )


def log_delete_object(instance, user=None, fields=None, exclude=None):

    return log_action(
        action_type=constants.LOG_ACTION_TYPE_DELETE,
        user=user,
        instance=instance,
        old_data=model_to_dict(
            instance=instance,
            fields=fields,
            exclude=exclude
        )
    )
