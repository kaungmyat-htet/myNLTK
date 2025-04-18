#-*- coding:utf-8 -*-

import unittest

from mynltk.tokenize import (
    syllable_tokenize
)

class TestTokenizePackage(unittest.TestCase):
    def setUp(self) -> None:
        self.text_1 = "ကျွန်တော်စာလုပ်နေပါသည်။"
        self.text_2 = "ကျွန်တော့်နာမည်ကမောင်မောင်ဖြစ်ပါသည်။"
        self.tokenized_words = ["ကျွန်တော်", "စာ", "လုပ်", "နေ", "ပါ", "သည်", "။"]

    def test_syllable_tokenize(self):
        self.assertEqual(syllable_tokenize(None), [])
        self.assertIsInstance(syllable_tokenize(self.text_1), list)
        self.assertEqual(syllable_tokenize(self.text_1), ["ကျွန်", "တော်", "စာ", "လုပ်", "နေ", "ပါ", "သည်", "။"])
        self.assertEqual(syllable_tokenize(self.text_2), ["ကျွန်", "တော့်", "နာ", "မည်", "က", "မောင်", "မောင်", "ဖြစ်", "ပါ", "သည်", "။"])