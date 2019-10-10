# Stubs for mersad.classical.affine_cipher (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

# Python Standard Library
from typing import Union

# Mersad Library
from mersad.util.base_class import MersadClassicalBase

def main() -> None: ...

class AffineCipher(MersadClassicalBase):
    def _config_subroutines(self, **kwargs: Union[int, str, bool]) -> None: ...
    @staticmethod
    def _translator(text: str, **kwargs: Union[int, str, bool]) -> str: ...

def affine_cipher_translator(text: str, **kwargs: Union[int, str, bool]) -> str: ...
def _check_keys(key_a: int, key_b: int, sequence_length: int) -> None: ...
