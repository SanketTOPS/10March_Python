#fl=open('hello.txt','w')
fl=open('hello.txt','a')

stid=input("Enter ID:")
stnm=input("Enter Name:")

fl.write(stid)
fl.write(stnm)