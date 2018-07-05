# -*- coding: utf-8 -*-
import unittest
import zg2uni

class TestZG2UNI(unittest.TestCase):
    def test_article_one(self):
        zawgyi = u'''ကခဂဃငစဆဇညဋဌဍဏတထဒဓနပဖဗဘမယရလ၀သဟဠအ'''
        unicode = u'''ကခဂဃငစဆဇညဋဌဍဏတထဒဓနပဖဗဘမယရလ၀သဟဠအ'''
        result = zg2uni.convert(zawgyi)
        self.assertEqual(unicode, result, "Failed converting Article One")

    def test_article_two(self):
        zawgyi = u'''သီဟိုဠ္မွ ဉာဏ္ႀကီးရွင္သည္ အာယုဝၯနေဆးၫႊန္းစာကို ဇလြန္ေဈးေဘးဗာဒံပင္ထက္ အဓိ႒ာန္လ်က္ ဂဃနဏဖတ္ခဲ့သည္။'''
        unicode = u'''သီဟိုဠ်မှ ဉာဏ်ကြီးရှင်သည် အာယုဝဍ္ဎနဆေးညွှန်းစာကို ဇလွန်ဈေးဘေးဗာဒံပင်ထက် အဓိဋ္ဌာန်လျက် ဂဃနဏဖတ်ခဲ့သည်။'''
        result = zg2uni.convert(zawgyi)
        self.assertEqual(unicode, result, "Failed converting Article One")

if __name__ == "__main__":
    unittest.main()
