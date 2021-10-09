import re
import numpy
from collections import Counter
import time

start_time = time.time()
f = open('output.txt', 'w')
cnt = Counter()
doc = open('1GB.txt', 'r')
text_string = doc.read().lower()
opt = re.sub(r'[^\w\s]','', text_string)
for word in opt.split():
    cnt[word] += 1
f.write(str(cnt))
f.close()
file_time = (time.time() - start_time)
print("--- %s seconds ---" % file_time)

