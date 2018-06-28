# -*- coding: utf-8 -*-

# Usage: main.py inputfilename.ext outputfilename.ext
# Example: main.py zawgyi.txt unicode.txt

import codecs
import zg2uni
import sys

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]
input_file = codecs.open(input_file_name,encoding='utf-8')
output_file = codecs.open(output_file_name,encoding='utf-8', mode='w')

for input_line in input_file:
  input_line = zg2uni.convert(input_line)
  output_file.write(input_line)
  output_file.flush()

input_file.close()
output_file.close()
