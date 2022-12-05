#Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums to same value (c) whether any value occur in both 
l1 = [1,2,3,4,5]
l2 = [5,6,7,8,9,10]
print("list1:",l1,"list2:",l2)
#a
if len(l1) == len(l2):
    print("Same length.")
else:
    print("not same length.")
    print("length of l1:",len(l1))
    print("length of l2:",len(l2))
    
#b   
if sum(l1) == sum(l2):
    print("Same sum:",sum(l1))
else:
    print("not same sum.")
    print("sum of l1:",sum(l1))
    print("sum of l2:",sum(l2))
    
#c
l = [ i for i in l1 if i in l2]
print("value occur in both:",l)