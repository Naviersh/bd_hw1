import re
from collections import Counter
import time
import matplotlib.pyplot as plt

points_x = []
points_y = []

def words_counter(file_txt,output):
    start_time = time.time()
    file = open(output, 'w')
    counter = Counter()
    doc = open(file_txt, 'r')
    for line in doc:
        disable_punctuation = re.sub(r'[^\w\s]', '', line).lower()
        for word in disable_punctuation.split():
            counter[word] += 1
    file.write(str(counter))
    file.close()
    file_time = (time.time() - start_time)
    print(file_txt,"--- %s seconds ---" % file_time)
    points_x.append(file_time)
    points_y.append(file_txt)


words_counter('10MB.txt','10MB_output.txt')
words_counter('100MB.txt','100MB_output.txt')
words_counter('1GB.txt','1GB_output.txt')
words_counter('5GB.txt','5GB_output.txt')
words_counter('10GB.txt','10GB_output.txt')

plt.plot(points_x, points_y)
plt.grid(True)
plt.xlabel(u'Time in seconds')
plt.show()