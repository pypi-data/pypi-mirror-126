from __future__ import annotations

__all__ = [
    'coroutine', 'lock_seed', 'summary', 'trace', 'trace_module', 'whereami'
]

import functools
import gc
import inspect
import os
import random
import threading
import types
from collections import Counter
from collections.abc import Callable, Generator, Hashable, Iterator
from contextlib import suppress
from itertools import islice
from types import FrameType
from typing import TypeVar, cast

import numpy as np
import wrapt

from ._import_hook import register_post_import_hook

_F = TypeVar('_F', bound=Callable[..., Generator])


def _get_module(frame: FrameType) -> str:
    if (module := inspect.getmodule(frame)) and module.__spec__:
        return module.__spec__.name
    return '__main__'


def _get_function(frame: FrameType) -> str:
    function = frame.f_code.co_name
    function = next(
        (f.__qualname__
         for f in gc.get_referrers(frame.f_code) if inspect.isfunction(f)),
        function)
    return '' if function == '<module>' else function


def _stack(frame: FrameType | None) -> Iterator[str]:
    while frame:
        yield f'{_get_module(frame)}:{_get_function(frame)}:{frame.f_lineno}'
        if frame.f_code.co_name == '<module>':  # Stop on module-level scope
            return
        frame = frame.f_back


def stack(skip: int = 0, limit: int | None = None) -> Iterator[str]:
    """Returns iterator of FrameInfos, stopping on module-level scope"""
    frame = inspect.currentframe()
    calls = _stack(frame)
    calls = islice(calls, skip + 1, None)  # Skip 'skip' outerless frames
    if not limit:
        return calls
    return islice(calls, limit)  # Keep at most `limit` outer frames


def whereami(skip: int = 0, limit: int | None = None) -> str:
    calls = stack(skip + 1, limit)
    return ' -> '.join(reversed([*calls]))


@wrapt.decorator
def trace(fn, _, args, kwargs):
    print(
        f'<({whereami(3)})> : {fn.__module__ or ""}.{fn.__qualname__}',
        flush=True)
    return fn(*args, **kwargs)


def _set_trace(obj, seen=None, prefix=None, module=None):
    # TODO: rewrite using unittest.mock
    if isinstance(obj, types.ModuleType):
        if seen is None:
            seen = set()
            prefix = obj.__name__
        if not obj.__name__.startswith(prefix) or obj.__name__ in seen:
            return
        seen.add(obj.__name__)
        for name in dir(obj):
            _set_trace(
                getattr(obj, name), module=obj, seen=seen, prefix=prefix)

    if not callable(obj):
        return

    if not hasattr(obj, '__dict__'):
        setattr(module, obj.__qualname__, trace(obj))
        print(f'wraps "{module.__name__}:{obj.__qualname__}"')
        return

    for name in obj.__dict__:
        with suppress(AttributeError, TypeError):
            member = getattr(obj, name)
            if not callable(member):
                continue
            decorated = trace(member)

            for m in (decorated, member, obj):
                with suppress(AttributeError):
                    decorated.__module__ = m.__module__
                    break
            else:
                decorated.__module__ = getattr(module, '__name__', '')
            setattr(obj, name, decorated)
            print(f'wraps "{module.__name__}:{obj.__qualname__}.{name}"')


def trace_module(name):
    """Enables call logging for each callable inside module name"""
    register_post_import_hook(_set_trace, name)


# ---------------------------------------------------------------------------


@wrapt.decorator
def threadsafe_coroutine(fn, _, args, kwargs):
    coro = fn(*args, **kwargs)
    coro.send(None)
    lock = threading.RLock()

    class Synchronized(wrapt.ObjectProxy):
        def send(self, item):
            with lock:
                return self.__wrapped__.send(item)

        def __next__(self):
            return self.send(None)

    return Synchronized(coro)


@threadsafe_coroutine
def summary() -> Generator[None, Hashable, None]:
    state: Counter[Hashable] = Counter()
    while True:
        key = yield
        if key is None:
            state.clear()
            continue
        state[key] += 1
        print(dict(state), flush=True, end='\r')


def coroutine(fn: _F) -> _F:
    def wrapper(*args, **kwargs):
        coro = fn(*args, **kwargs)
        coro.send(None)
        return coro

    return cast(_F, functools.update_wrapper(wrapper, fn))


# ---------------------------------------------------------------------------


def lock_seed(seed: int) -> None:
    """Set seed for all modules: random/numpy/torch"""
    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)

    def _torch_seed(torch):
        import torch
        import torch.backends.cudnn

        torch.manual_seed(seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False

    register_post_import_hook(_torch_seed, 'torch')
