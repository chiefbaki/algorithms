from random import randint, shuffle
import datetime

lst = [*range(int(input("Enter range: ")))]
shuffle(lst)

def linear_search(lst, k):
    cf = 0
    for i in range(len(lst)):
        cf += 1
        if lst[i] == k:
            return i
    return f"cf: {cf}"


start = datetime.datetime.now()
linear_search = linear_search(lst, 10)
print(linear_search)
print(f"End time: {datetime.datetime.now() - start}")