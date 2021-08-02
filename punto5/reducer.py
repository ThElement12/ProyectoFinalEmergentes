#!/usr/bin/env python3
"""reducer.py"""
from operator import itemgetter
import sys

mes_actual = None
total_actual = 0
mes = None

for line in sys.stdin:
    line = line.strip()
    mes, venta = line.split()
    try:
        venta = int(venta)
    except ValueError:
        continue
    if mes_actual == mes:
        total_actual += venta
    else:
        if mes_actual:
            print('%s\t%s' % (mes_actual, total_actual))
        total_actual = venta
        mes_actual = mes

if mes_actual == mes:
    print('%s\t%s' % (mes_actual, total_actual))
