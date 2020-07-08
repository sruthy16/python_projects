def dotProduct(listA, listB):
    productSum = 0
    for i, j in zip(listA, listB):
        productSum += i*j
    print(productSum)

def matrixMultiplication(matrixA, matrixB):
    result = [matrixA][matrixB[0]]
    for i in range(len(matrixA)):
        for j in  range(len(matrixB[0])):
            for x in range(len(matrixB)):
                result[i][k]
