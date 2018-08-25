# -*- coding: utf-8 -*-

import re


def replace(input):

    output = input

    output = re.sub(u'\u1000', u'\u0075', output)#kagyi
    output = re.sub(u'\u1001', u'\u0063', output)#kha_kway
    output = re.sub(u'\u1002', u'\u002a', output)#ga_nge
    output = re.sub(u'\u1003', u'\u0043', output)#ga_gyi
    output = re.sub(u'\u1004', u'\u0069', output)#nga
    output = re.sub(u'\u1005', u'\u0070', output)#sa_lone
    output = re.sub(u'\u1006', u'\u0071', output)#sa_lane
    output = re.sub(u'\u1007', u'\u005A', output)#za_gwe
    output = re.sub(u'\u1009', u'\u00DA', output)#nya_gyi
    output = re.sub(u'\u100A', u'\u006E', output)#nya_thay
    output = re.sub(u'\u100B', u'\u0023', output)#ta_talin_gait
    output = re.sub(u'\u100E', u'\u0058', output)#hta_wen_bae
    output = re.sub(u'\u100D', u'\u0021', output)#da_yin_gout
    output = re.sub(u'\u100E', u'\u00A1', output)#da_yin_mote
    output = re.sub(u'\u100F', u'\u0050', output)#na_gyi
    output = re.sub(u'\u1010', u'\u0077', output)#ta_wen_pu
    output = re.sub(u'\u1011', u'\u0078', output)#ta_sin_tuu
    output = re.sub(u'\u1012', u'\u0027', output)#da_dway
    output = re.sub(u'\u1013', u'\u0022', output)#da_oat_chait
    output = re.sub(u'\u1014', u'\u0045\u0065', output)#na_nge
    output = re.sub(u'\u1015', u'\u0079', output)#pa_sout
    output = re.sub(u'\u1016', u'\u007A', output)#pa_oo_htoke
    output = re.sub(u'\u1017', u'\u0041', output)#ba_dad_chait
    output = re.sub(u'\u1018', u'\u0062', output)#ba_gone
    output = re.sub(u'\u1019', u'\u0072', output)#ma
    output = re.sub(u'\u101A', u'\u002C', output)#ya_ba_lat
    output = re.sub(u'\u101B', u'\u0026', output)#ya_gout
    output = re.sub(u'\u101C', u'\u0076', output)#la
    output = re.sub(u'\u101D', u'\u0030', output)#wa
    output = re.sub(u'\u101E', u'\u006F', output)#ta
    output = re.sub(u'\u101F', u'\u005B', output)#ha
    output = re.sub(u'\u1020', u'\u0056', output)#la_gyi
    output = re.sub(u'\u1021', u'\u0074', output)#ar
    output = re.sub(u'\u1023', u'\u00a3', output)#kayi 2 sint
    output = re.sub(u'\u1024', u'\u00fe', output)# eii
    output = re.sub(u'\u1025', u'\u004f', output)# oo
    output = re.sub(u'\u1027', u'\u007b', output)# at_kayar_a
    output = re.sub(u'\u102b', u'\u0067', output)# yay_char_long
    output = re.sub(u'\u102c', u'\u006d', output)# yay_char
    output = re.sub(u'\u102d', u'\u0064', output)# longgyitin
    output = re.sub(u'\u102e', u'\u0044', output)# longgyitin_sanke
    output = re.sub(u'\u102f', u'\u004B', output)# 1_chuang_ngin
    output = re.sub(u'\u1030', u'\u004C', output)# 2_chuang_ngin
    output = re.sub(u'\u1031', u'\u0061', output)#ta_wai_htoe
    output = re.sub(u'\u1032', u'\u004a',  output)#naut_htoe_pyit
    output = re.sub(u'\u1036', u'\u0048',  output)#taytay_tin
    output = re.sub(u'\u1037', u'\u0068', output)# aut_ka__myit
    output = re.sub(u'\u1038', u'\u003b', output)#wa_sa_paut
    output = re.sub(u'\u103a', u'\u0066', output)# nga_tat
    output = re.sub(u'\u103b', u'\u0073', output)# ya_pint
    output = re.sub(u'\u103c', u'\u006A', output)  # ya_yit
    output = re.sub(u'\u103d', u'\u0047', output)#wa_swe
    output = re.sub(u'\u103e', u'\u0053', output)# ha_toe
    output = re.sub(u'\u103f', u'\u00f3', output)#ta_gy


    # nunbers
    output = re.sub(u'\u1041', u'\u0031', output)  # one
    output = re.sub(u'\u1042', u'\u0032', output)  # two
    output = re.sub(u'\u1043', u'\u0033', output)  # three
    output = re.sub(u'\u1044', u'\u0034', output)  # four
    output = re.sub(u'\u1045', u'\u0035', output)  # five
    output = re.sub(u'\u1046', u'\u0036', output)  # six
    output = re.sub(u'\u1047', u'\u0037', output)  # seven
    output = re.sub(u'\u1048', u'\u0038', output)  # eight
    output = re.sub(u'\u1049', u'\u0039', output)  # nine


    output = re.sub(u'\u104a', u'\u003f', output)# poat_kalay
    output = output.replace(u'\u104b', u'\u002f')  # poat_ma
    output = re.sub(u'\u104c', u'\u00fc', output)  # nai
    output = re.sub(u'\u104d', u'\u00ed', output)  # yway
    output = re.sub(u'\u104e', u'\u00a4', output)  # la_guang
    output = output.replace(u'\u104f', u'\u005c')  # ii


    return output

