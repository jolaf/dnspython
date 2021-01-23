# Copyright (C) Dnspython Contributors, see LICENSE for text of ISC license

from typing import Any, Callable, BinaryIO, Dict, Generator, Iterable, Iterator, Optional, TextIO, Tuple, Union

from dns.exception import DNSException
from dns.message import Message
from dns.name import Name
from dns.node import Node
from dns.rdata import Rdata
from dns.rdataclass import IN
from dns.rdataset import Rdataset
from dns.rdatatype import ANY, NONE
from dns.rrset import RRset

class BadZone(DNSException): ...
class NoSOA(BadZone): ...
class NoNS(BadZone): ...
class UnknownOrigin(BadZone): ...

class Zone:
    def __getitem__(self, key : str) -> Node:
        ...
    def __init__(self, origin : Union[str,Name], rdclass : int = IN, relativize : bool = True) -> None:
        self.nodes : Dict[str,Node]
        self.origin = origin
    def values(self) -> Iterable[Node]:
        ...
    def iterate_rdatas(self, rdtype : Union[int,str] = ANY, covers : Union[int,str,None] = None) -> Iterable[Tuple[Name, int, Rdata]]:
        ...
    def __iter__(self) -> Iterator[str]:
        ...
    def get_node(self, name : Union[Name,str], create: bool = False) -> Optional[Node]:
        ...
    def find_rrset(self, name : Union[str,Name], rdtype : Union[int,str], covers: Union[str, int] = NONE) -> RRset:
        ...
    def find_rdataset(self, name : Union[str,Name], rdtype : Union[str,int], covers: Union[str, int] = NONE,
                      create: bool = False) -> Rdataset:
        ...
    def get_rdataset(self, name : Union[str,Name], rdtype : Union[str,int], covers: Union[str, int] = NONE, create: bool = False) -> Optional[Rdataset]:
        ...
    def get_rrset(self, name : Union[str,Name], rdtype : Union[str,int], covers: Union[str, int] = NONE) -> Optional[RRset]:
        ...
    def replace_rdataset(self, name : Union[str,Name], replacement : Rdataset) -> None:
        ...
    def delete_rdataset(self, name : Union[str,Name], rdtype : Union[str,int], covers: Union[str, int] = NONE) -> None:
        ...
    def iterate_rdatasets(self, rdtype : Union[str,int] = ANY,
                          covers : Union[str,int] = NONE) -> Iterator[Tuple[Name, Rdataset]]:
        ...
    def to_file(self, f : Union[TextIO, BinaryIO, str], sorted: bool = True, relativize: bool = True, nl : Optional[bytes] = None) -> None:
        ...
    def to_text(self, sorted: bool = True, relativize: bool = True, nl : Optional[bytes] = None) -> bytes:
        ...

def from_xfr(xfr : Generator[Any,Any,Message], zone_factory : Callable[..., Zone] = Zone, relativize: bool = True, check_origin: bool = True) -> Zone:
    ...

def from_text(text : str, origin : Optional[Union[str,Name]] = None, rdclass : int = IN,
              relativize: bool = True, zone_factory : Callable[...,Zone] = Zone, filename : Optional[str] = None,
              allow_include: bool = False, check_origin: bool = True) -> Zone:
    ...

def from_file(f: Any, origin : Optional[Union[str,Name]] = None, rdclass: int = IN,
              relativize: bool = True, zone_factory : Callable[..., Zone] = Zone, filename : Optional[str] = None,
              allow_include: bool = True, check_origin: bool = True) -> Zone:
    ...
