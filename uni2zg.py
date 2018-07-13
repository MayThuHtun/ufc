# -*- coding: utf-8 -*-

import re


def replace(input):
    output = input

    output = re.sub(u'\u103A', u'\u1039', output)
    # athat
    output = re.sub(u'\u103B', u'\u103A', output)
    # yapint
    output = re.sub(u'\u103C', u'\u103B', output)
    # yayit
    output = re.sub(u'\u103D', u'\u103C', output)
    # waswe
    output = re.sub(u'\u103E', u'\u103D', output)
    # hahtoe
    output = re.sub(u'\u103F', u'\u1086', output)
    # thagyi
    output = re.sub(u'(\u103C\u103D)', u'\u108A', output)
    # waswal_hahtoe
    output = re.sub(u'(\u102B\u1039)', u'\u105A', output)
    # yaycha-athat

    return output


def precompose(input):
    output = input

    # ngr_sint
    output = re.sub(u'\u1004\u103A\u1039', u'\u1064', output)
    output = re.sub(u'(\u1064)([\u1000-\u1021])', u'\\2\\1', output)
    output = re.sub(u'(\u102D\u1036)', u'\u108E', output)
    # lone_gyi_tin_tai_tai_tin
    output = re.sub(u'(\u1064)([\u1000-\u1021])\u102D', u'\\1\u108B', output)
    # with lone_gyi_tin
    output = re.sub(u'(\u1064)([\u1000-\u1021])\u102E', u'\\1\u108C', output)
    # with lone_gyi_tin_san_khat
    output = re.sub(u'(\u1064)([\u1000-\u1021])\u1036', u'\\1\u108D', output)
    # with tai_tai_tin

    # pa_sint
    output = re.sub(u'\u1039\u1000', u'\u1060', output)
    # kagyi
    output = re.sub(u'\u1039\u1001', u'\u1061', output)
    # ka_kway
    output = re.sub(u'\u1039\u1002', u'\u1062', output)
    # ga_nge
    output = re.sub(u'\u1039\u1003', u'\u1063', output)
    # gagyi
    output = re.sub(u'\u1039\u1005', u'\u1065', output)
    # sa_lone
    output = re.sub(u'\u1039\u1006', u'\u1066', output)
    # sa_lane
    output = re.sub(u'\u1039\u1007', u'\u1068', output)
    # za_gwe
    output = re.sub(u'\u1039\u1008', u'\u1069', output)
    # za_myin_zwe
    output = re.sub(u'\u1039\u100B', u'\u106C', output)
    # datalinjade
    output = re.sub(u'\u1039\u100C', u'\u106D', output)
    # htawonbae
    output = re.sub(u'\u100D\u1039\u100D', u'\u106E', output)
    # dayinkaut
    output = re.sub(u'\u100E\u1039\u100D', u'\u106F', output)
    # dayinmot
    output = re.sub(u'\u1039\u100F', u'\u1070', output)
    # nagyi
    output = re.sub(u'\u1039\u1010', u'\u1071', output)
    # da_won_bu
    output = re.sub(u'\u1039\u1011', u'\u1073', output)
    # hta_sin_htoo
    output = re.sub(u'\u1039\u1012', u'\u1075', output)
    # da_dwe
    output = re.sub(u'\u1039\u1013', u'\u1076', output)
    # da_ot_chite
    output = re.sub(u'\u1039\u1014', u'\u1077', output)
    # na
    output = re.sub(u'\u1039\u1015', u'\u1078', output)
    # pasaut
    output = re.sub(u'\u1039\u1016', u'\u1079', output)
    # phoe-loat-htoke
    output = re.sub(u'\u1039\u1017', u'\u107A', output)
    # bae-la-chat
    output = re.sub(u'\u1039\u1018', u'\u107B', output)
    # ba-gone
    output = re.sub(u'\u1039\u1019', u'\u107C', output)
    # ma
    output = re.sub(u'\u1039\u101C', u'\u1085', output)
    # la

    return output


def logical2visual(input):
    output = input

    # 1=letters,2=yayit,3=yapint,4=waswe,5=hahtoe,6=waswe_hahtoe,7=tha_wai_htoe,8=yay_cha
    output = re.sub(
        u'([\u1000-\u1021])((?:\u103B)?)((?:\u103A)?)((?:\u103C)?)((?:\u103D)?)((?:\u108A)?)((?:\u1031)?)((?:\u102C)?)',
        '\\7\\2\\1\\3\\4\\5\\6\\8', output)

    return output


