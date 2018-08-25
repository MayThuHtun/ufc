# -*- coding: utf-8 -*-
import re

def replace(input):
    output = input
    #  nyalay

    output = output.replace(u'\u106A', u'\u1009')

    #  nya
    output = output.replace(u'\u106B', u'\u100A')

    #  yakaut
    output = output.replace(u'\u1090', u'\u101B')

    #  1chaungngin
    output = output.replace(u'\u1033', u'\u102F')

    #  2chaungngin
    output = output.replace(u'\u1034', u'\u1030')

    #  hahtoe
    output = output.replace(u'\u103D', u'\u103E')
    output = output.replace(u'\u1087', u'\u103E')

    #  waswae
    output = output.replace(u'\u103C', u'\u103D')

    #  yayit

    output = output.replace(u'\u103B', u'\u103C')
    output = output.replace(u'\u107E', u'\u103C')
    output = output.replace(u'\u107F', u'\u103C')
    output = output.replace(u'\u1080', u'\u103C')
    output = output.replace(u'\u1081', u'\u103C')
    output = output.replace(u'\u1082', u'\u103C')
    output = output.replace(u'\u1083', u'\u103C')
    output = output.replace(u'\u1084', u'\u103C')

    #  yapin
    output = output.replace(u'\u103A', u'\u103B')
    output = output.replace(u'\u107D', u'\u103B')

    #  htawonbae

    #  dayinkaut

    #  tatalin

    #  athat
    output = output.replace(u'\u1039', u'\u103A')

    #  outkamyint
    output = output.replace(u'\u1094', u'\u1037')
    output = output.replace(u'\u1095', u'\u1037')

    #  na
    output = output.replace(u'\u108F', u'\u1014')

    #  thagyi
    output = output.replace(u'\u1086', u'\u103F')

    return output


