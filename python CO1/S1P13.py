#13.Create a list of colors from comma-separated color names entered by user. Display  first and last colors.  
#Red,Pink,Orange,Yellow,Purple,Green,Blue,Brown
s =str(input("Enter the color names separated using , :"))
l = [ i for i in s.split(',')]
print(l)
print("First:",l[0], ",","last",l[-1])