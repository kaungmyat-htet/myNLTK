# -*- coding: utf-8 -*-
"""
function of tokenizers
"""
import re
from typing import List

def syllable_tokenize(
        text: str
) -> List[str]:
    """
    Syllable tokenizer

    Tokenizes text into inseperable units of Myanmar syllables.

    Args:
        text (str): Input string to tokenize.
    
    Returns:
        List[str]: A list of syllables.

    Example::

        from mynltk.tokenize import syllable_tokenize

        text = "ကျွန်တော့်နာမည်ကမောင်မောင်ဖြစ်ပါသည်။"

        syllable_tokenize(text)
        # output: ["ကျွန်", "တော့်", "နာ", "မည်", "က", "မောင်", "မောင်", "ဖြစ်", "ပါ", "သည်", "။"]
    """
    if not text or not isinstance(text, str):
        return []
    
    # remove whitespace between words
    text = text.replace(" ", "")

    segments = []

    from mynltk.tokenize.syllable_segment import segment

    segments = segment(text)

    return segments