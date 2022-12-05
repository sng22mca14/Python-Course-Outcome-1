'''3. List comprehensions:
(a) Generate positive list of numbers from a given list of integers
(b) Square of N numbers
(c) Form a list of vowels selected from a given word
(d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values)'''



#a Generate positive list of numbers from a given list of integers 
l=[-2,1,3,-3,4,-4]
s=[i for i in l if i>=0]
print(s)

# b Square of N numbers
l=[-2,1,3,-3,4,-4]
s=[i*i for i in l ]
print(s)

#c Form a list of vowels selected from a given word
v=['a','e','i','o','u','A','E','I','O','U']
w=input("Enter the word:")
s=[i for i in w if i in v]
print(s)
print("number of vowels:",len(s)) 

#d List ordinal value of each element of a word (Hint: use ord() to get ordinal values)
w=input("Enter the word:")
s=[ord(i) for i in w]
print(s)