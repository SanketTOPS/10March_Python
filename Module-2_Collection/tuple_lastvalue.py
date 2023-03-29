data=[[12,23,45],[34,67,8],[12,90,22]]

#print(data)
x=13
for i in data:
    print(i[-1])
    i[-1]=x

print(tuple(data))
