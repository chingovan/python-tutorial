"""
Problem:    Day la mot vi du don gian, nhap vao mot so nguyen va kiem tra xem co phai la hoan hao hay khong.
            So hoan hao la so nguyen duong co tong cac uoc nho hon no bang chinh no (vd: 6 = 3 + 2 + 1)
Coder:       Chi Ngo (chingovan@gmail.com)
Date:        2015/06/01
Slogan:      For a brighter future!
"""
number = int(input("Nhap vao mot so: "))
if number <= 1:
    print(number, " khong phai la so hoan hao")
else:
    sumDivision = 0
    for i in range(1, number):
        
        if number % i == 0:
            sumDivision += i    #sumDivision = sumDivision + i
    
    if sumDivision == number:
        
        print(number, " la so hoan hao")
    else:
        
        print(number, " khong phai la so hoan hoa")  