def shape(input):
    output = input
    # yayit

    output = re.sub(u'\u103B([\u1000])', u'\u107E\\1', output)
    # yayit(107E)
    output = re.sub(u'\u107E([\u1000-\u1021])([\u102D\u102E\u1036])', u'\u1080\\1\\2', output)
    # yait(1080)
    output = re.sub(u'\u103B([\u1000-\u1021])([\u102D\u102E\u1036])', u'\u107F\\1\\2', output)
    # yayiy(107F)

    # ta_chaung_ngin
    output = re.sub(
        u'([\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084])([\u1000-\u1021])((?:[\u102D\u102E\u1036])?)\u102F',
        u'\\1\\2\\3\u1033', output)
    # with yayit
    output = re.sub(u'([\u103A\u107D])((?:[\u102D\u102E\u1036])?)\u102F', u'\\1\\2\u1033', output)
    # with yapint

    # tachaunggin with pa-sint
    output = re.sub(u'([\u1060-\u1063])((?:[\u102D\u102E])?)\u102f', u'\\1\\2\u1033', output)
    output = re.sub(u'([\u1065-\u1069])((?:[\u102D\u102E])?)\u102f', u'\\1\\2\u1033', output)
    output = re.sub(u'([\u106C\u106D])((?:[\u102D\u102E])?)\u102f', u'\\1\\2\u1033', output)
    output = re.sub(u'([\u1070-\u107C])((?:[\u102D\u102E])?)\u102f', u'\\1\\2\u1033', output)
    output = re.sub(u'([\u1085\u1093])((?:[\u102D\u102E])?)\u102f', u'\\1\\2\u1033', output)

    # 2_chaung_ngin
    output = re.sub(
        u'([\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084])([\u1000-\u1021])((?:[\u102D\u102E\u1036])?)\u1030',
        u'\\1\\2\\3\u1034', output)
    # with yayit
    output = re.sub(u'([\u103A\u107D])((?:[\u102D\u102E\u1036])?)\u1030', u'\\1\\2\u1034', output)
    # with yapint
    output = re.sub(u'\u103D\u1030', u'\u1089', output)
    # with hahtoe

    # yapint
    output = re.sub(u'\u103A([\u103C\u103D])', u'\u107D\\1', output)

    # out-ka-myint
    output = re.sub(u'([\u1014\u101B\u1008\u1030\u1033\u102F\u1034])((?:[\u1032\u1036])?)\u1037', u'\\1\\2\u1094',
                    output)
    output = re.sub(u'([\u103C\u103D\u108A\u1088])((?:[\u1032\u1036])?)\u1037', u'\\1\\2\u1095', output)

    # na-nge
    output = re.sub(u'\u1014([\u103C\u103D\u108A])', u'\u108F\\1', output)

    # nange with pr-sint
    output = re.sub(u'\u1014((?:[\u102D\u102E])?)([\u1060-\u1063])', u'\u108F\\1\\2', output)
    output = re.sub(u'\u1014((?:[\u102D\u102E])?)([\u1065-\u1069])', u'\u108F\\1\\2', output)
    output = re.sub(u'\u1014((?:[\u102D\u102E])?)([\u106C\u106D])', u'\u108F\\1\\2', output)
    output = re.sub(u'\u1014((?:[\u102D\u102E])?)([\u1070-\u107C])', u'\u108F\\1\\2', output)
    output = re.sub(u'\u1014((?:[\u102D\u102E])?)([\u1085\u1093])', u'\u108F\\1\\2', output)

    # hahtoe
    output = re.sub(u'(\u100A)\u103D', u'\\1\u1087', output)
    # with nya

    # nya-lay
    output = re.sub(u'\u1009(\u1039)', u'\u1025\\1', output)

    # ya-kaut
    output = re.sub(u'\u101B\u102F', u'\u1090\u102F', output)
    # ya-kaut with 1-chaunggin

    # ya-kaut with pr-sint
    output = re.sub(u'\u101B((?:[\u102D\u102E])?)([\u1060-\u1063])', u'\u1090\\1\\2', output)
    output = re.sub(u'\u101B((?:[\u102D\u102E])?)([\u1065-\u1069])', u'\u1090\\1\\2', output)
    output = re.sub(u'\u101B((?:[\u102D\u102E])?)([\u106C\u106D])', u'\u1090\\1\\2', output)
    output = re.sub(u'\u101B((?:[\u102D\u102E])?)([\u1070-\u107C])', u'\u1090\\1\\2', output)
    output = re.sub(u'\u101B((?:[\u102D\u102E])?)([\u1085\u1093])', u'\u1090\\1\\2', output)

    return output


def convert(input):
    output = input

    output = precompose(output)
    output = replace(output)
    output = logical2visual(output)
    output = shape(output)

    return output

