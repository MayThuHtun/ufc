import unittest
import uni2win


class TESTUNI2WIN(unittest.TestCase):
    def test_article_one(self):
        unicode = u'''အပိုဒ် ၁
        လူတိုင်းသည် တူညီ လွတ်လပ်သော ဂုဏ်သိက္ခာဖြင့် လည်းကောင်း၊ တူညီလွတ်လပ်သော အခွင့်အရေးများဖြင့် လည်းကောင်း၊ မွေးဖွားလာသူများ ဖြစ်သည်။ 
        ထိုသူတို့၌ ပိုင်းခြား ဝေဖန်တတ်သော ဉာဏ်နှင့် ကျင့်ဝတ် သိတတ်သော စိတ်တို့ရှိကြ၍ ထိုသူတို့သည် အချင်းချင်း မေတ္တာထား၍ ဆက်ဆံကျင့်သုံးသင့်၏။'''
        win = u'''tydk'f 1
        vlwdkif;onf wlnD vGwfvyfaom *kPfodu©mjzihf vnf;aumif;? wlnDvGwfvyfaom tcGihfta&;rsm;jzihf vnf;aumif;? arG;zGm;vmolrsm; jzpfonf/ 
        xdkolwdkYü ydkif;jcm; a0zEefwwfaom ÓPfESihf usihf0wf odwwfaom pdwfwdkY&SdMuí xdkolwdkYonf tcsif;csif; arwÅmxm;í qufqHusihfokH;oihf\/'''
        result = uni2win.convert(unicode)
        self.assertEqual(win, result, "Failed to Convert Article One")

        def test_article_two(self):
            unicode = u'''အပိုဒ် ၂
            လူတိုင်းသည် လူ့အခွင့် အရေး ကြေညာစာတမ်းတွင် ဖော်ပြထားသည့် အခွင့်အရေး အားလုံး၊ လွတ်လပ်ခွင့် အားလုံးတို့ကို ပိုင်ဆိုင် ခံစားခွင့်ရှိသည်။ 
            လူမျိုးနွယ်အားဖြင့် ဖြစ်စေ၊ အသားအရောင်အားဖြင့် ဖြစ်စေ၊ ကျား၊ မ၊ သဘာဝအားဖြင့် ဖြစ်စေ၊ ဘာသာစကားအားဖြင့် ဖြစ်စေ၊ ကိုးကွယ်သည့် ဘာသာအားဖြင့် ဖြစ်စေ၊ 
            နိုင်ငံရေးယူဆချက်၊ သို့တည်းမဟုတ် အခြားယူဆချက်အားဖြင့် ဖြစ်စေ၊ နိုင်ငံနှင့် ဆိုင်သော၊ သို့တည်းမဟုတ် လူမှုအဆင့်အတန်းနှင့် ဆိုင်သော ဇစ်မြစ် အားဖြင့်ဖြစ်စေ၊ 
            ပစ္စည်း ဥစ္စာ ဂုဏ်အားဖြင့် ဖြစ်စေ၊ မျိုးရိုးဇာတိအားဖြင့် ဖြစ်စေ၊ အခြား အဆင့်အတန်း အားဖြင့် ဖြစ်စေ ခွဲခြားခြင်းမရှိစေရ။ ထို့ပြင် လူတစ်ဦး တစ်ယောက် 
            နေထိုင်ရာ နိုင်ငံ၏ သို့တည်းမဟုတ် နယ်မြေဒေသ၏ နိုင်ငံရေးဆိုင်ရာ ဖြစ်စေ စီရင်ပိုင်ခွင့်ဆိုင်ရာ ဖြစ်စေ တိုင်းပြည် အချင်းချင်း ဆိုင်ရာဖြစ်စေ၊ အဆင့်အတန်း တစ်ခုခုကို 
            အခြေပြု၍ သော်လည်းကောင်း၊ ဒေသနယ်မြေတစ်ခုသည် အချုပ်အခြာ အာဏာပိုင် လွတ်လပ်သည့် နယ်မြေ၊ သို့တည်းမဟုတ် ကုလသမဂ္ဂ ထိန်းသိမ်း စောင့်ရှောက် ထားရသည့် 
            နယ်မြေ၊ သို့တည်းမဟုတ် ကိုယ်ပိုင် အုပ်ချုပ်ခွင့် အာဏာတို့ တစိတ်တဒေသလောက်သာ ရရှိသည့် နယ်မြေ စသဖြင့် ယင်းသို့ သော နယ်မြေများ ဖြစ်သည် 
            ဟူသော အကြောင်းကို အထောက်အထား ပြု၍ သော်လည်းကောင်း ခွဲခြားခြင်း လုံးဝ မရှိစေရ။'''
            win = u'''tydk'f 2
            vlwdkif;onf vlYtcGihf ta&; aMunmpmwrf;wGif azmfjyxm;onhf tcGihfta&; tm;vkH;? vGwfvyfcGihf tm;vkH;wdkYudk ydkifqdkif cHpm;cGihf&Sdonf/ 
            vlrsdK;EG,ftm;jzihf jzpfap? tom;ta&miftm;jzihf jzpfap? usm;? r? obm0tm;jzihf jzpfap? bmompum;tm;jzihf jzpfap? udk;uG,fonhf bmomtm;jzihf jzpfap? 
            EdkifiHa&;,lqcsuf? odkYwnf;r[kwf tjcm;,lqcsuftm;jzihf jzpfap? EdkifiHESihf qdkifaom? odkYwnf;r[kwf vlrItqihftwef;ESihf qdkifaom Zpfjrpf tm;jzihfjzpfap? 
            ypönf; Opöm *kPftm;jzihf jzpfap? rsdK;½dk;Zmwdtm;jzihf jzpfap? tjcm; tqihftwef; tm;jzihf jzpfap cGJjcm;jcif;r&Sdap&/ xdkYjyif vlwpfOD; wpfa,muf 
            aexdkif&m EdkifiH\ odkYwnf;r[kwf e,fajra'o\ EdkifiHa&;qdkif&m jzpfap pD&ifydkifcGihfqdkif&m jzpfap wdkif;jynf tcsif;csif; qdkif&mjzpfap? tqihftwef; wpfckckudk 
            tajcûyí aomfvnf;aumif;? a'oe,fajrwpfckonf tcsKyftjcm tmPmydkif vGwfvyfonhf e,fajr? odkYwnf;r[kwf ukvor*¾ xdef;odrf; apmihfa&Smuf xm;&onhf 
            e,fajr? odkYwnf;r[kwf udk,fydkif tkyfcsKyfcGihf tmPmwdkY wpdwfwa'oavmufom &&Sdonhf e,fajr pojzihf ,if;odkY aom e,fajrrsm; jzpfonf 
            [laom taMumif;udk taxmuftxm; ûyí aomfvnf;aumif; cGJjcm;jcif; vkH;0 r&Sdap&/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Two")

        def test_article_three(self):
            unicode = u'''အပိုဒ် ၃
             လူတိုင်း၌ အသက်ရှင်ရန် လွတ်လပ်မှုခွင့်နှင့် လုံခြုံစိတ်ချခွင့် ရှိသည်။'''
            win = u'''tydk'f 3
             vlwdkif;ü touf&Sif&ef vGwfvyfrIcGihfESihf vkHûcHpdwfcscGihf &Sdonf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Three")

        def test_article_four(self):
            unicode = u'''အပိုဒ် ၄
            မည်သူကိုမျှ ကျေးကျွန်အဖြစ်၊ သို့တည်းမဟုတ် အစေအပါးအဖြစ်၊ နိုင်ထက်စီးနင်း စေခိုင်းခြင်း မပြုရ၊ လူကို ကျေးကျွန်သဖွယ် အဓမ္မ စေခိုင်းခြင်း၊ 
            အရောင်းအဝယ် ပြုခြင်းနှင့် ထိုသဘော သက်ရောက်သော လုပ်ငန်းဟူသမျှကို ပိတ်ပင် တားမြစ် ရမည်။'''
            win = u'''tydk'f 4
            rnfoludkrQ aus;uReftjzpf? odkYwnf;r[kwf taptyg;tjzpf? EdkifxufpD;eif; apcdkif;jcif; rûy&? vludk aus;uRefozG,f t"r® apcdkif;jcif;? 
            ta&mif;t0,f ûyjcif;ESihf xdkoabm oufa&mufaom vkyfief;[lorQudk ydwfyif wm;jrpf &rnf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Four")

        def test_article_five(self):
            unicode = u'''အပိုဒ် ၅
            မည်သူကိုမျှ ညှဉ်းပန်း နှိပ်စက်ခြင်း၊ သို့တည်းမဟုတ် ရက်စက်ကြမ်းကြုတ်စွာ လူမဆန်စွာ ဂုဏ်ငယ်စေသော ဆက်ဆံမှု မပြုရ၊ သို့တည်းမဟုတ် အပြစ်ဒဏ် ပေးခြင်းမပြုရ။'''
            win = u'''tydk'f 5
            rnfoludkrQ n§Of;yef; ESdyfpufjcif;? odkYwnf;r[kwf &ufpufMurf;êuwfpGm vlrqefpGm *kPfi,fapaom qufqHrI rûy&? odkYwnf;r[kwf tjypf'Pf ay;jcif;rûy&/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Five")

        def test_article_six(self):
            unicode = u'''အပိုဒ် ၆
            လူတိုင်းတွင် ဥပဒေအရာ၌ လူပုဂ္ဂိုလ်တစ်ဦး အဖြစ်ဖြင့် အရာခပ်သိမ်းတွင် အသိအမှတ် ပြုခြင်းကို ခံယူပိုင်ခွင့်ရှိသည်။'''
            win = u'''tydk'f 6
            vlwdkif;wGif Oya't&mü vlyk*¾dKvfwpfOD; tjzpfjzihf t&mcyfodrf;wGif todtrSwf ûyjcif;udk cH,lydkifcGihf&Sdonf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Six")

        def test_article_seven(self):
            unicode = u'''အပိုဒ် ၇
            လူအားလုံးတို့သည် ဥပဒေအရာ၌ တူညီကြသည့်အပြင်၊ ဥပဒေ၏ အကာအကွယ်ကို ခြားနားခြင်း မခံရစေဘဲ တူညီစွာ ခံစားပိုင်ခွင့်ရှိသည်။ 
            ဤကြေညာ စာတမ်းပါ သဘောတရားများကို ဖီဆန်၍ ခွဲခြားခြင်းမှ လည်းကောင်း၊ ထိုသို့ခွဲခြားခြင်းကို လှုံ့ဆော်ခြင်းမှ လည်းကောင်း၊ 
            ကင်းလွတ် စေရန် အကာအကွယ်ကို တူညီစွာ ခံစားပိုင်ခွင့် ရှိသည်။'''
            win = u'''tydk'f 7
            vltm;vkH;wdkYonf Oya't&mü wlnDMuonhftjyif? Oya'\ tumtuG,fudk jcm;em;jcif; rcH&apbJ wlnDpGm cHpm;ydkifcGihf&Sdonf/ 
            þaMunm pmwrf;yg oabmw&m;rsm;udk zDqefí cGJjcm;jcif;rS vnf;aumif;? xdkodkYcGJjcm;jcif;udk vIHYaqmfjcif;rS vnf;aumif;? 
            uif;vGwf ap&ef tumtuG,fudk wlnDpGm cHpm;ydkifcGihf &Sdonf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Seven")

        def test_article_eight(self):
            unicode = u'''အပိုဒ် ၈
             ဖွဲ့စည်းပုံ အခြေခံဥပဒေက သော်လည်းကောင်း အခြား ဥပဒေက သော်လည်းကောင်း လူတိုင်းအတွက် ပေးထားသည့် အခြေခံ အခွင့်အရေး များသည် 
             ချိုးဖောက် ဖျက်ဆီးခြင်းခံခဲ့ရလျှင် ထိုသို့ ချိုးဖောက်ဖျက်ဆီး သော ပြုလုပ်မှုကြောင့် ဖြစ်ပေါ်လာသော နစ်နာချက် အတွက် ထိုသူသည် နိုင်ငံဆိုင်ရာ 
             အာဏာပိုင်တရားရုံးတွင် ထိရောက်စွာ သက်သာခွင့် ရှိနိုင်စေရမည်။'''
            win = u'''tydk'f 8
             zGJUpnf;ykH tajccHOya'u aomfvnf;aumif; tjcm; Oya'u aomfvnf;aumif; vlwdkif;twGuf ay;xm;onhf tajccH tcGihfta&; rsm;onf 
             csdK;azmuf zsufqD;jcif;cHcJh&vQif xdkodkY csdK;azmufzsufqD; aom ûyvkyfrIaMumihf jzpfay:vmaom epfemcsuf twGuf xdkolonf EdkifiHqdkif&m 
             tmPmydkifw&m;½kH;wGif xda&mufpGm oufomcGihf &SdEdkifap&rnf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Eight")

        def test_article_nine(self):
            unicode = u'''အပိုဒ် ၉
             မည်သူမျှ ဥပဒေအရ မဟုတ်သော ဖမ်းဆီးခြင်းကို ဖြစ်စေ၊ ချုပ်နှောင်ခြင်းကို ဖြစ်စေ၊ ပြည်နှင်ခြင်းကိုဖြစ်စေ မခံစေရ။'''
            win = u'''tydk'f 9
             rnfolrQ Oya't& r[kwfaom zrf;qD;jcif;udk jzpfap? csKyfaESmifjcif;udk jzpfap? jynfESifjcif;udkjzpfap rcHap&/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Nine")

        def test_article_ten(self):
            unicode = u'''အပိုဒ် ၁ဝ
             အခွင့်အရေးများနှင့် တာဝန် ဝတ္တရားများကို အဆုံးအဖြတ်ခံရာတွင် လည်းကောင်း၊ ပြစ်မှုကြောင့် တရားစွဲဆို စီရင် ဆုံးဖြတ်ခံရာတွင် လည်းကောင်း၊ 
             လူတိုင်းသည် လွတ်လပ်၍ ဘက်မလိုက်သော တရားရုံးတော်၏ လူအများ ရှေ့မှောက်တွင် မျှတစွာ ကြားနာစစ်ဆေးခြင်းကို တူညီစွာ ခံစား ပိုင်ခွင့်ရှိသည်။'''
            win = u'''tydk'f 10
             tcGihfta&;rsm;ESihf wm0ef 0wÅ&m;rsm;udk tqkH;tjzwfcH&mwGif vnf;aumif;? jypfrIaMumihf w&m;pGJqdk pD&if qkH;jzwfcH&mwGif vnf;aumif;? 
             vlwdkif;onf vGwfvyfí bufrvdkufaom w&m;½kH;awmf\ vltrsm; a&SUarSmufwGif rQwpGm Mum;emppfaq;jcif;udk wlnDpGm cHpm; ydkifcGihf&Sdonf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Ten")

        def test_article_eleven(self):
            unicode = u'''အပိုဒ် ၁၁
            လူအများ ရှေ့မှောက်၌ ဥပဒေအတိုင်း စစ်ဆေး၍ ပြစ်မှုကျူးလွန်သည်ဟု ထင်ရှား စီရင်ခြင်းခံရသည့် အချိန်အထိ ပြစ်မှုနှင့် 
            တရားစွဲဆိုခြင်း ခံရသူတိုင်းသည် အပြစ်မဲ့သူဟူ၍ ယူဆ ခြင်းခံထိုက်သည့် အခွင့်အရေးရှိသည်။ ထိုအမှုကို ကြားနာစစ်ဆေးရာဝယ် 
            စွပ်စွဲခံရသည့် ပြစ်မှုအတွက် ခုခံချေပနိုင်ရန် လိုအပ်သော အခွင့်အရေးများကို ထိုသူအား ပေးပြီး ဖြစ်စေရမည်။
            လူတစ်ဦးတစ်ယောက်အား နိုင်ငံဥပဒေအရဖြစ်စေ၊ အပြည်ပြည်ဆိုင်ရာ ဥပဒေအရ ဖြစ်စေ၊ ပြစ်မှုမမြောက်သော လုပ်ရပ် သို့မဟုတ် ပျက်ကွက်မှုအရ 
            ဆွဲဆိုပြစ်ပေးခြင်း မပြုရ။ ထို့အပြင် ပြစ်မှုကျူးလွန်စဉ်အခါက ထိုက်သင့်စေနိုင်သော အပြစ်ဒဏ်ထက်ပိုမိုကြီးလေးသော အပြစ်ဒဏ်ကို ထိုက်သင့်ခြင်းမရှိစေရ။'''
            win = u'''tydk'f 11
            vltrsm; a&SUarSmufü Oya'twdkif; ppfaq;í jypfrIusL;vGefonf[k xif&Sm; pD&ifjcif;cH&onhf tcsdeftxd jypfrIESihf 
            w&m;pGJqdkjcif; cH&olwdkif;onf tjypfrJhol[lí ,lq jcif;cHxdkufonhf tcGihfta&;&Sdonf/ xdktrIudk Mum;emppfaq;&m0,f 
            pGyfpGJcH&onhf jypfrItwGuf ckcHacsyEdkif&ef vdktyfaom tcGihfta&;rsm;udk xdkoltm; ay;NyD; jzpfap&rnf/
            vlwpfOD;wpfa,muftm; EdkifiHOya't&jzpfap? tjynfjynfqdkif&m Oya't& jzpfap? jypfrIrajrmufaom vkyf&yf odkYr[kwf ysufuGufrIt& 
            qGJqdkjypfay;jcif; rûy&/ xdkYtjyif jypfrIusL;vGefpOftcgu xdkufoihfapEdkifaom tjypf'PfxufydkrdkBuD;av;aom tjypf'Pfudk xdkufoihfjcif;r&Sdap&/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Eleven")

        def test_article_twelve(self):
            unicode = u'''အပိုဒ် ၁၂
            မည်သူမျှ မိမိသဘောအတိုင်း အေးချမ်းလွတ်လပ်စွာ နေထိုင်ခြင်းကို သော်လည်းကောင်း၊ မိမိ၏ မိသားစုကို သော်လည်းကောင်း၊ 
            မိမိ၏ နေအိမ် အသိုက်အဝန်းကို သော်လည်းကောင်း၊ စာပေးစာယူကို သော်လည်းကောင်း၊ ဥပဒေအရ မဟုတ်သော ဝင်ရောက် စွက်ဖက်ခြင်း မခံစေရ။ 
            ထို့ပြင် မိမိ၏ဂုဏ်သိက္ခာ ကိုလည်း အထက်ပါ အတိုင်း ပုတ်ခတ်ခြင်း မခံစေရ။ လူတိုင်းတွင် ထိုသို့ ဝင်ရောက်စွက်ဖက်ခြင်းမှ သော်လည်းကောင်း 
            ပုတ်ခတ်ခြင်းမှ သော်လည်းကောင်း ဥပဒေအရ ကာကွယ် ပိုင်ခွင့်ရှိသည်။'''
            win = u'''tydk'f 12
            rnfolrQ rdrdoabmtwdkif; at;csrf;vGwfvyfpGm aexdkifjcif;udk aomfvnf;aumif;? rdrd\ rdom;pkudk aomfvnf;aumif;? 
            rdrd\ aetdrf todkuft0ef;udk aomfvnf;aumif;? pmay;pm,ludk aomfvnf;aumif;? Oya't& r[kwfaom 0ifa&muf pGufzufjcif; rcHap&/ 
            xdkYjyif rdrd\*kPfodu©m udkvnf; txufyg twdkif; ykwfcwfjcif; rcHap&/ vlwdkif;wGif xdkodkY 0ifa&mufpGufzufjcif;rS aomfvnf;aumif; 
            ykwfcwfjcif;rS aomfvnf;aumif; Oya't& umuG,f ydkifcGihf&Sdonf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Twelve")

        def test_article_thirteen(self):
            unicode = u'''အပိုဒ် ၁၃
            လူတိုင်းတွင် မိမိ၏နိုင်ငံ နယ်နိမိတ် အတွင်း၌ လွတ်လပ်စွာ သွားလာ ရွှေ့ပြောင်း နိုင်ခွင့်၊ နေထိုင်ခွင့်ရှိသည်။
            လူတိုင်းတွင် မိမိနေထိုင်ရာ တိုင်းပြည်မှ လည်းကောင်း၊ အခြားတိုင်းပြည်မှလည်းကောင်း ထွက်ခွာ သွားပိုင်ခွင့်ရှိသည့်အပြင်၊မိမိ၏ 
            တိုင်းပြည်သို့ ပြန်လာ ပိုင်ခွင့်လည်းရှိသည်။'''
            win = u'''tydk'f 13
            vlwdkif;wGif rdrd\EdkifiH e,fedrdwf twGif;ü vGwfvyfpGm oGm;vm a½TUajymif; EdkifcGihf? aexdkifcGihf&Sdonf/
            vlwdkif;wGif rdrdaexdkif&m wdkif;jynfrS vnf;aumif;? tjcm;wdkif;jynfrSvnf;aumif; xGufcGm oGm;ydkifcGihf&Sdonhftjyif?rdrd\ 
            wdkif;jynfodkY jyefvm ydkifcGihfvnf;&Sdonf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Thirteen")

        def test_article_fourteen(self):
            unicode = u'''အပိုဒ် ၁၄
            လူတိုင်းသည် ညှဉ်းပန်း နှိပ်စက် ခံနေရခြင်းမှ လွတ်ကင်းရန် အခြားတိုင်းပြည် များ၌ အေးချမ်းစွာ ခိုလှုံနေနိုင်ခွင့်ရှိသည်။
            နိုင်ငံရေးနှင့် မပတ်သက်သည့် ပြစ်မှုများမှ သော်လည်းကောင်း၊ ကုလသမဂ္ဂ၏ ရည်ရွက်ချက်နှင့် သဘောတရား မှုများကို 
            ဖီဆန်သော အမှုများမှ သော်လညး်ကောင်း၊ အမှန် ပေါ်ပေါက် လာသော ပြစ်မှုကြောင့် တရားစွဲဆိုခြင်း ခံရသည့် အမှုအခင်းများတွင် 
            အထက်ပါ အခွင့်အရေးကို အသုံးမပြုနိုင်စေရ။'''
            win = u'''tydk'f 14
            vlwdkif;onf n§Of;yef; ESdyfpuf cHae&jcif;rS vGwfuif;&ef tjcm;wdkif;jynf rsm;ü at;csrf;pGm cdkvIHaeEdkifcGihf&Sdonf/
            EdkifiHa&;ESihf rywfoufonhf jypfrIrsm;rS aomfvnf;aumif;? ukvor*¾\ &nf½GufcsufESihf oabmw&m; rIrsm;udk 
            zDqefaom trIrsm;rS aomfvn;faumif;? trSef ay:ayguf vmaom jypfrIaMumihf w&m;pGJqdkjcif; cH&onhf trItcif;rsm;wGif 
            txufyg tcGihfta&;udk tokH;rûyEdkifap&/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Fourteen")

        def test_article_fifteen(self):
            unicode = u'''အပိုဒ် ၁၅
            လူတိုင်းသည်၊ နိုင်ငံ တစ်နိုင်ငံ၏ နိုင်ငံသားအဖြစ် ခံယူခွင့်ရှိသည်။
            ဥပဒေအရ မဟုတ်လျှင် မည်သူမျှ မိမိ၏ နိုင်ငံသားအဖြစ်ကို စွန့်လွှတ်ခြင်း မခံစေရ၊ နိုင်ငံသားအဖြစ် ပြောင်းလဲနိုင်သော
            အခွင့်အရေးကို လည်း ငြင်းပယ်ခြင်း မခံစေရ။'''
            win = u'''tydk'f 15
            vlwdkif;onf? EdkifiH wpfEdkifiH\ EdkifiHom;tjzpf cH,lcGihf&Sdonf/
            Oya't& r[kwfvQif rnfolrQ rdrd\ EdkifiHom;tjzpfudk pGeYfvTwfjcif; rcHap&? EdkifiHom;tjzpf ajymif;vJEdkifaom
            tcGihfta&;udk vnf; jiif;y,fjcif; rcHap&/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Fifteen")

        def test_article_sixteen(self):
            unicode = u'''အပိုဒ် ၁၆
            အရွယ်ရောက် ပြီးသော ယောကျာ်း နှင့် မိန်းမတို့တွင် လူမျိုးကို သော်လည်းကောင်း၊ နိုင်ငံသား အဖြစ်ကို သော်လည်းကောင်း 
            ကိုးကွယ်သည့် ဘာသာကို သော်လည်းကောင်း၊ အကြောင်းပြု၍ ချုပ်ချယ် ကန့်သတ်ခြင်း မရှိဘဲ၊ ထိမ်းမြားနိုင်ခွင့် နှင့် မိသားစုထူထောင်နိုင်ခွင့်ရှိသည်။ 
            အဆိုပါ ယောကျာ်းနှင့် မိန်းမ တို့သည် လင်မယားအဖြစ် ပေါင်းသင်းနေစဉ် အချိန် အတွင်း၌ သော်လည်းကောင်း၊ အိမ်ထောင်ကို ဖျက်သိမ်း၍ 
            ကွာရှင်းကြသည့် အခါ၌လည်းကောင်း၊ လက်ထပ် ပေါင်းသင်း အိမ်ထောင်ပြုခြင်းနှင့် စပ်လျဉ်းသော တူညီသည့် အခွင့်အရေးများကို ရရှိထိုက်သည်။
            သတို့သား နှင့် သတို့သမီး နှစ်ဦးနှစ်ဘက်၏ လွတ်လပ်သော သဘောဆန္ဒရှိမှသာလျှင် ထိမ်းမြားခြင်းကို ပြုရမည်။
            မိသားစု တစ်ခုသည် လူ့အဖွဲ့အစည်း၏ သဘာ၀ကျသော အခြေခံအဖွဲ့တစ်ရပ်ဖြစ်သည်၊ ထိုမိသားစုသည် လူ့ အဖွဲ့အစည်းနှင့် 
            အစိုးရတို့၏ ကာကွယ်စောင့်ရှောက်ခြင်းကို ခံယူခွင့်ရှိသည်။'''
            win = u'''tydk'f 16
            t½G,fa&muf NyD;aom a,musmf; ESihf rdef;rwdkYwGif vlrsdK;udk aomfvnf;aumif;? EdkifiHom; tjzpfudk aomfvnf;aumif; 
            udk;uG,fonhf bmomudk aomfvnf;aumif;? taMumif;ûyí csKyfcs,f ueYfowfjcif; r&SdbJ? xdrf;jrm;EdkifcGihf ESihf rdom;pkxlaxmifEdkifcGihf&Sdonf/ 
            tqdkyg a,musmf;ESihf rdef;r wdkYonf vifr,m;tjzpf aygif;oif;aepOf tcsdef twGif;ü aomfvnf;aumif;? tdrfaxmifudk zsufodrf;í 
            uGm&Sif;Muonhf tcgüvnf;aumif;? vufxyf aygif;oif; tdrfaxmifûyjcif;ESihf pyfvsOf;aom wlnDonhf tcGihfta&;rsm;udk &&Sdxdkufonf/
            owdkYom; ESihf owdkYorD; ESpfOD;ESpfbuf\ vGwfvyfaom oabmqE´&SdrSomvQif xdrf;jrm;jcif;udk ûy&rnf/
            rdom;pk wpfckonf vlYtzGJUtpnf;\ obm0usaom tajccHtzGJUwpf&yfjzpfonf? xdkrdom;pkonf vlY tzGJUtpnf;ESihf 
            tpdk;&wdkY\ umuG,fapmihfa&Smufjcif;udk cH,lcGihf&Sdonf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Sixteen")

        def test_article_seventeen(self):
            unicode = u'''အပိုဒ် ၁၇
            လူတိုင်းတွင် မိမိ တစ်ဦးချင်းသော်လည်းကောင်း ၊ အခြားသူများနှင့် ဖက်စပ်၍ သော်လည်းကောင်း၊ ပစ္စည်းဥစ္စာ တို့ကို 
            ပိုင်ဆိုင်ရန် အခွင့်အရေးရှိရမည်။ ဥပဒေအရ မဟုတ်လျှင်၊ မည်သူမျှ မိမိ၏ပစ္စည်းဥစ္စာပိုင်ဆိုင်ခွင့်ကို စွန့်လွှတ်ခြင်း မခံစေရ။'''
            win = u'''tydk'f 17
            vlwdkif;wGif rdrd wpfOD;csif;aomfvnf;aumif; ? tjcm;olrsm;ESihf zufpyfí aomfvnf;aumif;? ypönf;Opöm wdkYudk 
            ydkifqdkif&ef tcGihfta&;&Sd&rnf/ Oya't& r[kwfvQif? rnfolrQ rdrd\ypönf;OpömydkifqdkifcGihfudk pGeYfvTwfjcif; rcHap&/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Seventeen")

        def test_article_eighteen(self):
            unicode = u'''အပိုဒ် ၁၈
            လူတိုင်းတွင် လွတ်လပ်စွာ တွေးခေါ် ကြံဆနိုင်ခွင့်၊ လွတ်လပ်စွာ ခံယူရပ်တည်နိုင်ခွင့် နှင့် လွတ်လပ်စွာ သက်ဝင် ကိုးကွယ်နိုင်ခွင့်ရှိသည်။ 
            အဆိုပါ အခွင့်အရေးများ၌ မိမိကိုးကွယ်သည့် ဘာသာကို သို့တည်းမဟုတ် သက်ဝင်ယုံကြည်ချက်ကို လွတ်လပ်စွာ ပြောင်းလဲနိုင်ခွင့် ပါဝင်သည့် အပြင် 
            မိမိ တစ်ယောက်ချင်းဖြစ်စေ၊ အခြားသူများနှင့် စုပေါင်း၍ဖြစ်စေ၊ ပြည်သူအများ ရှေ့မှောက်တွင် သော်လည်းကောင်း၊ ရှေ့မှောက်တွင် 
            မဟုတ်ဘဲ သော်လည်းကောင်း၊ မိမိ ကိုးကွယ်သော ဘာသာကို သို့တည်းမဟုတ် သက်ဝင် ယုံကြည်ချက်ကို လွတ်လပ် စွာ သင်ပြနိုင်ခွင့်၊ 
            ကျင့်သုံးနိုင်ခွင့်၊ ဝတ်ပြုကိုးကွယ်နိုင်ခွင့်နှင့် ဆောက်တည် နိုင်ခွင့်တို့လည်း ပါဝင်သည်။'''
            win = u'''tydk'f 18
            vlwdkif;wGif vGwfvyfpGm awG;ac: BuHqEdkifcGihf? vGwfvyfpGm cH,l&yfwnfEdkifcGihf ESihf vGwfvyfpGm ouf0if udk;uG,fEdkifcGihf&Sdonf/ 
            tqdkyg tcGihfta&;rsm;ü rdrdudk;uG,fonhf bmomudk odkYwnf;r[kwf ouf0if,kHMunfcsufudk vGwfvyfpGm ajymif;vJEdkifcGihf yg0ifonhf tjyif 
            rdrd wpfa,mufcsif;jzpfap? tjcm;olrsm;ESihf pkaygif;íjzpfap? jynfoltrsm; a&SUarSmufwGif aomfvnf;aumif;? a&SUarSmufwGif 
            r[kwfbJ aomfvnf;aumif;? rdrd udk;uG,faom bmomudk odkYwnf;r[kwf ouf0if ,kHMunfcsufudk vGwfvyf pGm oifjyEdkifcGihf? 
            usihfokH;EdkifcGihf? 0wfûyudk;uG,fEdkifcGihfESihf aqmufwnf EdkifcGihfwdkYvnf; yg0ifonf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Eighteen")

        def test_article_nineteen(self):
            unicode = u'''အပိုဒ် ၁၉
            လူတိုင်းတွင် လွတ်လပ်စွာ ထင်မြင် ယူဆနိုင်ခွင့်နှင့် လွတ်လပ်စွာ ဖွင့်ဟ ဖော်ပြနိုင်ခွင့်ရှိသည်။ အဆိုပါ အခွင့်အရေးများ၌ 
            အနှောင့် အယှက်မရှိဘဲ လွတ်လပ်စွာ ထင်မြင်ယူဆနိုင်ခွင့် ပါဝင် သည့်အပြင်၊ နိုင်ငံနယ်နိမိတ်များကို ထောက်ထားရန် မလိုဘဲ 
            သတင်းအကြောင်းအရာနှင့် သဘောတရားများကို တနည်းနည်း ဖြင့် လွတ်လပ်စွာ ရှာယူဆည်းပူးနိုင်ခွင့်၊ လက်ခံနိုင်ခွင့်နှင့် ဝေငှ ဖြန့်ချိခွင့်တို့လည်း ပါဝင်သည်။'''
            win = u'''tydk'f 19
            vlwdkif;wGif vGwfvyfpGm xifjrif ,lqEdkifcGihfESihf vGwfvyfpGm zGihf[ azmfjyEdkifcGihf&Sdonf/ tqdkyg tcGihfta&;rsm;ü 
            taESmihf t,Sufr&SdbJ vGwfvyfpGm xifjrif,lqEdkifcGihf yg0if onhftjyif? EdkifiHe,fedrdwfrsm;udk axmufxm;&ef rvdkbJ 
            owif;taMumif;t&mESihf oabmw&m;rsm;udk wenf;enf; jzihf vGwfvyfpGm &Sm,lqnf;yl;EdkifcGihf? vufcHEdkifcGihfESihf a0iS jzeYfcsdcGihfwdkYvnf; yg0ifonf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Nineteen")

        def test_article_twenty(self):
            unicode = u'''အပိုဒ် ၂ဝ
            လူတိုင်းတွင် လွတ်လပ် အေးချမ်းစွာ စုဝေးနိုင်ခွင့် နှင့် ဖွဲ့စည်းနိုင်ခွင့် တို့ ရှိသည်။
            မည်သူ့ကိုမျှ အဖွဲ့အစည်းတစ်ခုသို့ ဝင်စေရန် အတင်းအကျပ်မပြုရ။'''
            win = u'''tydk'f 20
            vlwdkif;wGif vGwfvyf at;csrf;pGm pka0;EdkifcGihf ESihf zGJUpnf;EdkifcGihf wdkY &Sdonf/
            rnfolYudkrQ tzGJUtpnf;wpfckodkY 0ifap&ef twif;tusyfrûy&/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Twenty")

        def test_article_twenty_one(self):
            unicode = u'''အပိုဒ် ၂၁
            လူတိုင်းတွင် မိမိနိုင်ငံ၏ အုပ်ချုပ်ရေး၌ ကိုယ်တိုင်ဖြစ်စေ၊ လွတ်လပ်စွာ ရွေးချယ်လိုက်သည့် ကိုယ်စားလှယ်များမှ တစ်ဆင့်ဖြစ်စေ ပါဝင် ဆောင်ရွက်နိုင်ခွင့် ရှိသည်။
            လူတိုင်းတွင် မိမိ၏နိုင်ငံရှိ ပြည်သူ့ ဝန်ထမ်းအဖွဲ့၌ ဝင်ရောက်နိုင်ရန် တူညီသည့် အခွင့် အရေးရှိသည်။
            ပြည်သူပြည်သားတို့၏ ဆန္ဒသည် အုပ်ချုပ် အာဏာ၏ အခြေခံဖြစ်ရမည်၊ အဆိုပါ ဆန္ဒကို အချိန်ကာလပိုင်းခြားလျက် စစ်မှန်သောရွေးကောက်ပွဲများဖြင့် 
            ထင်ရှားစေရမည်။ ရွေးကောက် ပွဲများတွင်လည်း လူတိုင်းအညီအမျှ ဆန္ဒမဲ ပေးနိုင်ခွင့် ရှိရမည့်အပြင် ၊ ထိုရွေးကောက်ပွဲများကို 
            လျှို့ဝှက် မဲပေး စနစ်ဖြင့် ဖြစ်စေ၊ အလားတူ လွတ်လပ်သော မဲပေးစနစ် ဖြင့်ဖြစ်စေ ကျင်းပရမည်။'''
            win = u'''tydk'f 21
            vlwdkif;wGif rdrdEdkifiH\ tkyfcsKyfa&;ü udk,fwdkifjzpfap? vGwfvyfpGm a½G;cs,fvdkufonhf udk,fpm;vS,frsm;rS wpfqihfjzpfap yg0if aqmif½GufEdkifcGihf &Sdonf/
            vlwdkif;wGif rdrd\EdkifiH&Sd jynfolY 0efxrf;tzGJUü 0ifa&mufEdkif&ef wlnDonhf tcGihf ta&;&Sdonf/
            jynfoljynfom;wdkY\ qE´onf tkyfcsKyf tmPm\ tajccHjzpf&rnf? tqdkyg qE´udk tcsdefumvydkif;jcm;vsuf ppfrSefaoma½G;aumufyGJrsm;jzihf 
            xif&Sm;ap&rnf/ a½G;aumuf yGJrsm;wGifvnf; vlwdkif;tnDtrQ qE´rJ ay;EdkifcGihf &Sd&rnhftjyif ? xdka½G;aumufyGJrsm;udk 
            vQdKY0Suf rJay; pepfjzihf jzpfap? tvm;wl vGwfvyfaom rJay;pepf jzihfjzpfap usif;y&rnf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Twenty One")

        def test_article_twenty_two(self):
            unicode = u'''အပိုဒ် ၂၂
            လူတိုင်းတွင် လူ့အဖွဲ့အစည်း၏ အဖွဲ့ဝင်တစ်ဦးအနေနှင့် လူမှုရေးလုံခြုံခွင့်ရယူပိုင့်ခွင့်ရှိသည့် အပြင်နိုင်ငံရေး ကြိုးပမ်းမှုဖြင့်ဖြစ်စေ၊ 
            နိုင်ငံတကာ ပူပေါင်းဆောင်ရွက်မှုဖြင့်ဖြစ်စေ၊ နိုင်ငံအသီးသီး၏ဖွဲ့စည်းပုံနှင့် လည်းကောင်း၊ သယံဇာတ အင်အားနှင့်လည်းကောင်း 
            ထိုလူ၏ ဂုဏ်သိက္ခာနှင့် စရိုက်လက္ခဏာ လွတ်လပ်စွာ တိုးတက်မြင့်မားရေးအတွက် မရှိမဖြစ်လိုအပ်သော စီးပွားရေး၊လူမှုရေးနှင့် 
            ယဉ်ကျေးမှု အခွင့်အရေးများကို သုံးစွဲပိုင်ခွင့်ရှိသည်။'''
            win = u'''tydk'f 22
            vlwdkif;wGif vlYtzGJUtpnf;\ tzGJU0ifwpfOD;taeESihf vlrIa&;vkHûcHcGihf&,lydkihfcGihf&Sdonhf tjyifEdkifiHa&; BudK;yrf;rIjzihfjzpfap? 
            EdkifiHwum ylaygif;aqmif½GufrIjzihfjzpfap? EdkifiHtoD;oD;\zGJUpnf;ykHESihf vnf;aumif;? o,HZmw tiftm;ESihfvnf;aumif; 
            xdkvl\ *kPfodu©mESihf p½dkufvu©Pm vGwfvyfpGm wdk;wufjrihfrm;a&;twGuf r&Sdrjzpfvdktyfaom pD;yGm;a&;?vlrIa&;ESihf 
            ,Ofaus;rI tcGihfta&;rsm;udk okH;pGJydkifcGihf&Sdonf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Twenty Two")

        def test_article_twenty_three(self):
            unicode = u'''အပိုဒ် ၂၃
            လူတိုင်းတွင် အလုပ်လုပ် ရန်လည်းကောင်း၊ မိမိနှစ်သက်ရာ အသက်မွေးမှု အလုပ် အကိုင်ကို လွတ်လပ်စွာရွေးချယ်ရန် လည်းကောင်း၊ တရားမျှတ၍ 
            လုပ်ပျော်သော အလုပ်ခွင်၏ အခြေအနေကို ရရှိရန် လည်းကောင်း၊ အလုပ်လက်မဲ့ ဖြစ်ရခြင်းမှ အကာအကွယ် ရရှိရန် လည်းကောင်း အခွင့်အရေးရှိသည်။
            လူတိုင်းတွင် ခွဲခြားခြင်းမခံရစေဘဲ၊ တူညီသော အလုပ်အတွက် တူညီသော အခကြေးငွေ ရပိုင်ခွင့်ရှိသည်။
            အလုပ်လုပ်ကိုင်သည့် လူတိုင်းတွင်၊ မိမိနှင့် မိမိ၏ မိသားစုအတွက် လူ့ဂုဏ်သိက္ခာ နှင့် ညီအောင် နေထိုင် စားသောက်နိုင်ရန်၊ စိတ်ချလောက်သည့်ပြင်၊ 
            တရား မျှတ၍ လုပ်ပျော်သည့် လစာကြေးငွေ ရပိုင်ခွင့်ရှိသည်။ လိုအပ်ခဲ့လျှင်အခြား နည်းလမ်းများမှ လူမှုရေး အထောက်အပံ့ကိုလည်း ထပ်မံ၍ ရပိုင်ခွင့် ရှိသည်။
            လူတိုင်းတွင် မိမိအကျိုး ခံစားခွင့်ကို ကာကွယ်ရန် အလုပ်သမား အစည်းအရုံးများ ဖွဲ့စည်းခွင့် ၊ ပါဝင် ဆောင်ရွက်ခွင့် ရှိသည်။'''
            win = u'''tydk'f 23
            vlwdkif;wGif tvkyfvkyf &efvnf;aumif;? rdrdESpfouf&m toufarG;rI tvkyf tudkifudk vGwfvyfpGma½G;cs,f&ef vnf;aumif;? w&m;rQwí 
            vkyfaysmfaom tvkyfcGif\ tajctaeudk &&Sd&ef vnf;aumif;? tvkyfvufrJh jzpf&jcif;rS tumtuG,f &&Sd&ef vnf;aumif; tcGihfta&;&Sdonf/
            vlwdkif;wGif cGJjcm;jcif;rcH&apbJ? wlnDaom tvkyftwGuf wlnDaom tcaMu;aiG &ydkifcGihf&Sdonf/
            tvkyfvkyfudkifonhf vlwdkif;wGif? rdrdESihf rdrd\ rdom;pktwGuf vlY*kPfodu©m ESihf nDatmif aexdkif pm;aomufEdkif&ef? pdwfcsavmufonhfjyif? 
            w&m; rQwí vkyfaysmfonhf vpmaMu;aiG &ydkifcGihf&Sdonf/ vdktyfcJhvQiftjcm; enf;vrf;rsm;rS vlrIa&; taxmuftyHhudkvnf; xyfrHí &ydkifcGihf &Sdonf/
            vlwdkif;wGif rdrdtusdK; cHpm;cGihfudk umuG,f&ef tvkyform; tpnf;t½kH;rsm; zGJUpnf;cGihf ? yg0if aqmif½GufcGihf &Sdonf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Twenty Three")

        def test_article_twenty_four(self):
            unicode = u'''အပိုဒ် ၂၄
            လူတိုင်းတွင် သင့်မြတ်လျော်ကန်စွာ ကန့်သတ်ထားသည့် အလုပ်လုပ်ချိန် အပြင်၊ လစာနှင့်တကွ အခါကာလအားလျော်စွာ သတ်မှတ် ထားသည့် 
            အလုပ် အားလပ်ရက်များပါဝင်သည့် အနားယူခွင့်နှင့် အားလပ်ခွင့် ခံစားပိုင်ခွင့် ရှိသည်။'''
            win = u'''tydk'f 24
            vlwdkif;wGif oihfjrwfavsmfuefpGm ueYfowfxm;onhf tvkyfvkyfcsdef tjyif? vpmESihfwuG tcgumvtm;avsmfpGm owfrSwf xm;onhf 
            tvkyf tm;vyf&ufrsm;yg0ifonhf tem;,lcGihfESihf tm;vyfcGihf cHpm;ydkifcGihf &Sdonf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Twenty Four")

        def test_article_twenty_five(self):
            unicode = u'''အပိုဒ် ၂၅
            လူတိုင်းတွင် မိမိနှင့်တကွ မိမိ၏ မိသားစု ကျန်းမာရေးနှင့်တကွ ကိုယ်စိတ်နှစ်ဖြာ အေးချမ်းစွာ နေထိုင်နိုင်ရေး အတွက် အစာအဟာရ၊ 
            အဝတ်အထည် နေအိမ်၊ ဆေးဝါး အကူအညီနှင့် လိုအပ်သည့် လူမှု အထောက်အပံ့များ ပါဝင်သော သင့်တော် လျှောက်ပတ်သည့် လူမှု အဆင့်အတန်းကို 
            ရယူခံစားခွင့် ရှိသည်။ ထို့ပြင် အလုပ်လက်မဲ့ဖြစ်သော အခါ၌ သော်လည်းကောင်း၊ မကျန်းမမာ ဖြစ်သော အခါ၌ သော်လည်းကောင်း၊ 
            ကိုယ်အင်္ဂါ မစွမ်း မသန်ဖြစ်သော အခါ၌ သော်လည်းကောင်း၊ မုဆိုးမဖြစ်သောအခါ၌ သော်လည်းကောင်း၊ အသက်အရွယ်အိုမင်းသော အခါ၌ 
            သော်လည်းကောင်း၊ မိမိကိုယ်တိုင်က မတတ်နိုင်သော အကြောင်းကြောင့် ဝမ်းစာ ရှာမှီးနိုင်သော နည်းလမ်း မရှိသော အခါ၌ 
            သော်လည်းကောင်း၊ နေထိုင်စားသောက်ရေးအတွက် လုံခြုံစိတ်ချရမှု အခွင့်အရေးရှိသည်။
            သားသည် မိခင်များနှင့် ကလေးများသည် အထူးစောင့်ရှောက်ခြင်းနှင့် အကူအညီပေးခြင်းကို ရခွင့် ရှိသည်။ ဥပဒေအရ ထိမ်းမြားခြင်းဖြင့်ဖြစ်စေ 
            အခြား နည်းဖြင့် ဖြစ်စေ မွေးဖွားသော ကလေးအားလုံး သည် တူညီသော လူမှု ကာကွယ် စောင့်ရှောက်ရေးကို ရယူ ခံစားကြရမည်။'''
            win = u'''tydk'f 25
            vlwdkif;wGif rdrdESihfwuG rdrd\ rdom;pk usef;rma&;ESihfwuG udk,fpdwfESpfjzm at;csrf;pGm aexdkifEdkifa&; twGuf tpmt[m&? 
            t0wftxnf aetdrf? aq;0g; tultnDESihf vdktyfonhf vlrI taxmuftyHhrsm; yg0ifaom oihfawmf avQmufywfonhf vlrI tqihftwef;udk 
            &,lcHpm;cGihf &Sdonf/ xdkYjyif tvkyfvufrJhjzpfaom tcgü aomfvnf;aumif;? rusef;rrm jzpfaom tcgü aomfvnf;aumif;? 
            udk,ft*Fg rpGrf; roefjzpfaom tcgü aomfvnf;aumif;? rkqdk;rjzpfaomtcgü aomfvnf;aumif;? touft½G,ftdkrif;aom tcgü 
            aomfvnf;aumif;? rdrdudk,fwdkifu rwwfEdkifaom taMumif;aMumihf 0rf;pm &SmrSD;Edkifaom enf;vrf; r&Sdaom tcgü 
            aomfvnf;aumif;? aexdkifpm;aomufa&;twGuf vkHûcHpdwfcs&rI tcGihfta&;&Sdonf/
            om;onf rdcifrsm;ESihf uav;rsm;onf txl;apmihfa&Smufjcif;ESihf tultnDay;jcif;udk &cGihf &Sdonf/ Oya't& xdrf;jrm;jcif;jzihfjzpfap 
            tjcm; enf;jzihf jzpfap arG;zGm;aom uav;tm;vkH; onf wlnDaom vlrI umuG,f apmihfa&Smufa&;udk &,l cHpm;Mu&rnf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Twenty Five")

        def test_article_twenty_six(self):
            unicode = u'''အပိုဒ် ၂၆
             လူတိုင်းသည် ပညာသင် ယူနိုင်ခွင့်ရှိသည်၊ အနည်းဆုံးမူလတန်းနှင့် အခြေခံ အဆင့် အတန်းများတွင် ပညာ သင်ကြားရေးသည် အခမဲ့ဖြစ်ရမည်။ 
             မူလတန်းပညာသည် မသင်မနေရ ပညာ ဖြစ်ရမည်။ စက်မှုလက်မှုပညာနှင့် အသက်မွေးမှု ပညာများကို ယေဘူယျအားဖြင့် သင်ကြားရယူ နိုင်စေရမည်။ 
             ထို့ပြင် အထက်တန်းပညာအတွက် အရည်အချင်းကို အခြေခံပြု၍ တူညီသော အခွင့်အရေး ရရှိစေရမည်။
             ပညာသင်ကြားရေးကို လူသားတို့၏ စရိုက်လက္ခဏာ အပြည့်အဝ တိုးတက်မှု အပြင်၊ လူ့အခွင့်အရေးနှင့် အခြေခံလွတ်လပ်ခွင့် ရိုသေ 
             လေးစားမှု တို့ကို ရှင်သန်ဖွံ့ဖြိုးလာစေရန် ရည်ရွယ်၍ သင်ကြား စေရမည်။ ပညာသင်ကြားရေးသည် နိုင်ငံ အားလုံး တို့တွင် လည်းကောင်း၊ 
             လူမျိုးစုများ တွင်လည်းကောင်း၊ ဘာသာရေးအသင်းအဖွဲ့များတွင် လည်းကောင်း၊ အချင်းချင်းနားလည်မှု၊ သည်းခံ မှုနှင့် ခင်မင်ရင်းနှီးမှုတို့ကို အားပေးရမည်။ 
             ထို့ပြင် ငြိမ်းချမ်းရေး တည်တံ့အောင် ဆောင်ရွက်ရန် အလို့ငှါ၊ ကုလသမဂ္ဂ၏ ဆောင်ရွက်မှုများကိုလည်း ဖြစ်မြောက် အောင် အားပေးရမည်။
             မိဘတို့တွင်၊ မိမိတို့၏ ကလေးများ သင်ယူရမည့်ပညာ အမျိုးအစားကို ရွေးချယ်နိုင်သော လက်ဦး အခွင့်အရေးရှိသည်။'''
            win = u'''tydk'f 26
             vlwdkif;onf ynmoif ,lEdkifcGihf&Sdonf? tenf;qkH;rlvwef;ESihf tajccH tqihf twef;rsm;wGif ynm oifMum;a&;onf tcrJhjzpf&rnf/ 
             rlvwef;ynmonf roifrae& ynm jzpf&rnf/ pufrIvufrIynmESihf toufarG;rI ynmrsm;udk a,bl,stm;jzihf oifMum;&,l Edkifap&rnf/ 
             xdkYjyif txufwef;ynmtwGuf t&nftcsif;udk tajccHûyí wlnDaom tcGihfta&; &&Sdap&rnf/
             ynmoifMum;a&;udk vlom;wdkY\ p½dkufvu©Pm tjynhft0 wdk;wufrI tjyif? vlYtcGihfta&;ESihf tajccHvGwfvyfcGihf ½dkao 
             av;pm;rI wdkYudk &SifoefzGHUNzdK;vmap&ef &nf½G,fí oifMum; ap&rnf/ ynmoifMum;a&;onf EdkifiH tm;vkH; wdkYwGif vnf;aumif;? 
             vlrsdK;pkrsm; wGifvnf;aumif;? bmoma&;toif;tzGJUrsm;wGif vnf;aumif;? tcsif;csif;em;vnfrI? onf;cH rIESihf cifrif&if;ESD;rIwdkYudk tm;ay;&rnf/ 
             xdkYjyif Nidrf;csrf;a&; wnfwHhatmif aqmif½Guf&ef tvdkYiSg? ukvor*¾\ aqmif½GufrIrsm;udkvnf; jzpfajrmuf atmif tm;ay;&rnf/
             rdbwdkYwGif? rdrdwdkY\ uav;rsm; oif,l&rnhfynm trsdK;tpm;udk a½G;cs,fEdkifaom vufOD; tcGihfta&;&Sdonf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Twenty Six")

        def test_article_twenty_seven(self):
            unicode = u'''အပိုဒ် ၂၇
            လူတိုင်းတွင် သက်ဆိုင်ရာ ယဉ်ကျေးမှု လောက၌ လွတ်လပ်စွာ ပါဝင်ဆောင် ရွက်နိုင်ခွင့် သုခုမပညာရပ် များကိုလွတ်လပ်စွာလိုက်စား မွေ့လျော်နိုင်ခွင့်၊ 
            သိပ္ပံ ပညာထွန်းကားရေး လုပ်ငန်းများတွင် လွတ်လပ်စွာ ဝင်ရောက် လုပ်ကိုင် နိုင်ခွင့်နှင့် ထိုပညာ၏ အကျိုး အာနိသင်များကို လွတ်လပ်စွာ ခံစားသုံးစွဲနိုင်ခွင့် ရှိသည်။
            လူတိုင်းတွင် သိပ္ပံမှ ဖြစ်စေ၊ စာပေမှဖြစ်စေ၊ သုခုမပညာမှ ဖြစ်စေ၊ မိမိကိုယ်ပိုင်ဉာဏ်ဖြင့်ကြံစည် ဖန်တီးမှုမှ ဖြစ်ထွန်းလာသည့် ဂုဏ်နှင့် ငွေကြေး 
            အကျိုးအမြတ်များကို ခံစားရယူနိုင်ရန် အခွင့်အရေး အတွက် ကာကွယ်မှုကို ရရှိရန် အခွင့်အရေး ရှိသည်။'''
            win = u'''tydk'f 27
            vlwdkif;wGif oufqdkif&m ,Ofaus;rI avmuü vGwfvyfpGm yg0ifaqmif ½GufEdkifcGihf okckrynm&yf rsm;udkvGwfvyfpGmvdkufpm; arGUavsmfEdkifcGihf? 
            odyÜH ynmxGef;um;a&; vkyfief;rsm;wGif vGwfvyfpGm 0ifa&muf vkyfudkif EdkifcGihfESihf xdkynm\ tusdK; tmedoifrsm;udk vGwfvyfpGm cHpm;okH;pGJEdkifcGihf &Sdonf/
            vlwdkif;wGif odyÜHrS jzpfap? pmayrSjzpfap? okckrynmrS jzpfap? rdrdudk,fydkifÓPfjzihfBuHpnf zefwD;rIrS jzpfxGef;vmonhf *kPfESihf aiGaMu; 
            tusdK;tjrwfrsm;udk cHpm;&,lEdkif&ef tcGihfta&; twGuf umuG,frIudk &&Sd&ef tcGihfta&; &Sdonf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Twenty Seven")

        def test_article_twenty_eight(self):
            unicode = u'''အပိုဒ် ၂၈
            လူတိုင်းသည် ဤကြေညာ စာတမ်းတွင် ဖော်ပြထားသည့် အခွင့်အရေးများ နှင့် လွတ်လပ်ခွင့်များကို အပြည့်အစုံ ရယူနိုင်သော လူမှု ဆက်ဆံရေး 
            အခြေအနေနှင့် အပြည်ပြည်ဆိုင်ရာ ဆက်ဆံရေး အခြေအနေတို့၏ အကျိုးကျေးဇူးကို ခံစားနိုင်ခွင့် ရှိသည်။'''
            win = u'''tydk'f 28
            vlwdkif;onf þaMunm pmwrf;wGif azmfjyxm;onhf tcGihfta&;rsm; ESihf vGwfvyfcGihfrsm;udk tjynhftpkH &,lEdkifaom vlrI qufqHa&; 
            tajctaeESihf tjynfjynfqdkif&m qufqHa&; tajctaewdkY\ tusdK;aus;Zl;udk cHpm;EdkifcGihf &Sdonf/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Twenty Eight")

        def test_article_twenty_nine(self):
            unicode = u'''အပိုဒ် ၂၉
            မိမိ၏စရိုက်လက္ခဏာ လွတ်လပ်စွာ ဖွံ့ဖြိုး တိုးတက်နိုင်သည့် တစ်ခုတည်းသော လူ့အသိုက်အဝန်း အတွက်လူတိုင်း၌ တာဝန် ရှိသည်။
            မိမိ၏ အခွင့်အရေးများနှင့် လွတ်လပ် ခွင့်များကို သုံးစွဲရာတွင် လူတိုင်းသည်၊ အခြားသူများ၏ အခွင့်အရေးများနှင့်လွတ်လပ်ခွင့်များကို
            အသိအမှတ်ပြု၍ ရိုသေလေးစားစေရန်အလို့ငှာ လည်းကောင်း၊ ဒီမိုကရေစီကျင့်သုံးသော လူ့အဖွဲ့အစည်းတွင် ကိုယ်ကျင့်တရားအပြင်၊ 
            ရပ်ရွာအေးချမ်းသာယာရေးနှင့် ပြည်သူ့ အကျိုး စီးပွား ဖြစ်ထွန်းရေးတို့ အတွက်၊ တရားမျှတစွာ ကျင့်ဆောင်ရန် အလို့ငှာ လည်းကောင်း၊ 
            ဥပဒေက ပြဌာန်းထားသည့် ချုပ်ချယ်မှုများဖြင့်သာ ကန့်သတ်ခြင်းခံရမည်။
            အဆိုပါ အခွင့်အရေးများနှင့် လွတ်လပ် ခွင့်များကို မည်သည့် အမှုကိစ္စတွင်မျှ ကုလသမဂ္ဂ၏ ရည်ရွယ်ချက်များနှင့်လည်းကောင်း၊ 
            အခြေခံမူများနှင့် လည်းကောင်း ဆန့်ကျင်၍ မသုံးစွဲရ။'''
            win = u'''tydk'f 29
            rdrd\p½dkufvu©Pm vGwfvyfpGm zGHUNzdK; wdk;wufEdkifonhf wpfckwnf;aom vlYtodkuft0ef; twGufvlwdkif;ü wm0ef &Sdonf/
            rdrd\ tcGihfta&;rsm;ESihf vGwfvyf cGihfrsm;udk okH;pGJ&mwGif vlwdkif;onf? tjcm;olrsm;\ tcGihfta&;rsm;ESihfvGwfvyfcGihfrsm;udk
            todtrSwfûyí ½dkaoav;pm;ap&eftvdkYiSm vnf;aumif;? 'Drdkua&pDusihfokH;aom vlYtzGJUtpnf;wGif udk,fusihfw&m;tjyif? 
            &yf½Gmat;csrf;om,ma&;ESihf jynfolY tusdK; pD;yGm; jzpfxGef;a&;wdkY twGuf? w&m;rQwpGm usihfaqmif&ef tvdkYiSm vnf;aumif;? 
            Oya'u jyXmef;xm;onhf csKyfcs,frIrsm;jzihfom ueYfowfjcif;cH&rnf/
            tqdkyg tcGihfta&;rsm;ESihf vGwfvyf cGihfrsm;udk rnfonhf trIudpöwGifrQ ukvor*¾\ &nf½G,fcsufrsm;ESihfvnf;aumif;? 
            tajccHrlrsm;ESihf vnf;aumif; qeYfusifí rokH;pGJ&/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Twenty Nine")

        def test_article_thirty(self):
            unicode = u'''အပိုဒ် ၃ဝ
            ဤကြေညာစာတမ်းပါ အခွင့်အရေးနှင့်တကွ လွတ်လပ်ခွင့်များ ပျက်စီးရာပျက်စီးကြောင်းတို့ကိုရည်ရွယ်၍၊ နိုင်ငံတစ်နိုင်ငံ အတွက် ဖြစ်စေ၊ 
            လူတစ်စုအတွက် ဖြစ်စေ၊ လူတစ်ဦးတစ်ယောက် အတွက် ဖြစ်စေ ပါဝင် ဆောင်ရွက်ရန် အခွင့်ရှိသည်ဟု သော်လည်းကောင်း၊ ကိုယ်တိုင်ဆောင်ရွက်ရန် 
            အခွင့်ရှိသည် ဟုသော်လည်းကောင်းအဓိပ္ပါယ် ပိုင်းခြားကောက်ယူခြင်း မရှိစေရ။'''
            win = u'''tydk'f 30
            þaMunmpmwrf;yg tcGihfta&;ESihfwuG vGwfvyfcGihfrsm; ysufpD;&mysufpD;aMumif;wdkYudk&nf½G,fí? EdkifiHwpfEdkifiH twGuf jzpfap? 
            vlwpfpktwGuf jzpfap? vlwpfOD;wpfa,muf twGuf jzpfap yg0if aqmif½Guf&ef tcGihf&Sdonf[k aomfvnf;aumif;? udk,fwdkifaqmif½Guf&ef 
            tcGihf&Sdonf [kaomfvnf;aumif;t"dyÜg,f ydkif;jcm;aumuf,ljcif; r&Sdap&/'''
            result = uni2win.convert(unicode)
            self.assertEqual(win, result, "Failed to Convert Article Thirty")


if __name__ == "__main__":
    unittest.main()
