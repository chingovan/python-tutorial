x = float(input("Nhap vao x: "));
n = int(input("Nhap vao so vong lap: "))

s = 1
t = 1
for i in range(1, n + 1):
    t = t*x/i
    s = s + t
    
print("e^%f = %f"%(x, s))