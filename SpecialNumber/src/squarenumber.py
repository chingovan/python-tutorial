"""
Problem:    Day la mot vi du don gian, nhap vao mot so nguyen va kiem tra xem co phai la chinh phuong hay khong.
            So nguyen a duoc goi la so chinh phuong neu ton tai mot so nguyen x sao cho x*x == a
Coder:       Chi Ngo (chingovan@gmail.com)
Date:        2015/06/01
Slogan:      For a brighter future!
"""

number = int(input("Nhap vao mot so nguyen:"))
if number <= 0:
    
    print(number, " khong phai la so chinh phuong")
else:
    
    isSquareNumber = False
    for i in range(0, number + 1):
        
        if i * i == number:
            
            isSquareNumber = True
            break
        
    if isSquareNumber == True:
        print( number, " la so chinh phuong")
    else:
        print(number, " khong phai la so chinh phuong")