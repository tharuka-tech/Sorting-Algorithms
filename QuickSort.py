def swap(list ,i,j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def partition(list,start,end):
    print("List: " ,list[start:end + 1])
    pivot=list[end]
    print ("Pivot: ",pivot)
    
    i = start-1
    j = start

    while j < end :
        while pivot < list[j] :
            j += 1
        i += 1   
        swap(list,i,j)
        print(list,"i = ",i,"j = ",j)
    print("Partition: ",list)  
    return i

def quickSort(list,start,end ):
    if start < end:
        p = partition(list,start,end)
        quickSort(list,start,p - 1)
        quickSort(list,p + 1,end)
    
list=[50,23,9,18,61,32]
quickSort(list,0,len(list)-1)





