# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import re
from random import randint

k = int(input("Enter the power k: "))
koeff=[randint(0,100) for i in range(k)]+[randint(1,100)]
poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])
print(poly)

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
        
print(new_poly)

with open('polynom.txt', 'w') as data:
    data.write(new_poly)