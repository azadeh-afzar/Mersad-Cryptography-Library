# Stubs for mersad.test.classical.test_atbash_cipher (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

# Python Standard Library
import unittest
from typing import Any

class TestShiftCipher(unittest.TestCase):
    base_path: Any = ...
    agent: Any = ...
    plain_text: Any = ...
    sh0_s0: Any = ...
    sh1_s0: Any = ...
    custom_alphabet: Any = ...
    def setUp(self) -> None: ...
    def test_encrypt_without_shuffle(self) -> None: ...
    def test_encrypt_with_shuffle_without_seed(self) -> None: ...
    def test_encrypt_with_custom_alphabet(self) -> None: ...
    def test_decryption_without_shuffle(self) -> None: ...
    def test_decrypt_with_shuffle_without_seed(self) -> None: ...
    def test_decrypt_with_custom_alphabet(self) -> None: ...
    def test_terminal_application(self) -> None: ...
