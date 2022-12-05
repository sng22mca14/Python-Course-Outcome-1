startyear = int(input("enter start year :"))
endyear = int(input("enter start year :"))
if(startyear<endyear):
     for i in range (startyear,endyear):
         if(i%4==0 and i%100!=0) or (i%400==0):
             print(i)
             
       
         