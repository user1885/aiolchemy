"""
Base context decorators for aiogram
"""
from functools import wraps
from dataclasses import dataclass
from inspect import getfullargspec
from typing import (
    ContextManager,
    AsyncContextManager,
)


@dataclass(slots=True)
class contextual:
    ctx: ContextManager
    args: tuple = ()
    name: str = "ctx"

    def __call__(self, func):
        @wraps(func)
        def inner(*args, **kwargs):
            with self.ctx(*self.args) as context:
                kwargs[self.name] = context
                return func(*args, **kwargs)
        return inner


@dataclass(slots=True)
class acontextual:
    """
    Async version of contextual
    """
    ctx: AsyncContextManager
    args: tuple = ()
    name: str = "ctx"

    def __call__(self, coro):
        # later we need arg names of coro
        coro_spec = getfullargspec(coro)
        wraps(coro)
        async def inner(*args, **kwargs):
            # aiogram register handlers and put specified kwargs
            # in callback function
            # that's why we need to filter kwargs to ensure
            # callback coro takes specified by aiogram kwargs
            intersection = set(kwargs) & set(coro_spec.args)
            # filter kwargs
            new_kwargs = {kw: kwargs[kw] for kw in intersection}
            async with self.ctx(*self.args) as acontext:
                # context object for wrapped coro
                new_kwargs[self.name] = acontext
                return await coro(*args, **new_kwargs)
        return inner
