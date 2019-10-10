# Stubs for mersad.util.base_class (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

# Python Standard Library
import argparse
from typing import Any
from typing import List
from typing import Optional
from typing import Union

class MersadClassicalBase:
    _defaults: Any = ...
    configuration: Any = ...
    def __init__(self, **kwargs: Union[int, str, bool]) -> None: ...
    def __str__(self) -> str: ...
    def encrypt(self, plain_text: str, key: Optional[int]=..., replace_key: bool=...) -> str: ...
    def decrypt(self, cipher_text: str, key: Optional[int]=..., replace_key: bool=...) -> str: ...
    def config(self, **kwargs: Union[int, str, bool]) -> None: ...
    def reset(self) -> None: ...
    def show_key(self) -> int: ...
    def _process(self, text: str, key: Optional[int], replace_key: bool, decrypt: bool) -> str: ...
    def _config_subroutines(self, **kwargs: Union[int, str, bool]) -> None: ...
    @staticmethod
    def _translator(text: str, **kwargs: Union[int, str, bool]) -> str: ...

class MainFunctionClassical:
    args: Any = ...
    agent_class: Any = ...
    description: Any = ...
    epilog: Any = ...
    def __init__(self, args: List[Any], agent_class: Any, description: str, epilog: str) -> None: ...
    def process(self) -> None: ...
    def parse_args(self) -> argparse.Namespace: ...
    @staticmethod
    def _argparse_parent() -> argparse.ArgumentParser: ...
