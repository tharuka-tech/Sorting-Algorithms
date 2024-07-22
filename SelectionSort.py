def selectionSort(sList):
    for i in range (0, len(sList) - 1):
        minIndex = i
        for j in range (i+1, len(sList)):
           if sList[j] < sList[minIndex]:
                minIndex = j
        
        if minIndex != i:
            sList[i],sList[minIndex] = sList[minIndex], sList[i]
    

exList = [2, 6, 9, 0, 10, 4]
selectionSort(exList)
print(exList)