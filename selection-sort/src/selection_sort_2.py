a=[3, 6, 9, 2, 6, 8, 9, 1, 7, 21, 7, 12]

for i in range(0, len(a)-1):
    minValue = a[i];
    k = i;
    for j in range(i, len(a)):
        
        if minValue > a[j]:
            minValue = a[j];
            k = j;
    
    #Neu tim duoc phan tu khac nho hon a[i] thi doi cho.
    if k != i:
        t = a[k];
        a[k] = a[i];
        a[i] = t;
print(a)