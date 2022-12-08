# Вычислить число c заданной точностью d
# Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
num = math.pi
precision = int(input("Enter the precision for the number Pi: "))
def roundno(num, precision):
    scale = 10.0 ** precision
    return int(num * scale) / scale
print(roundno(num,precision))