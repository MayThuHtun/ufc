import unittest
import zg2uni

class TestZG2UNI(unittest.TestCase):
    def test_article_one(self):
        zawgyi = u'ျဖစ္ေစ တိုင္းျပည္ အခ်င္းခ်င္း ဆိုင္ရာျဖစ္ေစ၊ အဆင့္အတန္း တစ္ခုခုကို အေျချပဳ၍ ေသာ္လည္းေကာင္း၊ ေဒသနယ္ေျမတစ္ခုသည္ အခ်ဳပ္အျခာ အာဏာပိုင္ လြတ္လပ္သည့္'
        unicode = u'ဖြစ်စေ တိုင်းပြည် အချင်းချင်း ဆိုင်ရာဖြစ်စေ၊ အဆင့်အတန်း တစ်ခုခုကို အခြေပြု၍ သော်လည်းကောင်း၊ ဒေသနယ်မြေတစ်ခုသည် အချုပ်အခြာ အာဏာပိုင် လွတ်လပ်သည့်'
        result = zg2uni.convert(zawgyi)
        self.assertEqual(unicode, result, "Failed converting Article One")



if __name__ == "__main__":
    unittest.main()
