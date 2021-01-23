# Copyright (C) Dnspython Contributors, see LICENSE for text of ISC license

from typing import Any, Final

from dns.exception import DNSException

NONE: Final[int] = ...
A: Final[int] = ...
NS: Final[int] = ...
MD: Final[int] = ...
MF: Final[int] = ...
CNAME: Final[int] = ...
SOA: Final[int] = ...
MB: Final[int] = ...
MG: Final[int] = ...
MR: Final[int] = ...
NULL: Final[int] = ...
WKS: Final[int] = ...
PTR: Final[int] = ...
HINFO: Final[int] = ...
MINFO: Final[int] = ...
MX: Final[int] = ...
TXT: Final[int] = ...
RP: Final[int] = ...
AFSDB: Final[int] = ...
X25: Final[int] = ...
ISDN: Final[int] = ...
RT: Final[int] = ...
NSAP: Final[int] = ...
NSAP_PTR: Final[int] = ...
SIG: Final[int] = ...
KEY: Final[int] = ...
PX: Final[int] = ...
GPOS: Final[int] = ...
AAAA: Final[int] = ...
LOC: Final[int] = ...
NXT: Final[int] = ...
SRV: Final[int] = ...
NAPTR: Final[int] = ...
KX: Final[int] = ...
CERT: Final[int] = ...
A6: Final[int] = ...
DNAME: Final[int] = ...
OPT: Final[int] = ...
APL: Final[int] = ...
DS: Final[int] = ...
SSHFP: Final[int] = ...
IPSECKEY: Final[int] = ...
RRSIG: Final[int] = ...
NSEC: Final[int] = ...
DNSKEY: Final[int] = ...
DHCID: Final[int] = ...
NSEC3: Final[int] = ...
NSEC3PARAM: Final[int] = ...
TLSA: Final[int] = ...
HIP: Final[int] = ...
CDS: Final[int] = ...
CDNSKEY: Final[int] = ...
CSYNC: Final[int] = ...
SPF: Final[int] = ...
UNSPEC: Final[int] = ...
EUI48: Final[int] = ...
EUI64: Final[int] = ...
TKEY: Final[int] = ...
TSIG: Final[int] = ...
IXFR: Final[int] = ...
AXFR: Final[int] = ...
MAILB: Final[int] = ...
MAILA: Final[int] = ...
ANY: Final[int] = ...
URI: Final[int] = ...
CAA: Final[int] = ...
AVC: Final[int] = ...
TA: Final[int] = ...
DLV: Final[int] = ...

class UnknownRdatatype(DNSException): ...

def from_text(text: Any) -> int: ...
def to_text(value: Any) -> str: ...
def is_metatype(rdtype: Any) -> bool: ...
def is_singleton(rdtype: Any) -> bool: ...
