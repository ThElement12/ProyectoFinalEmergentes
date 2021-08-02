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
    datosVenta[0] = datosVenta[0].lower()
    if (datosVenta[1] == 'enero' and (datosVenta[0] == 'santiago' or datosVenta[0] == 'la_vega' or datosVenta[0] == 'moca') ) or \
            (datosVenta[1] == 'marzo' and (datosVenta[0] == 'santiago' or datosVenta[0] == 'la_vega' or datosVenta[0] == 'moca') ):
        print('%s\t%s' % (datosVenta[0], datosVenta[2]))