eps = float(input("Nhap so sai so :"))

s = 1
t = 1
i = 1
while t > eps:
    t = t / i
    i = i + 1
    s = s + t
    
print("e = ", s)