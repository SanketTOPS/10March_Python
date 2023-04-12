class studinfo:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)

class otherstudent(studinfo):
    def getdata(self, id, name):
        return super().getdata(id, name)
    

st=studinfo()
ot=otherstudent()

st.getdata(1,'Sanket')
ot.getdata(2,'Nirav')