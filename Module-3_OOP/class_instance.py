class studinfo:
    stid=12
    stnm="Sanket"

    def printdata(self):
        print("ID:",self.stid)
        print("Name:",self.stnm)

# Object of class
"""st=studinfo()
st.printdata()
st.stid=30
st.stnm="Nirav"
st.printdata()"""

# Instance
studinfo().printdata()
studinfo().stid=22
studinfo().stnm="Ashok"
studinfo().printdata()