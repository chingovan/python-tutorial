n = int(input("Nhap so vong lap :"))

s = 1;
t = 1;
for i in range(1, n + 1):
    t = t / i
    s = s + t
    
print("e = ", s)