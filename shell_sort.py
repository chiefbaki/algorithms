import time 
from random import randint, random, shuffle

def timing():
    start_time = time.time()
    return lambda x: print("[{:.2f}s] {}".format(time.time() - start_time, x))

t = timing()

# a_list = [randint(1, 1000) for i in range(1, int(input("Enter range: "))+1)]
# res = list(dict.fromkeys(a_list))

n = int(input("Enter range: "))
res = [*range(1, n+1)]
shuffle(res)

def shell_sort(lst):
    gap = len(lst) // 2

    cf = 0 
    mf = 0
    
    while gap > 0:
        for value in range(gap, len(lst)):
            current_value = lst[value]
            position = value

            cf += 1
            while position >= gap and lst[position - gap] > current_value:
                lst[position] = lst[position - gap]
                mf += 1
                position -= gap
                lst[position] = current_value

        gap //= 2

    print(f'cf: {cf}')
    print(f'mf: {mf}')
    return lst 

t(f"Loaded {len(res)} rows data from 'res'")
print(shell_sort(res))
