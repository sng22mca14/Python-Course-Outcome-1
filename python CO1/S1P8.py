s = "onion"
temp = s[0]
for i in s[1:]:
    if s[0] == i:
        temp = temp+'$'
    temp = temp+i
print(temp)