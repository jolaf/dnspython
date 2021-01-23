# Copyright (C) Dnspython Contributors, see LICENSE for text of ISC license

from hmac import HMAC
from typing import Any, Optional, Tuple

from dns.exception import DNSException
from dns.name import Name

class BadTime(DNSException): ...
class BadSignature(DNSException): ...
class PeerError(DNSException): ...
class PeerBadKey(PeerError): ...
class PeerBadSignature(PeerError): ...
class PeerBadTime(PeerError): ...
class PeerBadTruncation(PeerError): ...

HMAC_MD5: Any
HMAC_SHA1: Any
HMAC_SHA224: Any
HMAC_SHA256: Any
HMAC_SHA384: Any
HMAC_SHA512: Any
default_algorithm = HMAC_MD5
BADSIG: int
BADKEY: int
BADTIME: int
BADTRUNC: int

def sign(wire: Any, keyname: Any, secret: Any, time: Any, fudge: Any, original_id: Any, error: Any, other_data: Any, request_mac: Any, ctx: Optional[Any] = ..., multi: bool = ..., first: bool = ..., algorithm: Any = ...) -> HMAC: ...
def hmac_md5(wire: Any, keyname: Any, secret: Any, time: Any, fudge: Any, original_id: Any, error: Any, other_data: Any, request_mac: Any, ctx: Optional[Any] = ..., multi: bool = ..., first: bool = ..., algorithm: Any = ...) -> HMAC: ...
def validate(wire: Any, keyname: Any, secret: Any, now: Any, request_mac: Any, tsig_start: Any, tsig_rdata: Any, tsig_rdlen: Any, ctx: Optional[Any] = ..., multi: bool = ..., first: bool = ...) -> HMAC: ...
def get_algorithm(algorithm: Any) -> Name: ...
def get_algorithm_and_mac(wire: Any, tsig_rdata: Any, tsig_rdlen: Any) -> Tuple[Name, bytes]: ...
