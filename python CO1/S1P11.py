#11.Find biggest of 3 numbers entered
a = int(input("Enter number a:"))
b =int(input("Enter number b:"))
c = int(input("Enter number c:"))
if a>b:
    if a>c:
        print(a," is greater")
    else:
        print(c," is greater")
else:
    if b>c:
        print(b," is greater")
    else:
        print(c," is greater")
        