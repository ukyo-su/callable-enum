from dataclasses import dataclass
from enum import auto, Enum
from types import MethodType
from typing import Callable


@dataclass
class _Wrapper:
    body: Callable
    value: any


def register(value=None):
    if value is None:
        value = auto()

    def decorator(body):
        return _Wrapper(body, value)

    return decorator


class CallableEnum(Enum):
    def __new__(cls, v):
        ret = object.__new__(cls)
        if isinstance(v, _Wrapper):
            ret._value_ = v.value
            ret._func = MethodType(v.body, ret)
        else:
            raise TypeError("a CallableEnum member without method definition")
        return ret

    def __call__(self, *args, **kwargs):
        return self._func(*args, **kwargs)
