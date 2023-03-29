data={"web":['java','python','php'],'mobile':['iOS','Android','Flutter']}

#print(data)

x=list()
y=list()

x.append(data["web"])
y.append(data["mobile"])

#print(x)
#print(y)

for i in x:
    print(i,sep=",")
