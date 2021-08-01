#!/usr/bin/env python3
"""reducer.py"""

from operator import itemgetter
import sys

#mayo julio diciembre
for linea in sys.stdin:
    linea = linea.strip()
    ciudad, mes, ventas = linea.split('\t')
    mes = mes.lower()
    if mes == 'mayo' or mes == 'julio' or mes == 'diciembre':
        print('%s\t%s\t%s' % (ciudad, mes, ventas))