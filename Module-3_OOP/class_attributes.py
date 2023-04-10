class student:
    stid=0
    stnm=''

    def getdata(self):
        self.stid=input("Enter your ID:")
        self.stnm=input("Enter your Name:")
    
    def printdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)
    
# Object of class
st=student()
st.getdata()
st.printdata()

