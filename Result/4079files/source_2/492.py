#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Entry point for the pulsar-queue application.

Contains the pulsar-queue object instantiation and configuration.
"""

import json
# Python-native imports
import logging.config
from typing import Type, Union

# Third-party imports
import pykka

# App imports
from pyCrow.crowlib import Action

L = logging.getLogger(__name__)
L.debug(f'Loaded module: {__name__}.')


# helper method
def actor_get_or_create(actor: Union[Type[pykka.Actor], str], index: int = 0, *args,
                        **kwargs) -> pykka.ActorRef:
    """Convenience wrapper to either retrieve existing actors from registry or to create new actor
    references that are subsequently started and registered.

    When ``actor`` is provided as string, make sure to specify the path like so:

        ``actor_get_or_create(actor='pyCrow.crowlib.RestActor', ...)``

    or

        ``actor_get_or_create(actor='crowlib.RestActor', ...)``

    :param Union[Type[pykka.Actor], str] actor: The actor class type or the actor class name.
    :param int index: In case the actor exists in the registry, the actor at this position will be
                      returned.

    :exception NameError: Raised when there is no such Actor with the given name.
    :exception TypeError: Raised when an actor class name is given which cannot be resolved to a
                          class type.
    """
    if isinstance(actor, str):
        try:
            if '.' in actor:
                _module, _actor = tuple(actor.rsplit('.', 1))
                try:
                    return pykka.ActorRegistry.get_by_class_name(actor_class_name=_actor)[index]
                except IndexError:
                    pass  # log this?

                import importlib
                _module = importlib.import_module(
                    _module if _module.startswith('pyCrow.') else f'pyCrow.{_module}')
            else:
                try:
                    return pykka.ActorRegistry.get_by_class_name(actor_class_name=actor)[index]
                except IndexError:
                    pass  # log this?

                _actor = actor
                import sys
                _module = sys.modules[__name__]

            actor = getattr(_module, _actor)
        except AttributeError:
            error_msg = f'{actor} does not exist.'
            L.error(error_msg)
            raise NameError(error_msg)

    if not (isinstance(actor, type) or issubclass(actor, pykka.Actor)):
        error_msg = f'{actor} is not a valid actor class.'
        L.error(error_msg)
        raise TypeError(error_msg)

    try:
        return pykka.ActorRegistry.get_by_class(actor_class=actor)[index]
    except IndexError:
        pass  # log this?

    try:
        ref: pykka.ActorRef = actor.start(*args, **kwargs)
        assert ref is not None
    except AssertionError:
        L.error(msg='Unable to start the REST Actor.')
    except pykka.ActorDeadError as ade:
        L.warning(msg=f'Message received for dead REST Actor: {ade}')
    else:
        return ref


class AppActor(pykka.ThreadingActor):
    """ Build Pykka App actor parent to all other actors.
    """

    def __init__(self):
        super(AppActor, self).__init__()
        # todo set default configuration
        self._config = {}

    def on_start(self):
        # load config for this application
        self._refresh_config()

        # create RestActor per se to receive external commands
        actor_get_or_create(actor='crowlib.RestActor', config=self._config.get('server', {}))

    def on_stop(self):
        L.debug('AppActor is stopped.')

    def on_failure(self, exception_type, exception_value, traceback):
        L.error(f'AppActor failed: {exception_type} {exception_value} {traceback}')

    def on_receive(self, msg: dict):
        L.info(msg=f'AppActor received message: {msg}')
        # process msg and interact with sub-actors accordingly

        _cmd = msg.get('cmd', '').lower()
        if _cmd == Action.CONFIG_REFRESH.get('cmd'):
            self._refresh_config()
        elif _cmd == Action.CONFIG_GET.get('cmd'):
            return self._config
        elif _cmd == Action.AUDIO_RECORD.get('cmd'):
            ref = actor_get_or_create(
                'audiolib.AudioActor', chunk_size=1024, config=self._config.get('recorder', {}))
            ref.tell(message=msg)
            # vr: Recorder = Recorder()
            # vr.record_to_file('./resources/demo.wav', seconds=_duration)

        elif _cmd == Action.MODEL_TRAIN.get('cmd'):
            ref = actor_get_or_create(
                'crowlib.ExperimentActor',
                config=self._config.get('model_train', {}).get('experiment', {}))
            ref.tell(message=msg)

        elif _cmd in [Action.SERVER_START.get('cmd'), Action.SERVER_RESTART.get('cmd'),
                      Action.SERVER_STOP.get('cmd')]:
            pykka.ActorRegistry.broadcast(message=msg, target_class='RestActor')

        else:
            # default: do nothing but log this event
            L.info(msg=f'Received message {msg} which cannot be processed.')

    def _refresh_config(self, config_file='config.json'):
        with open(config_file, 'r') as json_data_file:
            self._config = json.load(json_data_file)
            # todo validate config... at some point
            L.info(f'Refreshing configuration:\n{self._config}')
