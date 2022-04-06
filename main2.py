from audioop import reverse
import time
from random import randint
from collections import OrderedDict

def timing():
    start_time = time.time()
    return lambda x: print("[{:.2f}s] {}".format(time.time() - start_time, x))

t = timing()

a_list = [randint(1, 100000) for i in range(1,int(input("Enter the length: "))+1)]
res = list(dict.fromkeys(a_list))

# list1 = [i for i in range(1, int(input("Enter range: ")))]


cf = 0
mf = 0 

N = len(res)
for i in range(1, N):
    for j in range(i,0,-1):
        cf += 1
        if res[j] < res[j-1]:
            mf += 1
            res[j], res[j-1] = res[j-1], res[j]
        else:
            break
print(res)
t(f"Loaded {len(res)} rows data from 'a_list'")
print(f'CF= {cf}')
print(f'MF= {mf}')