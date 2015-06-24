code = "ST1"
fullname = "Ngo Van Chi"
gender = True
birthday = "01/01/1989"
address = "Ha noi, Vietnam"

info = code + " " + fullname + " " +  ("Nam" if gender == True else "Nu") + " " + birthday + " " + address

print(info)

info = "%s %s %s %s %s" % (code, fullname,("Nam" if gender == True else "Nu"), birthday, address)
print(info)

print('Mothership was attacked\a\a\a')

print("Hello\nWorld")

print ('Hello\rA\b')

print("Hello\t\tWorld")

str1 = 'Hello World'
str2 = str1.upper()

print(str1)
print(str2)