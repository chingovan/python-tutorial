str1 = 'Hello World'
str2= "I'm Vietnamese"

str3 = str1 + str2

print(str3)

str4 = str1*3

print(str4)

str5 = "Viet"
str6 = "US"

testin1 = str5 in str2
if testin1 == True:
    print( str5, " in ", str2)
else :
    print( str5, " not in ", str2)

testin2 = str6 in str2
if testin2 == True:
    print( str6, " in ", str2)
else:
    print( str6, " not in ", str2)
    
print("Dau xuong dong \n")
print(r"Dau xuong dong \n")
print(R"Dau xuong dong \n")
