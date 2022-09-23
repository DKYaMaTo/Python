def findMax(dataArray, i, max):
    if i == 0:
        return max

    if i > 0:
        if dataArray[i] > max:
            max = dataArray[i]

        return findMax(dataArray, i - 1, max)


def sumNegative(dataArray, i, j):
    if j <= i:

        if dataArray[j] < 0:
            return dataArray[j] + sumNegative(dataArray, i, j + 1)

        else:
            return sumNegative(dataArray, i, j + 1)
    else:
        return 0


dataArray = [-110, -503, 15, -7, 11, 13, 17, -19, 2, 29, 31, 37, 41, 4, -3, 10]

Max = dataArray[0]
i = len(dataArray) - 1
j = 0

print("The biggest number is", str(findMax(dataArray, i, Max)), end="")
print(" and the sum of negative number is ", (sumNegative(dataArray, i, j)))
