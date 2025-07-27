
import datetime
import functools

from smart_plant.storage.models import Actions
from smart_plant.db import session_factory


def log_action(func):
    @functools.wraps(func)
    def inner(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        with session_factory() as session:
            record = Actions(
                actor=self.__class__.__name__,
                action=func.__name__,
                dt=datetime.datetime.now(datetime.timezone.utc)
            )
            session.add(record)
            session.commit()
        return result
    return inner