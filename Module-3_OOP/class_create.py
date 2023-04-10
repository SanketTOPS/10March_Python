class student:
    stid=12
    stnm='Sanket'

    def myfunc(self):
        print("This is student class.")
    
    def getsum(self,a,b):
        print("Sum:",a+b)
        


# Object of class
st=student()
print(st.stid)
print(st.stnm)
st.myfunc()
st.getsum(23,78)
