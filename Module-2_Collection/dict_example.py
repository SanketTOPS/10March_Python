stdata={'id':101,'name':'nirav','sub':'python'}
print(stdata)
#print(stdata.keys())
#print(stdata.values())
#print(stdata['name'])
#print(stdata.get('sub'))
#print(len(stdata))


"""if 'nirav' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

stdata["id"]=102 #update
stdata["city"]="rajkot" #add
#stdata.pop('sub')
#stdata.clear()
#del stdata
#print(stdata)

newdict=stdata.copy()
print(newdict)
