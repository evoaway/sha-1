import sha1
import hashlib
import os
import time

def tests():
    message = "The quick brown fox jumps over the lazy dog"
    lib_hash = hashlib.sha1(message.encode()).digest()
    my_hash = sha1.get_digest(message.encode())
    if lib_hash == my_hash:
        print("Passed!", end='\n')
    else:
        print("Fail!", end='\n')

    message = ""
    lib_hash = hashlib.sha1(message.encode()).digest()
    my_hash = sha1.get_digest(message.encode())
    if lib_hash == my_hash:
        print("Passed!", end='\n')
    else:
        print("Fail!", end='\n')
    print(lib_hash, end='\n')
    print(my_hash, end='\n')

    rnd = os.urandom(100)
    lib_hash = hashlib.sha1(rnd).digest()
    my_hash = sha1.get_digest(rnd)
    if lib_hash == my_hash:
        print("Passed!", end='\n')
    else:
        print("Fail!", end='\n')
def time_test():
    rnd = os.urandom(111)
    start_time = time.perf_counter()
    lib_hash = hashlib.sha1(rnd).digest()
    end_time = time.perf_counter()
    elaspsed_time = end_time - start_time
    print("Haslib SHA-1 elapsed time: ", elaspsed_time, end='\n')
    start_time = time.perf_counter()
    my_hash = sha1.get_digest(rnd)
    end_time = time.perf_counter()
    elaspsed_time = end_time - start_time
    print("My SHA-1 elapsed time: ", elaspsed_time, end='\n')

if __name__ == '__main__':
    tests()
    #time_test()
