#Accept a file name from user and print extension of that
s =str(input("Enter a file name:")) 
l = s.split('.')
print("Filename:",s)
print("The extension:",l[-1])