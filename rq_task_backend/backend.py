from django.tasks.backends import BaseTaskBackend

from redis import Redis
from rq import Queue


class RQTaskBackend(BaseTaskBackend):

    def __init__(self, *args, **kwargs):
        super(RQTaskBackend, self).__init__(*args, **kwargs)

        # TODO: Add connection string handling
        self._queue = Queue(connection=Redis())
        self._results = {}
        self._next_id = 1

    def _get_next_id(self):
        next_id = self._next_id
        self._next_id = next_id + 1
        return next_id

    def delay(self, task, *args, **kwargs):
        result_id = self._get_next_id()
        job = self._queue.enqueue(task.run, *args)
        self._results[result_id] = job

        return result_id
