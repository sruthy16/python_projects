

def min(list):
    cur = 0
    for i in list:
        if(cur > i):
            cur = i
    print(cur)

list_num = [1, 5, 4, 8, 89, 56, 34, 0]
min(list_num)