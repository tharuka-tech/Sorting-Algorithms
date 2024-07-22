
def bubbleSort(bubbleList):
    for i in range(0 , len(bubbleList)-1):
        #i part ensures that we do not recheck elements that have already been sorted in previous passes
        for j in range (0 , len(bubbleList)-1-i):
            if bubbleList[j] > bubbleList[j+1]:
                bubbleList[j] , bubbleList[j+1] = bubbleList[j+1] , bubbleList[j]
    return bubbleList



exList = [2,6,9,0,10,4]
(bubbleSort(exList))
print(exList)