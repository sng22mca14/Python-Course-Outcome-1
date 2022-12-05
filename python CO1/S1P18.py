#18. Merge two dictionaries. 
dic1 ={
    "bob":23,
    "charlie":36,
    "Alice":72,
    "eric":18,
    "david":9,
}
dic2 ={
    "oii":23,
    " leo":36,
    " waw":72,
    " yoo":18,
    "hey":9,
}

print(dic1|dic2)
#print({**dic1,**dic2})
#dic3=dic2.copy()
#dic3.update(dic1)
#print(dic3)