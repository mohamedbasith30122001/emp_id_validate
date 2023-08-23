class emp:
  def __init__(self,name,id,gender,dob,bloodgroup,address,mobile,aadhar,salary,exp,location,doj):
    self.name=name
    self.id=id
    self.gender=gender
    self.dob=dob
    self.bldgp=bloodgroup
    self.adrs=address
    self.mobile=mobile
    self.aadhar=aadhar
    self.salary=salary
    self.exp=exp
    self.loc=location
    self.doj=doj

class tcs(emp):
  def display(self):
    print("NAME:",self.name,"\nID:","TCS"+str(self.id),"\nDOB:",self.dob,"\nSALARY:","% .2f" %self.salary,"\nLOCATION:",self.loc)
    print("------------------------------------------------------------------------------------------------------")
class hcl(emp):
  def display(self):
    sal=self.salary//10
    sal=sal-self.salary
    n=self.name.split()
    print("FIRST-NAME:",n[0],"\nSECOND-NAME:",n[1],"\nID:","HCL"+str(self.id),"\nSALARY:",abs(sal),"\nGENDER:",self.gender,"\nBLOOD GROUP:",self.bldgp,"\nDOJ:",self.doj)
    print("----------------------------------------------------------------------------------------------------- ")
class infy(emp):
  def display(self):
    print("NAME:",self.name,"\nID:","INFY"+str(self.id),"\nANNUAL SALARY:",(self.salary)*12,"LPA","\nEXPERINCE:",self.exp,"\nMOBILE:",self.mobile,"\nAADHAR NUM:",self.aadhar,"\nADDESS:",self.adrs)
    print("----------------------------------------------------------------------------------------------------- ")
