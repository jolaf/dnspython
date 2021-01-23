# Copyright (C) Dnspython Contributors, see LICENSE for text of ISC license

from typing import Any, Iterator, Optional, Tuple

from dns.exception import DNSException
from dns.name import Name

EOF: int
EOL: int
WHITESPACE: int
IDENTIFIER: int
QUOTED_STRING: int
COMMENT: int
DELIMITER: int

class UngetBufferFull(DNSException): ...

class Token:
    ttype: Any = ...
    value: Any = ...
    has_escape: Any = ...
    def __init__(self, ttype: Any, value: str = ..., has_escape: bool = ...) -> None: ...
    def is_eof(self) -> bool: ...
    def is_eol(self) -> bool: ...
    def is_whitespace(self) -> bool: ...
    def is_identifier(self) -> bool: ...
    def is_quoted_string(self) -> bool: ...
    def is_comment(self) -> bool: ...
    def is_delimiter(self) -> bool: ...
    def is_eol_or_eof(self) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def unescape(self) -> Token: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[Tuple[Any, str]]: ...
    def __getitem__(self, i: Any) -> Any: ...

class Tokenizer:
    file: Any = ...
    ungotten_char: Any = ...
    ungotten_token: Any = ...
    multiline: int = ...
    quoting: bool = ...
    eof: bool = ...
    delimiters: Any = ...
    line_number: int = ...
    filename: Any = ...
    def __init__(self, f: Any = ..., filename: Optional[Any] = ...) -> None: ...
    def where(self) -> Tuple[str, int]: ...
    def skip_whitespace(self) -> int: ...
    def get(self, want_leading: bool = ..., want_comment: bool = ...) -> Token: ...
    def unget(self, token: Any) -> None: ...
    def next(self) -> Tuple[int, str]: ...
    def __next__(self) -> Tuple[int, str]: ...
    def __iter__(self) -> Tokenizer: ...
    def get_int(self) -> int: ...
    def get_uint8(self) -> int: ...
    def get_uint16(self) -> int: ...
    def get_uint32(self) -> int: ...
    def get_string(self, origin: Optional[Any] = ...) -> str: ...
    def get_identifier(self, origin: Optional[Any] = ...) -> str: ...
    def get_name(self, origin: Optional[Any] = ...) -> Name: ...
    def get_eol(self) -> str: ...
    def get_ttl(self) -> int: ...
