#!/usr/bin/env python3
import sys
"""mapper.py"""

# input comes from STDIN (standard input)
for linea in sys.stdin:
    # remove leading and trailing whitespace
    linea = linea.strip(' ')
    # split the linea into words
    datosVenta = linea.split()
    # increase counters
    print('%s\t%s' % (datosVenta[0], datosVenta[2]))