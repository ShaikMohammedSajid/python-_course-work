
for i in range(5):
    for j in range(5):
        print(i+j ,end = " ")
    print()
  

# for changing only in coloumns we take only j:
for i in range(5):
    for j in range(5):
        print(j%2,end = " ")
    print()    

#SUM OF BOTH ROWS AND COLOUMNS WE USE I+J:
#IN THIS BOTH ROWS AND COLOUMNS CHANGE:
for i in range(5):
    for j in range(5):
        print(i+j,end = " ")
    print()  
# IF WE WANT TO PRINT "*" STRAIGHT LIKE 1 AFTER ANOTHER   
for i in range(5):
    for j in range(i+1):
        print("*",end = " ")
    print()          

#FOR PRINT MAX TO MIN "*" WE USE THUS LIKE (5-I)
for i in range(5):
    for j in range(i -1):
        print("*",end =" ")
    print()        