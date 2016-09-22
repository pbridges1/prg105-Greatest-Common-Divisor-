a = raw_input("Enter a number: \n")
b = raw_input("Enter a second number: \n")
a = int(a)
b = int(b)
while a != 0 and b != 0:
    left = a % b
    a = b
    b = left
print (a)
