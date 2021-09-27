import os
import random

with open('text.txt') as f:
    strings = [line for line in f]
    line_count = len(strings)
print('Количество строк:',line_count)

with open('1MB.txt', "w") as new_f:
    file_size = 0
    while file_size < 1024*1024:
        n = random.randint(0, line_count-1)
        new_f.write(strings[n])
        file_size = os.path.getsize('1MB.txt')
    new_f.close()
    print(file_size, "байт")



