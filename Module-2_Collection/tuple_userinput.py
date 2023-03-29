#data=[]
data=list()

n=int(input("Enter number of elements:"))


for i in range(n):
    x=input("Enter your list value:")
    data.append(x)

#print(data)
print(tuple(data))

