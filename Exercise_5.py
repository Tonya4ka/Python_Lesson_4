# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
import re
from random import randint

def format_poly(dct_poly):
    poly='+'.join([f'{(v,"")[v==1]}x^{k}' for k,v in dct_poly.items() if v][::-1])
    pattern = "(\d+)?([a-z])\^(\d+)"
    result = [ re.match(pattern, el).groups() for el in poly.split('+') ]
    result = [ list(el) for el in result ]
    result = [[v if v is not None else '1' for v in el1] for el1 in result]
    
    new_poly = ''
    for el in result:
        if int(el[2]) > 1:
            new_poly+=el[0]+'*'+el[1]+'^'+el[2]+'+'
        elif int(el[2]) == 1:
            new_poly+=el[0]+'*'+el[1]+'+'
        elif int(el[2]) == 0:
            new_poly+=el[0]

    if new_poly[-1]=='+':
        new_poly = new_poly[:-1]    
    if new_poly[:2] == '1*':
        new_poly = new_poly[2:]

    return new_poly
        
def parse_poly(poly):
    new_poly = poly.split('+')
    dct = {}

    for el in new_poly:
        if 'x^' in el:
            k = el.split('x^')[1]
            v = list(el.split('x^')[0])
            if '*' in v:
                del(v[v.index('*')])
            v = "".join(v)
            if v == '':
                v = 1
            dct.update({int(k): int(v)})
        elif 'x' in el and 'x^' not in el:
            dct.update({1: int(el.split('*x')[0])})
            if v == '':
                v = 1
        elif 'x' not in el:
            dct.update({0: int(el)})
    return dct

def read_data():
    with open('polynom.txt', 'r') as poly1:
        res1 = [ line.strip() for line in poly1.readlines() ]

    with open('polynom2.txt', 'r') as poly2:
        res2 = [ line.strip() for line in poly2.readlines() ]

    return res1[0], res2[0]
        
poly1, poly2 = read_data()
x, y = parse_poly(poly1), parse_poly(poly2)

res_poly = {k: x.get(k, 0) + y.get(k, 0) for k in set(x) | set(y)}
print(format_poly(res_poly))

with open('sum_polynom.txt', 'w') as data:
    data.write(format_poly(res_poly))