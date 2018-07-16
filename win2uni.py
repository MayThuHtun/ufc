# -*- coding: utf-8 -*-
import re


def convert(input):
    output = input
    output = output.replace(u'\u004F', u'\u1025')  # u
    output = output.replace(u'\u00CD', u'\u1009')  # nya-lay
    output = output.replace(u'\u00DA', u'\u1009')

    #  #####Consonent
    output = output.replace(u'\u0075', u'\u1000')  # ka
    output = output.replace(u'\u0063', u'\u1001')  # kha
    output = output.replace(u'\u002A', u'\u1002')  # ga-nge
    output = output.replace(u'\u0043', u'\u1003')  # ga-gyi
    output = output.replace(u'\u0069', u'\u1004')  # nga
    output = output.replace(u'\u0070', u'\u1005')  # sa-lone
    output = output.replace(u'\u0071', u'\u1006')  # sa-lane
    output = output.replace(u'\u005A', u'\u1007')  # za
    output = output.replace(u'\u006E', u'\u100A')  # nya
    output = output.replace(u'\u00F1', u'\u100A')
    output = output.replace(u'\u0023', u'\u100B')  # ta-ta-lin
    output = output.replace(u'\u0058', u'\u100C')  # hta-won-bae
    output = output.replace(u'\u0021', u'\u100D')  # da-yin-kaut
    output = output.replace(u'\u00A1', u'\u100E')  # da-yin-mote
    output = output.replace(u'\u0050', u'\u100F')  # na-gyi
    output = output.replace(u'\u0077', u'\u1010')  # ta-won-pu
    output = output.replace(u'\u0078', u'\u1011')  # hta-sin-htoo
    output = output.replace(u'\u0027', u'\u1012')  # da-dway
    output = output.replace(u'\u0022', u'\u1013')  # da-out-chaint
    output = output.replace(u'\u0065', u'\u1014')  # na
    output = output.replace(u'\u0045', u'\u1014')
    output = output.replace(u'\u0079', u'\u1015')  # pa
    output = output.replace(u'\u007A', u'\u1016')  # pha
    output = output.replace(u'\u0041', u'\u1017')  # ba-htet
    output = output.replace(u'\u0062', u'\u1018')  # ba
    output = output.replace(u'\u0072', u'\u1019')  # ma
    output = output.replace(u'\u002C', u'\u101A')  # ya-pa-lat
    output = output.replace(u'\u0026', u'\u101B')  # ya-kaut
    output = output.replace(u'\u00BD', u'\u101B')
    output = output.replace(u'\u0076', u'\u101C')  # la
    #  wa
    output = output.replace(u'\u0030', u'\u1040')
    output = output.replace(u'\u0030', u'\u101D')
    output = output.replace(u'\u1040', u'\u101D')

    output = output.replace(u'\u006F', u'\u101E')  # tha
    output = output.replace(u'\u005B', u'\u101F')  # ha
    output = output.replace(u'\u0056', u'\u1020')  # la-gyi
    output = output.replace(u'\u0074', u'\u1021')  # ah

    # #####
    output = output.replace(u'\u00A3', u'\u1023')  # ka+ku
    output = output.replace(u'\u00FE', u'\u1024')  # eei
    output = output.replace(u'\u007B', u'\u1027')  # a
    output = output.replace(u'\u00FC', u'\u104C')  # nike
    output = output.replace(u'\u00ED', u'\u104D')  # ywae
    output = output.replace(u'\u00A4', u'\u104E')  # lae-kaung
    output = output.replace(u'\u005C', u'\u104F')  # ei
    output = output.replace(u'\u00F3', u'\u103F')  # tha-gyi

    #  ##### Number
    output = output.replace(u'\u0031', u'\u1041')  # one
    output = output.replace(u'\u0032', u'\u1042')  # two
    output = output.replace(u'\u0033', u'\u1043')  # three
    output = output.replace(u'\u0034', u'\u1044')  # four
    output = output.replace(u'\u0035', u'\u1045')  # five
    output = output.replace(u'\u0036', u'\u1046')  # six
    output = output.replace(u'\u0037', u'\u1047')  # seven
    output = output.replace(u'\u0038', u'\u1048')  # eight
    output = output.replace(u'\u0039', u'\u1049')  # nine

    output = output.replace(u'\u003F', u'\u104A')  # 1chaung-pote
    output = output.replace(u'\u002F', u'\u104B')  # 2chaung-pote

    # #####
    output = output.replace(u'\u0067', u'\u102B')  # yay-char-gi
    output = output.replace(u'\u006D', u'\u102C')  # yay-char-lay
    output = output.replace(u'\u0064', u'\u102D')  # lone-gyi-tin
    output = output.replace(u'\u0044', u'\u102E')  # lone-gyi-tin-san-khat
    output = output.replace(u'\u004B', u'\u102F')  # 1-chaung-ngin
    output = output.replace(u'\u006B', u'\u102F')
    output = output.replace(u'\u004C', u'\u1030')  # 2-chaung-ngin
    output = output.replace(u'\u006C', u'\u1030')
    output = output.replace(u'\u0061', u'\u1031')  # tha-way-htoe
    output = output.replace(u'\u004A', u'\u1032')  # naut-pyit
    output = output.replace(u'\u0048', u'\u1036')  # ttt
    output = output.replace(u'\u0055', u'\u1037')  # out-ka-myint
    output = output.replace(u'\u0059', u'\u1037')
    output = output.replace(u'\u0068', u'\u1037')
    output = output.replace(u'\u003B', u'\u1038')  # wit-sa-2lone-paut
    output = output.replace(u'\u0066', u'\u103A')  # a-thet
    output = output.replace(u'\u00DF', u'\u103B')  # ya-pit
    output = output.replace(u'\u0073', u'\u103B')
    output = output.replace(u'\u0042', u'\u103C')  # ya-yit
    output = output.replace(u'\u004D', u'\u103C')
    output = output.replace(u'\u004E', u'\u103C')
    output = output.replace(u'\u0060', u'\u103C')
    output = output.replace(u'\u006A', u'\u103C')
    output = output.replace(u'\u0078', u'\u103C')
    output = output.replace(u'\u0047', u'\u103D')  # wa-swe
    output = output.replace(u'\u0053', u'\u103E')  # ha-htoe

    output = re.sub(u'\u0070\u0073', u'\u1008', output)
    output = re.sub(u'\u1005\u103B', u'\u1008', output)  # za-myin-zwe

    # ##########
    output = re.sub(u'([\u1000-\u1021])\u0046', u'\u0046\\1', output)  # up-ngathat
    output = re.sub(u'([\u1000-\u1021])\u00D0', u'\u0046\\1\u102E', output)  # with-lgtsk
    output = re.sub(u'([\u1000-\u1021])\u00D8', u'\u0046\\1\u102D', output)  # with-lgt
    output = re.sub(u'([\u1000-\u1021])\u00F8', u'\u0046\\1\u1036', output)  # with-ttt

    output = re.sub('\u0046', u'\u1004\u103A\u1039', output)  # up-ngathat

    output = re.sub(u'\u00F0', u'\u102D' + u'\u1036', output)  # lgt-ttt
    output = re.sub(u'\u00D8', u'\u1004' + u'\u103A' + u'\u1039' + u'\u102D', output)  # ngathat-lgt
    output = re.sub(u'\u00D0', u'\u1004' + u'\u103A' + u'\u1039' + u'\u102E', output)  # ngathat-lgtsk
    output = re.sub(u'\u00F8', u'\u1004' + u'\u103A' + u'\u1039' + u'\u1036', output)  # ngathat-ttt
    output = re.sub(u'\u003A', u'\u102B' + u'\u103A', output)  # yaychar-htoe
    output = re.sub(u'\u0054', u'\u103D' + u'\u103E', output)  # wa-hatoe
    output = re.sub(u'\u0049', u'\u103E' + u'\u102F', output)  # hatoe-1chaung
    output = re.sub(u'\u00AA', u'\u103E' + u'\u1030', output)  # hatoe-2chaung
    output = re.sub(u'\u0051', u'\u103B' + u'\u103E', output)  # yapit-hatoe
    output = re.sub(u'\u0052', u'\u103B' + u'\u103D', output)  # yapit-waswe
    output = re.sub(u'\u0057', u'\u103B' + u'\u103D' + u'\u103E', output)  # yapit-waswe-hatoe
    output = re.sub(u'[\u003C\u003E]', u'\u103B' + u'\u103D', output)  # yayit-waswe
    output = re.sub(u'\u00FB', u'\u103C' + u'\u102F', output)  # yayit-1chaung

    output = re.sub(u'\u00D3', u'\u1009\u102C', output)  # nya-lay+yaychar

    output = re.sub(u'\u004F\u0044', u'\u1025\u102E', output)  # u+lgtsk
    output = re.sub(u'\u1025\u102E', u'\u1026', output)
    output = re.sub(u'\u004F\u0044', u'\u1026', output)

    # ##### pat-sint

    output = re.sub(u'\u00FA', u"\u1039\u1000", output)  # ka
    output = re.sub(u'\u00A9', u'\u1039\u1001', output)  # kha
    output = re.sub(u'\u00BE', u'\u1039\u1002', output)  # ga-nge
    output = re.sub(u'\u00A2', u'\u1039\u1003', output)  # ga-gyi
    output = re.sub(u'\u00F6', u"\u1039\u1005", output)  # sa-lone
    output = re.sub(u'\u00E4', u'\u1039\u1006', output)  # sa-lane
    output = re.sub(u'\u00C6', u'\u1039\u1007', output)  # za
    output = re.sub(u'\u00D1', u'\u1039\u1008', output)  # za-zwe
    output = re.sub(u'\u00B3', u'\u1039\u100B', output)  # tatalin
    output = re.sub(u'\u00B2', u'\u1039\u100C', output)  # hta-won-bae
    output = re.sub(u'\u00A2', u'\u1039\u100F', output)  # ns-gyi
    output = re.sub(u'[\u00C5\u00E5]', u'\u1039\u1010', output)  # ta
    output = re.sub(u'[\u00A6\u00AC]', u'\u1039\u1011', output)  # hta
    output = re.sub(u'\u00B4', u'\u1039\u1012', output)  # da-dwe
    output = re.sub(u'\u00A8', u'\u1039\u1013', output)  # da-out
    output = re.sub(u'\u00E9', u'\u1039\u1014', output)  # na
    output = re.sub(u'\u00DC', u'\u1039\u1015', output)  # pa
    output = re.sub(u'\u00E6', u'\u1039\u1016', output)  # pha
    output = re.sub(u'\u00C1', u'\u1039\u1017', output)  # ba-htet
    output = re.sub(u'\u00C7', u'\u1039\u1018', output)  # ba
    output = re.sub(u'\u00AE', u'\u1039\u1019', output)  # ma
    output = re.sub(u'\u2019', u'\u1039\u101C', output)  # la
    output = re.sub(u'\u00C9', u'\u1039\u1010\u103D', output)  # ta-wa-swe


    #  ####

    output = re.sub(u'\u0040', u'\u1091', output)  # gan-da
    output = re.sub(u'\u00A5', u'\u100B\u1039\u100B', output)  # double-tatalin-jake
    output = re.sub(u'\u00B9', u'\u100D\u1039\u100E', output)  # da-yin-mode+kaut
    output = re.sub(u'\u00D7', u'\u100D\u1039\u100D', output)  # double-da-yin-kaut


    # ###pattern
    output = re.sub(
        u'((?:\u1031)?)((?:\u103C)?)([\u1000-\u1021])((?:\u103B)?)((?:\u103D)?)((?:\u103E)?)((?:\u1037)?)((?:\u102C)?)',
        r'\3\2\4\5\6\1\7\8', output)

    return output
