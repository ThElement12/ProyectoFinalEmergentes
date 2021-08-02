#!/usr/bin/env python3
"""reducer.py"""
# Mes con Mayor y Menor Venta
from operator import itemgetter
import sys

ciudad_actual = None
total_actual = 0
ciudad = None
mayor = 0
ciudad_mayor = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip(' ')

    # parse the input we got from mapper.py
    ciudad, venta = line.split()

    # convert venta (currently a string) to int
    try:
        venta = int(venta)

    except ValueError:
        # venta was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: mes) before it is passed to the reducer
    if ciudad_actual == ciudad:
        total_actual += venta

    else:
        if ciudad_actual:
            if total_actual > mayor:
                mayor = total_actual
                mes_mayor = ciudad_actual

        total_actual = venta
        ciudad_actual = ciudad

# do not forget to output the last mes if needed!

print('Ciudad Con mayor venta: %s\t%s' % (mes_mayor, mayor))
