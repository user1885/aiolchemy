"""
Session context decoratos for aiogram
"""
from .base import acontextual
from ..core import async_session


class asessional:
    """
    Decorator for coroutines with sqlalchemy async sessions
    """
    def __call__(self, coro):
        inner = self._get_inner()
        return inner(coro)

    def __new__(cls, func=None):
        instance = super().__new__(cls)
        if func is None:
            return instance
        return instance(func)

    @classmethod
    def _get_inner(cls):
        return acontextual(
            ctx=async_session,
            name="session",
        )