def decompose(input):
    output = input

    output = re.sub(u'\u1008', u'\u0070\u0073', output)#za_myin_zwe
    output = re.sub(u'\u1026', u'\u004f\u0044', output)#oo_lgt_sanket
    output = re.sub(u'\u1029', u'\u006a\u006f', output)#aww
    output = re.sub(u'\u102a', u'\u0061\u006a\u006f\u006d\u006f', output)#aww_thway_htoe
    output = re.sub(u'\u102b\u103a', u'\u003a', output)  # yaychar_shayhtoe
    output = re.sub(u'\u007e\u0047', u'\u003c', output)#yayit_agyi_waswe
    output = re.sub(u'\u0060\u0047', u'\u003e', output)  # yayit_waswe
    output = re.sub(u'\u0050\u1039\u0021', u'\u0040', output)#nagyi_dayingout
    output = re.sub(u'\u0053\u006b', u'\u0049',  output)#hatoe_1chaung
    output = re.sub(u'\u0053\u006c', u'\u00aa', output)#hatoe_2chaung
    output = re.sub(u'\u0073\u0053', u'\u0051', output)#yapint_hatoe
    output = re.sub(u'\u0073\u0047', u'\u0052',  output)#yapint_waswe
    output = re.sub(u'\u0047\u0053', u'\u0054',  output)#waswe_hatoe
    output = re.sub(u'\u0073\u0054', u'\u0057',  output)#yapint_waswe_hatoe
    output = re.sub(u'\u00da\u006d', u'\u00d3', output)#nya_yaychar

    # pr_sint
    output = re.sub(u'\u0023\u1039\u0023', u'\u00a5', output)#ttlg_2sint
    output = re.sub(u'\u1039\u0043', u'\u00a2', output)#gagyi
    output = re.sub(u'\u1039\u0078', u'\u00a6', output)#ta_sin_too
    output = re.sub(u'\u1039\u0022', u'\u00a8', output)#da_oak_chait
    output = re.sub(u'\u1039\u0063', u'\u00a9', output)#kha_kway
    output = re.sub(u'\u1039\u0072', u'\u00ae', output)#ma
    output = re.sub(u'\u1039\u0058', u'\u00b2', output)#ta_wen_bae
    output = re.sub(u'\u1039\u0023', u'\u00b3', output)#ddlg
    output = re.sub(u'\u1039\u0027', u'\u00b4', output)#da_dway
    output = re.sub(u'\u0021\u1039\u00a1', u'\u00b9', output)#dyg_dym
    output = output.replace(u'\u1039\u002a', u'\u00be')#ga_nge
    output = re.sub(u'\u1039\u0041', u'\u00c1', output)#ba_lat_chai
    output = re.sub(u'\u1039\u0077', u'\u00c5', output)#ta_wen_pu
    output = re.sub(u'\u1039\u005a', u'\u00c6', output)#za_gwe
    output = re.sub(u'\u1039\u0062', u'\u00c7', output)#ba_gone
    output = re.sub(u'\u1039\u0077\u0047', u'\u00c9', output)#dwa
    output = re.sub(u'\u1039\u0070\u0073', u'\u00d1', output)#za_myin_zwe
    output = re.sub(u'\u1039\u0050', u'\u00d6', output)#na_gyi
    output = re.sub(u'\u0021\u1039\u0021', u'\u00d7', output)#dayin_gout_2sint
    output = re.sub(u'\u1039\u0079', u'\u00dc', output)#pa_saut
    output = re.sub(u'\u1039\u0071', u'\u00e4', output)#sa_lane
    output = re.sub(u'\u1039\u007a', u'\u00e6', output)#pa_oo_htoke
    output = re.sub(u'\u1039\u0065', u'\u00e9', output)#na_nge
    output = re.sub(u'\u1039\u0070', u'\u00f6', output)#sa_lone
    output = re.sub(u'\u1039\u0075', u'\u00fa', output)#ka_gyi
    output = re.sub(u'\u1039\u0076', u'\u2019', output)#la

    return output

