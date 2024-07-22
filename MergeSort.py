def mergeSort(mergeList):
    if len(mergeList) > 1:
        # Finding the middle of the list
        mid = len(mergeList) // 2
        
        # Dividing the list elements into two halves
        left_half = mergeList[:mid]
        right_half = mergeList[mid:]
        
        # Recursively sorting each half
        mergeSort(left_half)
        mergeSort(right_half)
        
        # Merging the sorted halves
        i = j = k = 0
        
        # Copy data to temporary lists left_half and right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                mergeList[k] = left_half[i]
                i += 1
            else:
                mergeList[k] = right_half[j]
                j += 1
            k += 1
        
        # Checking if any element was left
        while i < len(left_half):
            mergeList[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            mergeList[k] = right_half[j]
            j += 1
            k += 1

    return mergeList


exList = [2, 6, 9, 0, 10, 4]
mergeSort(exList)
print(exList)
