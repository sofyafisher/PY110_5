from tasks.task1 import conventer
from tasks.task2 import wave
from tasks.task3 import wave_inf
from tasks.task4 import word_value, find_mostvalued
from tasks.task5 import modify
from tasks.task6 import roman_to_int

print(conventer([1, 1, 1, 1]))
print(wave("hello"))

a = wave_inf('hello')
for i in range(8):
    print(next(a))

print(find_mostvalued("abc", "mno", "xyz"))
print(modify("mouse"))

print(roman_to_int("MCMXC"))