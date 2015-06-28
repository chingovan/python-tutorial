a = ['life', 'is', 'not', 'fair', 'get', 'used', 'to', 'it']

def getLastCharacter(s):
    return s[-1]


print(a)

b = sorted(a, key=getLastCharacter)

print("List a :" , a)
print("List b : ", b)