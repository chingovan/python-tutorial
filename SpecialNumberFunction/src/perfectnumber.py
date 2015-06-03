"""
Problem:    Day la mot vi du don gian, nhap vao mot so nguyen va kiem tra xem co phai la hoan hao hay khong.
            So hoan hao la so nguyen duong co tong cac uoc nho hon no bang chinh no (vd: 6 = 3 + 2 + 1)
Coder:       Chi Ngo (chingovan@gmail.com)
Date:        2015/06/03
Slogan:      For a brighter future!
"""
def isPerfectNumber(num):
    if num <= 1:
        return False;
    else:
        sumDivision = 0
        for i in range(1, num):
        
            if num % i == 0:
                sumDivision += i    #sumDivision = sumDivision + i
    
    
        return True if sumDivision == num else False
        #return sumDivision == number ? True : False;  
        
number = int(input("Nhap vao mot so: "))

result = isPerfectNumber(number);

if result:
    
    print(number, " la so hoan hao")
else:
    
    print(number, " khong la so hoan hao")