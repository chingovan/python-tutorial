a=[3, 6, 9, 2, 6, 8, 9, 1, 7, 21, 7, 12]

for i in range(0, len(a)-1):
    
    for j in range(i, len(a)):
        
        if a[i] > a[j]:
            t = a[i];
            a[i] = a[j];
            a[j] = t;
print(a)