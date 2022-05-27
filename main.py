from tasks.task1 import conventer
from tasks.task2 import wave
from tasks.task3 import wave_inf
from tasks.task4 import find_mostvalued
from tasks.task5 import modify
from tasks.task6 import roman_to_int
from tasks.task7 import person

print("Задание1:", conventer([1, 1, 1, 1]))
print("Задание2:", wave("hello"))

a = wave_inf('hello')
print("Задание3:")
print("----------")
for i in range(8):
    print(next(a))
print("----------")

print("Задание4:", find_mostvalued("abc", "mno", "xyz"))
print("Задание5:", modify("mouse"))

print("Задание6:", roman_to_int("MCMXC"))

print("Задание7:")
print("----------")
for key, value in person().items():
  print("{0}: {1}".format(key,value))
print("----------")