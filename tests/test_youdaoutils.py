import json

from dict2anki.extractors.youdaoutils.wordgetter import get_text
from unittest import TestCase


class TestWordGetter(TestCase):
    def test_get_word(self):
        text = get_text('hello')
        print(json.dumps(text, indent=2, ensure_ascii=False))
