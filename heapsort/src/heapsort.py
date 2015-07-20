def heap(myList, lastIndex):
    
    if(lastIndex == 0) :
        
        return;
    else :

        i = lastIndex;
        while (i >= 1) :        
            parentIndex = int((i - 1) / 2);
            # Co the thay the bang cach
            # if lastIndex % 2 == 0:
            #    parentIndex = int((i - 2) / 2)
            # else:
            #    parentIndex = int((i - 1) / 2)
            
            if myList[parentIndex] > myList[i]:
                temp = myList[i]
                myList[i] = myList[parentIndex]
                myList[parentIndex] = temp;

            
            i = i - 1

def heapsort(myList, listSize):
    for i in range(1, listSize):
        heap(myList, listSize-i)
        temp = myList[0]
        myList[0] = myList[listSize - i]
        myList[listSize - i] = temp

a = [3, 6, 9, 2, 6, 8, 9, 1, 7, 21, 7, 12]
    
print("Before sorting: ", a)
heapsort( a, len(a))
print("After sorting: ", a)
print("After reversed: ", a[::-1])