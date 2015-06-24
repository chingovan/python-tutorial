x = float(input("Nhap vao x: "));
eps = float(input("Nhap so sai so :"))

s = 1
t = 1
i = 1
while t > eps:
    t = t * x / i
    i = i + 1
    s = s + t
    
print("e^%f = %f" % (x, s))
