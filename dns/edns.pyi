# Copyright (C) Dnspython Contributors, see LICENSE for text of ISC license

from typing import Any, Type

NSID: int

class Option:
    otype: Any = ...
    def __init__(self, otype: Any) -> None: ...
    def to_wire(self, file: Any) -> None: ...
    @classmethod
    def from_wire(cls, otype: Any, wire: bytes, current: int, olen: int) -> Option: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...

class GenericOption(Option):
    data: Any = ...
    def __init__(self, otype: Any, data: Any) -> None: ...
    def to_wire(self, file: Any) -> None: ...
    @classmethod
    def from_wire(cls, otype: Any, wire: Any, current: Any, olen: Any) -> GenericOption: ...

def get_option_class(otype: Any) -> Type[Option]: ...

def option_from_wire(otype: Any, wire: Any, current: Any, olen: Any) -> Option: ...
