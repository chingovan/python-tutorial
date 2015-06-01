"""
Problem:     Day la mot vi du don gian, nhap vao mot so nguyen va kiem tra xem co phai la so nguyen to hay khong.
            So nguyen to la cac so nguyen duong chi chia het cho 1 va chinh no.
Coder:       Chi Ngo (chingovan@gmail.com)
Date:        2015/06/01
Slogan:      For a brighter future!
"""
number = int(input("Nhap vao mot so nguyen: "))

if number < 2:
    print(number, " khong phai la so nguyen to")
elif number == 2:
    print( number, " la so nguyen to")
else:
    isPrimeNumber = True;
    for i in range(2, number):
        if number % i == 0:
            isPrimeNumber = False;
            break
        
    if isPrimeNumber == True:
        print( number, " la so nguyen to")
    else:
        print(number, " khong phai la so nguyen to")