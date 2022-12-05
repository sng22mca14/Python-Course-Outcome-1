#9.Create a string from given string where first and last characters exchanged.   [eg: python > nythop]
s = "python"
first = s[0]
last = s[-1]
s = last+ s[1:-1]+first
print(s)