def dotProduct(listA, listB):
    productSum = 0
    for i, j in zip(listA, listB):
        productSum += i*j
    print(productSum)

listX = [1, 2, 5]
listY = [5, 6, 7]
dotProduct(listX, listY)