#15. Print out all colors from color-list1 not contained in color-list2.
list1=['red','pink','orange','yellow','purple','green','blue','brown','black']
list2=['red','pink','orange','yellow','purple','green','blue']
l=[i for i in list1 if i not in list2]
print("color not in list2:",l)
