# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
lst = [int(i) for i in input("Enter the numbers of the list separated by space: ").split()]
for i in lst:
   if lst.count(i) == 1:
       print(i, end=" ")