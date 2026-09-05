'''res = [i for i in range(1,11)]
print(res)

n = 12
res = [i for i in range(1,n+1) if n% i ==0]
print(res)

r=[12,34,56,235,1422,535,24,425]
res = [i if i % 2==0 else 0 for i in r]
print(res)

r =[12,34,56],[235,1422],[535,24,425]
res = {j for i in r for j in i if j % 2==0}
print(res)


# set comprehension
res = {i for i in range(1,11)}
print(res)

n = 12
res = {i for i in range(1,n+1) if n% i ==0}
print(res)

r=[12,34,56,235,1422,535,24,425]
res = {i if i % 2==0 else 0 for i in r}
print(res)

r =[12,34,56],[235,1422],[535,24,425]
res = {j for i in r for j in i if j % 2==0}
print(res)'''


'''l = [int(input(f"enter the number -{i+1}:")) for i in range(5)]
print(l)'''

'''l = [str(input(f"Student name - {i +1}:")) for i in range(5)]
print(l)'''

#dict comp
'''names = {input(f"Enter the name-{i+1}:"): int(input("enter the marks:")) for i in range(5)}
print(names)'''

#square of an number
'''res = {i:i*i for i in range(1,11)}
print(res)

#even numbers
res = {i for i in range(1,11)if i %2 == 0}
print(res)'''

#upper names
'''names=["mahesh","rahul","venu","nandu"]
res = [name.upper() for name in names]
print(res)'''

#string lengths
'''names = ["mahesh","rahul","venu","nandu"]
res = [len(name) for name in names]
print(res)'''

#add 10 to every number