from tasks.task1 import conventer
from tasks.task2 import wave
from tasks.task3 import wave_inf

print(conventer([1, 1, 1, 1]))
print(wave("hello"))

a = wave_inf('hello')
for i in range(8):
    print(next(a))