def logical2visual(input):
    output = input

    # 1=letters
    # 2=yayit
    # 3=yapint
    # 4=waswe
    # 5=hatoe
    # 6=tawaetoe
    # 7=nga_tat
    # 8=aumyit
    # 9=yaychar
    output = re.sub(u'([\u1000-\u1021])((?:\u103c)?)((?:\u103b)?)((?:\u103d)?)((?:\u103e)?)((?:\u1031)?)((?:\u103a)?)((?:\u1037)?)((:\u102c)?)','\\6\\2\\1\\3\\4\\5\\7\\8\\9', output)
    output = re.sub(u'(\u1021)((?:[\u102d\u102f])?)\u102f', u'\\1\\2\u006b', output)


    # nga_that and wasapout
    output = re.sub(u'\u1038\u1039', u'\u1039\u1038', output)

    # nga_sint
    output = re.sub(u'\u102d\u1036\u1039', u'\u00f0', output)
    output = re.sub(u'\u1004\u103a\u1039', u'\u0046', output)  # normal
    output = re.sub(u'(\u0046)([\u1000-\u1021])', '\\2\\1', output)
    output = re.sub(u'([\u1000-\u1021])\u0046\u102d', u'\\1\u00d8', output)#lgt
    output = re.sub(u'([\u1000-\u1021])\u0046\u102e', u'\\1\u00d0', output)#longgyitinsanke
    output = re.sub(u'([\u1000-\u1021])\u0046\u1036', u'\\1\u00f8', output)#taytaytin

    return output


