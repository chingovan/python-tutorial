"""
Problem:    Day la mot vi du don gian, nhap vao mot so nguyen va kiem tra xem co phai la chinh phuong hay khong.
            So nguyen a duoc goi la so chinh phuong neu ton tai mot so nguyen x sao cho x*x == a
Coder:       Chi Ngo (chingovan@gmail.com)
Date:        2015/06/04
Slogan:      For a brighter future!
"""

def isSquareNumber(num):
    if number <= 0:
    
        return False
    else:
    
        isSquareNumber = False
        for i in range(1, number + 1):
        
            if i * i == number:
            
                isSquareNumber = True
                break
        
        if isSquareNumber == True:
            return True
        else:
            return False
        
number = int(input("Nhap vao mot so nguyen:"))

result = isSquareNumber(number)

if result == True:
    
    print( number, " la so chinh phuong")
else:
    
    print(number, " khong phai la so chinh phuong")