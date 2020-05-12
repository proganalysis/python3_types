from functools import partial
from flowlight.tasks.task import _Task

class Node:
    """Abstract representation of `Machine` and `Group`.

    :param name: the unique name of a `Node`.

    Usage::

        >>> machine = Machine('host1')
        >>> isinstance(machine, Node)
        True
        >>> group = Group([Machine('host1'), Machine('host2')])
        >>> isinstance(group, Node)
        True
    """
    def __init__(self, name):
        self.name = name

    def run(self, cmd):
        raise NotImplementedError

    def enable_connection(self):
        raise NotImplementedError

    def run_task(node, task, *args, **kwargs):
        if not isinstance(task, _Task):
            raise Exception('Need a task')
        return task.__call__(node, *args, **kwargs)

    def run_tasks(self, tasks, *args, **kwargs):
        if not isinstance(tasks, list):
            tasks = [tasks]
        return list(map(partial(self.run_task, *args, **kwargs), tasks))
