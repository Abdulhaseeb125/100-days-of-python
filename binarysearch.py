import random
import time


def binary_search(num_list: list, search):
    global founded
    center = (len(num_list) - 1) // 2
    if num_list == []:
        founded = False
        return
    if search == num_list[center]:
        founded = True
    elif search < num_list[center]:
        binary_search(num_list[:center], search)
    elif search > num_list[center]:
        binary_search(num_list[center + 1:], search)

    if founded == True:
        return True
    else:
        return False


num_list = []
for i in range(0,100000000):
    num_list.append(i)
result = binary_search(num_list, 99999)
print(time.process_time())
print(result)
