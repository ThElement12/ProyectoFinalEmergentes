#!/usr/bin/env python3
"""reducer.py"""
from operator import itemgetter
import sys

mes_actual = None
total_actual = 0
mes = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip(' ')

    # parse the input we got from mapper.py
    mes, venta = line.split()

    # convert venta (currently a string) to int
    try:
        venta = int(venta)
    except ValueError:
        # venta was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: mes) before it is passed to the reducer
    if mes_actual == mes:
        total_actual += venta
    else:
        if mes_actual:
            # write result to STDOUT
            print('%s\t%s' % (mes_actual, total_actual))
        total_actual = venta
        mes_actual = mes

# do not forget to output the last mes if needed!
if mes_actual == mes:
    print('%s\t%s' % (mes_actual, total_actual))
