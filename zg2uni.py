# -*- coding: utf-8 -*-
import re


def convert(input):
    output = input
    #  nyalay
    output = output.replace(u'\u106A', u'\u1009')

    #  1chaungngin
    output = output.replace(u'\u1033', u'\u102F')

    #  2chaungngin
    output = output.replace(u'\u1034', u'\u1030')

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

    #  nya
    output = output.replace(u'\u106B', u'\u100A')

    #  hahtoe
    output = output.replace(u'\u103D', u'\u103E')
    output = output.replace(u'\u107D', u'\u103E')
    output = output.replace(u'\u1087', u'\u103E')

    #  yakaut
    output = output.replace(u'\u1090', u'\u101B')

    #  htawonbae
    output = output.replace(u'\u1092', u'\u100C')

    #  dayinkaut
    output = output.replace(u'\u106E', u'\u100D')

    #  tatalin
    output = output.replace(u'\u1097', u'\u100B')

    #  na
    output = output.replace(u'\u108F', u'\u1014')

    #  athat
    output = output.replace(u'\u1039', u'\u103A')

    #  waswae
    #  thagyi
    output = output.replace(u'\u1086', u'\u103F')

    #  outkamyint
    output = output.replace(u'\u1094', u'\u1037')
    output = output.replace(u'\u1095', u'\u1037')

    return output
