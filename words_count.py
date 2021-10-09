import re
from collections import Counter
import time

start_time = time.time()
f = open('output.txt', 'w')
cnt = Counter()
doc = open('1MB.txt', 'r')
for line in doc:
    opt = re.sub(r'[^\w\s]', '',line)
    for word in line.split():
        cnt[word] += 1
f.write(str(cnt))
f.close()
file_time = (time.time() - start_time)
print("--- %s seconds ---" % file_time)

