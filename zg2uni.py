# -*- coding: utf-8 -*-
import re


def convert(input):
    output = input
    ##nyalay
    output = output.replace(u'\u106A', u'\u1009')

    #1chaungngin
    output = output.replace(u'\u1033', u'\u102F')

    #2chaungngin
    output = output.replace(u'\u1034', u'\u1030')

    #yayit
    output = output.replace(u"[\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084]", u"\u103C")

    #nya
    output = output.replace(u'\u106B', u'\u100A')

    #hahtoe
    output = output.replace(u'\u103D', u'\u103E')
    output = output.replace(u'\u107D', u'\u103E')
    output = output.replace(u'\u1087', u'\u103E')

    #yacaut
    output = output.replace(u'\u1090', u'\u101B')

    #htaonepae
    output = output.replace(u'\u1092', u'\u100C')

    #dayinkaut
    output = output.replace(u'\u106E', u'\u100D')

    #tatalin
    output = output.replace(u'\u1090', u'\u100B')

    #na
    output = output.replace(u'\u108F', u'\u1014')

    #waswe
    output = output.replace(u'\u103C', u'\u103D')


    return output