def shape(input):
    output = input

    # ya_yit
    output = re.sub(u'\u103c([\u1000\u1003\u1006\u100f\u1010\u1011\u1018\u101a\u101c\u101e\u101f\u1021])', u'\u004d\\1', output)  # ya_yit_agyi
    output = re.sub(u'\u103c([\u1000-\u1021])([\u102d\u102e\u1036])', u'\u004e\\1\\2', output)  # yayit_lgt(sanke)
    output = re.sub(u'\u004d([\u1000-\u1021])([\u102d\u102e\u1036])', u'\u0042\\1\\2', output)  # yayit_agi lgt(sanke)
    output = re.sub(u'\u103c([\u1000-\u1021])(\u103d)', u'\u0060\\1\\2', output)  # yayit with waswe
    output = re.sub(u'\u004d([\u1000-\u1021])(\u103d)', u'\u007e\\1\\2', output)  # yayit_agyi with waswe

    # ta/na_chuang_ngin
    output = re.sub(u'([\u1000-\u1007])((?:[\u102d\u102e])?)((?:\u103e)?)\u102f', u'\\1\\2\\3\u006b', output)  # 1chaung_some letters
    output = re.sub(u'([\u1009-\u100b])((?:[\u102d\u102e])?)((?:\u103e)?)\u102f', u'\\1\\2\\3\u006b', output)  # 1chaung_some letters
    output = re.sub(u'([\u100e-\u101f])((?:[\u102d\u102e])?)((?:\u103e)?)\u102f', u'\\1\\2\\3\u006b', output)  # 1chaung_some letters
    output = re.sub(u'(\u1021)((?:[\u102d\u102e])?)((?:\u103e)?)\u102f', u'\\1\\2\\3\u006b', output)  # 1chaung with some letters
    output = re.sub(u'([\u1000-\u1007])((?:[\u102d\u102e])?)((?:\u103e)?)\u1030', u'\\1\\2\\3\u006c', output)  # 2chaung_some letters
    output = re.sub(u'([\u1009-\u100b])((?:[\u102d\u102e])?)((?:\u103e)?)\u1030', u'\\1\\2\\3\u006c', output)  # 2chaung_some letters
    output = re.sub(u'([\u100e-\u101f])((?:[\u102d\u102e])?)((?:\u103e)?)\u1030', u'\\1\\2\\3\u006c', output)  # 2chaung_some letters
    output = re.sub(u'(\u1021)((?:[\u102d\u102e])?)((?:\u103e)?)\u1030', u'\\1\\2\\3\u006c', output)  # 2chaung_some_letters
    output = re.sub(u'\u004d([\u1000-\u1021])\u006b', u'\u00ea\\1', output)  # yayit_agyi_1chaung
    output = re.sub(u'\u103c([\u1000-\u1021])\u006b', u'\u00fb\\1', output)  # yayit_1chaung
    output = re.sub(u'([\u006a\u0042\u004d\u004e\u0060])([\u1000-\u1021])((?:[\u102d\u102e])?)((?:\u0047)?)\u006b', u'\\1\\2\\3\\4\u004b', output)  # 1chaung
    output = re.sub(u'([\u006a\u0042\u004d\u004e\u0060])([\u1000-\u1021])((?:[\u102d\u102e])?)((?:\u0047)?)\u006c', u'\\1\\2\\3\\4\u004c', output)  # 2chaung
    output = re.sub(u'\u1039([\u1000-\u1021])((?:[\u102d\u102e])?)\u006b', u'\u1039\\1\\2\u004b', output)  # 1chaung
    output = re.sub(u'\u1039([\u1000-\u1021])((?:[\u102d\u102e])?)\u006c', u'\u1039\\1\\2\u004c', output)  # 1chaung

    output = re.sub(u'\u100a\u103e', u'\u100a\u00a7', output)  # nya_ hatoe
    output = re.sub(u'\u1009(\u103a)', u'\u1025\\1', output)  # nyapyat_oo

    output = re.sub(u'\u1014((?:[\u102d\u102e\u1032])?)([\u103d\u103e\u102f\u1030\u006b\u006c])', u'\u0045\\1\\2', output)#nga_nge_apyat
    output = re.sub(u'\u1014\u1039([\u1000-\u1021])', u'\u0045\u1039\\1', output)  # 2chaung_prsint

    # out_ka_myit
    output = re.sub(u'([\u1014\u102f\u1030\u006b\u006c])((?:[\u1032\u1036])?)\u1037', u'\\1\\2\u0059', output)
    output = re.sub(u'([\u103d\u103e])((?:[\u1032\u1036])?)\u1037', u'\\1\\2\u0055', output)
    output = re.sub(u'(\u103d\u103e)\u1037', u'\\1\u0055', output)


    output = re.sub(u'\u101b((?:[\u102d\u102e\u1032])?)([\u102f\u1030\u103d\u006b\u006c])', u'\u00bd\\1\\2', output)#yagout

    output = re.sub(u'\u100a(\u103d\u103e)', u'\u00f1\\1', output)  # nya_ waswe_hatoe

    return output


def convert(input):

    output = logical2visual(input)
    output = shape(output)
    output = replace(output)
    output = decompose(output)

    return output
