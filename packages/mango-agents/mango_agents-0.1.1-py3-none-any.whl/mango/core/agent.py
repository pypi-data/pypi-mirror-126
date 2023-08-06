"""
This module implements the base class for agents (:class:`Agent`).

Every agent must live in a container. Containers are responsible for making
 connections to other agents.
"""
import asyncio
import logging
from abc import ABC, abstractmethod
from typing import Any, Dict
# import mango.core.container  # might lead to cycle imports, we have to rethink this
from ..util.scheduling import ScheduledTask, Scheduler
# import mango.core.container

logger = logging.getLogger(__name__)


class Agent(ABC):
    """Base class for all agents."""

    def __init__(self, container):
        """Initialize an agent and register it with its container
        :param container: The container that the agent lives in. Must be a Container
        """
        # if not isinstance(container, mango.core.container.Container):
        #     raise TypeError('"container" must be a "Container" instance but '
        #                     'is {}'.format(container))
        aid = container._register_agent(self)
        self._container = container
        self._aid = aid
        self.inbox = asyncio.Queue()
        self._check_inbox_task = asyncio.create_task(self._check_inbox())
        self._check_inbox_task.add_done_callback(self.raise_exceptions)
        self.stopped = asyncio.Future()
        self._scheduled_tasks = []
        self._scheduler = Scheduler()
        logger.info('Agent starts running')

    def schedule_task(self, task: ScheduledTask, src = None):
        """Schedule a task with asyncio. When the task is finished, if finite, its automatically
        removed afterwards. For scheduling options see the subclasses of ScheduledTask.

        :param task: task to be scheduled
        :param src: object, which represents the source of the task (for example the object in which the task got created)
        """
        self._scheduler.schedule_task(task, src=src)

    async def tasks_complete(self, timeout=1):
        """Wait for all scheduled tasks to complete using a timeout.

        :param timeout: waiting timeout. Defaults to 1.
        """
        await self._scheduler.tasks_complete(timeout=timeout)

    def raise_exceptions(self, fut: asyncio.Future):
        """
        Inline function used as a callback to raise exceptions
        :param fut: The Future object of the task
        """
        if fut.exception() is not None:
            logger.error('Caught the following exception in _check_inbox: %s', fut.exception())
            raise fut.exception()

    @property
    def aid(self):
        """Return the agents ID"""
        return self._aid

    async def _check_inbox(self):
        """Task for waiting on new message in the inbox"""

        logger.debug('Start waiting for msgs')
        while True:
            # run in infinite loop until it is cancelled from outside
            msg = await self.inbox.get()
            logger.debug(f'Received message;{str(msg)}')

            # msgs should be tuples of (priority, content)
            priority, content, meta = msg
            meta['priority'] = priority
            self.handle_msg(content=content, meta=meta)

            # signal to the Queue that the message is handled
            self.inbox.task_done()

    @abstractmethod
    def handle_msg(self, content, meta: Dict[str, Any]):
        """

        Has to be implemented by the user.
        This method is called when a message is received.
        The message with the lowest priority number
        in the que is handled first.
        This is a blocking call, if non-blocking message handling is desired,
        one should call asyncio.create_task() in order to handle more than
        one message at a time
        :param content: The deserialized message object
        :param meta: Meta details of the msg. In case of mqtt this dict
        includes at least the field 'topic'
        """
        raise NotImplementedError

    async def shutdown(self):
        """Shutdown all tasks that are running
         and deregister from the container"""

        if not self.stopped.done():
            self.stopped.set_result(True)
        if self._container.running:
            self._container.deregister_agent(self._aid)
        try:
            # Shutdown reactive inbox task
            self._check_inbox_task.remove_done_callback(self.raise_exceptions)
            self._check_inbox_task.cancel()
            await self._check_inbox_task

            await self._scheduler.stop()
        except asyncio.CancelledError:
            pass
        finally:
            logger.info('Shutdown successful')
