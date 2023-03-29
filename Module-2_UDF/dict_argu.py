def getdata(data):
    print("ID:",data['id'])
    print("Name:",data['name'])
    print("Subject:",data['sub'])


#getdata({'id':101,'name':'sanket','sub':'python'})

stid=input("Enter ID:")
stnm=input("Enter Name:")
stsub=input("Enter Subject:")

getdata({'id':stid,'name':stnm,'sub':stsub})