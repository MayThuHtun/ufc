# -*- coding: utf-8 -*-
import unittest
import uni2win


class TestZG2UNI(unittest.TestCase):

    def test_article_consonant(self):
        win = u''''''
        unicode = u''''''
        result = uni2win.convert(unicode)
        self.assertEqual(win, result, "Failed converting Article One")


if __name__ == "__main__":
    unittest.main()
