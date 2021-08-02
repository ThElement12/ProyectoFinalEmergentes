#!/usr/bin/env python3
"""reducer.py"""
#Mes con Mayor y Menor Venta
from operator import itemgetter
import sys

mes_actual = None
total_actual = 0
mes = None
mayor = 0
mes_mayor = None
menor = 0
mes_menor = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip(' ')

    # parse the input we got from mapper.py
    mes, venta = line.split()


    # convert venta (currently a string) to int
    try:
        venta = int(venta)
        if menor == 0:
            menor = venta
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
            if total_actual > mayor:
                mayor = total_actual
                mes_mayor = mes_actual
            elif total_actual < menor:
                menor = total_actual
                mes_menor = mes_actual
        total_actual = venta
        mes_actual = mes

# do not forget to output the last mes if needed!

print('Mayor: %s\t%s' % (mes_mayor, mayor))
print('Menor: %s\t%s' % (mes_menor, menor))
