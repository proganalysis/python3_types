"""
The application controller that provides the key application functionality. The controller provides an interface
 tasks are run on a background thread.
"""

import logging
import unittest
import threading
from queue import Queue

from method_proxy import MethodWrapperProxy

logger = logging.getLogger(__name__)


def command(method):
    """Decorator to enqueue method calls in Actor instances."""
    def enqueue_call(self, *args, **kwargs):
        args = list(args)
        args.insert(0, self)
        self.enqueue(method, args, kwargs)
    return enqueue_call


class Actor(threading.Thread):
    """A simple implementation of the active object design pattern."""

    def __init__(self):
        threading.Thread.__init__(self)
        self._commands = Queue()
        self._must_stop = False
        self.exception_handler = None

    def enqueue(self, method, args=None, kwargs=None):
        self._commands.put((method, args, kwargs))

    @command
    def stop(self):
        self._must_stop = True

    def run(self):
        while not self._must_stop:
            try:
                cmd, args, kwargs = self._commands.get()
                cmd(*args if args is not None else [], **kwargs if kwargs is not None else {})
            except Exception as e:
                if self.exception_handler:
                    self.exception_handler(cmd, args, kwargs, e)


class ActorTest(unittest.TestCase):

    def raise_hell(self, e):
        raise e

    def play_nice(self):
        self.nice = True

    def produce_exception(self, handler=None):
        a = Actor()
        a.exception_handler = handler
        a.start()
        a.enqueue(self.raise_hell, [ValueError()])
        self.nice = False
        a.enqueue(self.play_nice)
        a.stop()
        a.join(1)
        self.assertEqual(a.is_alive(), False)
        self.assertEqual(self.nice, True)

    def test_actor_continues_running_on_exception_without_handler(self):
        self.produce_exception()

    def test_actor_continues_running_on_exception_with_handler(self):
        test = self
        def handler(method, args, kwargs, ex):
            test.assertEqual(type(ex), type(ValueError()))
        self.produce_exception(handler)


class ActiveObjectProxy(MethodWrapperProxy):
    """
    Proxies method calls on the target instance by dispatching them to a queue for execution by an active object.
    """
    def __init__(self, actor, delegate):
        super().__init__(delegate, ActiveObjectProxy.enqueue)
        self.actor = actor

    @staticmethod
    def enqueue(proxy, target, name, method):
        def invoke_later(self, *args, **kwargs):
            proxy.actor.enqueue(method, args, kwargs)
        return invoke_later


class DoitBackgroundTask:
    def doit(self):
        self.called = True

    def test_thread(self, t, test):
        self.doit()
        test.assertEqual(t, threading.current_thread())


class ActiveObjectProxyTest(unittest.TestCase):
    def test_actor_thread_terminates(self):
        a = Actor()
        a.start()
        a.stop()
        a.join(timeout=1)
        self.assertEqual(a.is_alive(), False)

    def test_proxy_methods_execute(self):
        actor = Actor()
        actor.start()
        task = DoitBackgroundTask()
        proxy = ActiveObjectProxy(actor, task)
        proxy.doit()
        actor.stop()
        actor.join(timeout=1)
        self.assertEqual(task.called, True)

    def test_proxy_methods_execute_on_thread(self):
        actor = Actor()
        actor.start()
        task = DoitBackgroundTask()
        proxy = ActiveObjectProxy(actor, task)
        proxy.test_thread(actor, self)
        actor.stop()
        actor.join(timeout=1)
        self.assertEqual(task.called, True)

