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
    datosVenta[1] = datosVenta[1].lower()
    if datosVenta[1] == 'mayo' or datosVenta[1] == 'julio' or datosVenta[1] == 'diciembre':
        print('%s\t%s' % (datosVenta[0], datosVenta[2]))