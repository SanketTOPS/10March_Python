class nirav:
    nid=0
    nsub=''

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.nsub=input("Enter Nirav's Subject:")

class ashok:
    aid=0
    asub=''

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashok's Subject:")

class pratik:
    pid=0
    psub=''

    def p_getdata(self):
        self.pid=input("Enter Pratik's ID:")
        self.psub=input("Enter Pratik's Subject:")

class college(nirav,ashok,pratik):
    def printdata(self):
        print("--------Nirav's Data--------")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)
        print("--------Ashok's Data--------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)
        print("--------Pratik's Data--------")
        print("Pratik's ID:",self.pid)
        print("Pratik's Subject:",self.psub)


cl=college()
cl.n_getdata()
cl.a_getdata()
cl.p_getdata()
cl.printdata()




