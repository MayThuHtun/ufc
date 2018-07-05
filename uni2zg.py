# -*- coding: utf-8 -*-
import re

def convert(input):
    output = input

    output = output.replace(u'\u1009', u'\u106A')
    return output
