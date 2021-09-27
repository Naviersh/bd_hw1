import os
import time

def multiplication(new_file,size):
    file_size = 0
    start_time = time.time()
    with open(new_file, "w") as file:
        with open('1MB.txt', "r") as o_file:
            strings = "".join([line for line in o_file])
            while file_size < size:
                file.write(strings)
                file_size = os.path.getsize(new_file)
    file.close()
    time_script = print(new_file, "--- %s seconds ---" % (time.time() - start_time))
    return new_file, time_script;

multiplication('10MB.txt',1024*1024*10)
multiplication('100MB.txt',1024*1024*100)
multiplication('1GB.txt',1024*1024*1000)
multiplication('5GB.txt',1024*1024*1000*5)
multiplication('10GB.txt',1024*1024*10000)


