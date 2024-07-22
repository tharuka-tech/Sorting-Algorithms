def mBubbleSort(bubbleList):
    n = len(bubbleList)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):  # The -i part ensures that we do not recheck elements that have already been sorted in previous passes
            if bubbleList[j] > bubbleList[j + 1]:
                # Swap elements if they are in the wrong order
                bubbleList[j], bubbleList[j + 1] = bubbleList[j + 1], bubbleList[j]
                swapped = True
        # If no swaps were made during the pass, the list is already sorted
        if not swapped:
            break
    return bubbleList

exList = [2, 6, 9, 0, 10, 4]
mBubbleSort(exList)
print(exList)