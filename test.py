import unittest
import zg2uni

class TestZG2UNI(unittest,TestCase):
    def test-article-one(self):
        zawgyi = u'A'
        unicode = u'A'
        result = zg2uni.convert(zawgyi)
        self.assertEqual(unicode, result, "Failed converting Article One")



if __name__ == "__main__":
    unittest.main()
