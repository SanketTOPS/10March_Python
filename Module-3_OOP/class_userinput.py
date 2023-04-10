class studInfo:
    stid=0
    stnm=""

    def getdata(self):
        self.stid=input("Enter ID:") #new
        self.stnm=input("Enter Name:") #new
    
    def printdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)
    
st=studInfo()
st.getdata()
st.printdata()