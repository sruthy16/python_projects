
def unique(list):
    uniqueList = []
    for i in list:
        if i not in uniqueList:
            uniqueList.append(i)
    print(uniqueList)

numList = [1, 4, 4, 5, 6, 8, 8, 7, 8, 8, 8, 9, 9, 9]
unique(numList)



