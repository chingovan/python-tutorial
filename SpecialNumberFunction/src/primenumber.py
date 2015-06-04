"""
Problem:     Day la mot vi du don gian, nhap vao mot so nguyen va kiem tra xem co phai la so nguyen to hay khong.
            So nguyen to la cac so nguyen duong chi chia het cho 1 va chinh no.
Coder:       Chi Ngo (chingovan@gmail.com)
Date:        2015/06/03
Slogan:      For a brighter future!
"""
def isPrimerNumber(num):
    
    if num < 2:
        
        return False
    elif num == 2:
     
        return True
    else:
        isPrimeNum = True;
        for i in range(2, num):
            if num % i == 0:
                isPrimeNum = False;
                break
        
        if isPrimeNum == True:
            return True
        else:
            return  False

number = int(input("Nhap vao mot so nguyen: "))

result = isPrimerNumber(number)
if result == True:
    
    print(number, " la so nguyen to")
else:
    
    print(number, " khong la so nguyen to")