def decompose(input):

    output = input

    output = re.sub(u'\u1025(?=[\u103a\u102C])', u'\u1009', output)
    output = re.sub(u'([\u1000-\u1021])\u1064', u'\u1064\\1', output)  # nga-thet+yay-char
    output = re.sub(u'([\u1000-\u1021])(\u108B)', u'\u1064\\1\u102D', output)  # con+ngathetlgt
    output = re.sub(u'([\u1000-\u1021])(\u108C)', u'\u1064\\1\u102E', output)  # con+ngathetlgtsk
    output = re.sub(u'([\u1000-\u1021])(\u108D)', u'\u1064\\1\u1036', output)  # con+ngathetttt
    output = re.sub(u'\u108E', u'\u102D\u1036', output)

    output = re.sub(u'\u1088', u'\u103E\u102F', output)
    output = re.sub(u'\u1089', u'\u103E\u1030', output)
    output = re.sub(u'\u105A', u'\u102B\u103A', output)
    output = re.sub(u'\u108A', u'\u103D\u103E', output)

    #  #########  patsint

    output = re.sub(u'\u1060', u"\u1039\u1000", output)
    #  ka
    output = re.sub(u'\u1061', u'\u1039\u1001', output)
    #  kha
    output = re.sub(u'\u1062', u'\u1039\u1002', output)
    #  ga-nge
    output = re.sub(u'\u1063', u'\u1039\u1003', output)
    #  ga-gyi
    output = re.sub(u'\u1065', u"\u1039\u1005", output)
    #  sa-lone
    output = re.sub(u'[\u1066\u1067]', u'\u1039\u1006', output)
    #  sa-lane
    output = re.sub(u'\u1068', u'\u1039\u1007', output)
    #  za
    output = re.sub(u'\u1069', u'\u1039\u1008', output)
    #  za-zwe
    output = re.sub(u'\u106C', u'\u1039\u100B', output)
    #  tatalin
    output = re.sub(u'\u1070', u'\u1039\u100F', output)
    #  na-gyi
    output = re.sub(u'[\u1071\u1072]', u'\u1039\u1010', output)
    #  ta
    output = re.sub(u'[\u1073\u1074]', u'\u1039\u1011', output)
    #  da
    output = re.sub(u'\u1075', u'\u1039\u1012', output)
    #  da-dwe
    output = re.sub(u'\u1076', u'\u1039\u1013', output)
    #  da-out
    output = re.sub(u'\u1077', u'\u1039\u1014', output)
    #  na
    output = re.sub(u'\u1078', u'\u1039\u1015', output)
    #  pa
    output = re.sub(u'\u1079', u'\u1039\u1016', output)
    #  pha
    output = re.sub(u'\u107A', u'\u1039\u1017', output)
    #  ba-htet
    output = re.sub(u'[\u107B\u1093]', u'\u1039\u1018', output)
    #  ba
    output = re.sub(u'\u107C', u'\u1039\u1019', output)
    #  ma
    output = re.sub(u'\u1085', u'\u1039\u101C', output)
    #  la
    output = re.sub(u'\u106D', u'\u1039\u100C', output)
    #  hta-won-bae

    #########
    #output = re.sub(u'([\u1000-\u1021])(\u1064)(\u1036)', u'\\2\\1\\3', output)
    #output = re.sub('\u1064', u'\u1004\u103A\u1039', output)
    #  up-ngathat

    output = re.sub(u'\u104E', u'\u104E\u1004\u103A\u1038', output)
    #  la-gaung

    output = re.sub(u'\u105A', u'\u102B' + u'\u103A', output)
    #  yaychar-htoe

    output = re.sub(u'\u108A', u'\u103D' + u'\u103E', output)
    #  wa-hatoe

    output = re.sub(u'\u1088', u'\u103E' + u'\u102F', output)
    #  hatoe-1chaung

    output = re.sub(u'\u1089', u'\u103E' + u'\u1030', output)
    #  hatoe-2chaung

    output = re.sub(u'\u103E\u103B', u'\u103B' + u'\u103E', output)
    #  yapin-hatoe

    output = re.sub(u'\u108E', u'\u102D' + u'\u1036', output)
    #  lgt-ttt

    output = re.sub(u'\u108B', u'\u1004' + u'\u103A' + u'\u1039' + u'\u102D', output)
    #  ngathat-lgt

    output = re.sub(u'\u108C', u'\u1004' + u'\u103A' + u'\u1039' + u'\u102E', output)
    #  ngathat-lgtsk

    output = re.sub(u'\u108D', u'\u1004' + u'\u103A' + u'\u1039' + u'\u1036', output)
    #  ngathat-ttt

    ##########
    output = re.sub(u'\u1091', u'\u100F\u1039\u100D', output)
    #  ganda
    output = re.sub(u'\u1092', u'\u100B\u1039\u100C', output)
    #  htawombae-ayit
    output = re.sub(u'\u1097', u'\u100B\u1039\u100B', output)
    #  tatalin
    output = re.sub(u'\u106F', u'\u100D\u1039\u100E', output)
    #  dayin-hmote
    output = re.sub(u'\u106E', u'\u100D\u1039\u100D', output)
    #  dayinkaut

    return output


def visual2logical(input):
    ##########Pattern

    output = input

    output = re.sub(
        u'((?:\u1031)?)((?:\u103c)?)((?:\u1064)?)([\u1000-\u1021])((?:\u1039[\u1000-\u1021])?)((?:\u103b)?)((?:\u103d)?)((?:\u103e)?)((?:\u1037)?)((?:\u102c)?)', '\\3\\4\\5\\2\\6\\7\\8\\1\\9\\10', output)

    output = re.sub(u'(\u102F)([\u102D\u102E])', '\\2\\1', output)
    output = re.sub(u'(\u1030)([\u102D\u102E])', '\\2\\1', output)
    output = re.sub(u'\u1064', u'\u1004\u103A\u1039', output)

    return output


def convert(input):
    output = input
    output = replace(output)
    output = decompose(output)
    output = visual2logical(output)

    return output
