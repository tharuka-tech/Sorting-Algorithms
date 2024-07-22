def insertionSort(inList):
    for i in range(1, len(inList)):
        curNum = inList[i]
        j = i - 1
        while j >= 0 and inList[j] > curNum:
            inList[j + 1] = inList[j]
            j -= 1
        inList[j + 1] = curNum

exList = [2, 6, 9, 0, 10, 4]
insertionSort(exList)
print(exList)
