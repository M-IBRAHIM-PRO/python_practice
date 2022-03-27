class sales_man:
    def __init__(self,name,salary,sales_rupess):
        self.name=name
        self.salary=salary
        self.sales=sales_rupess
    @classmethod
    def from_dashes(cls, string):
        params=string.split("-")
        print(params)
        return cls(params[0],params[1],params[2])
rohan=sales_man("ROHAN",23000,100000)
salim=sales_man("SALIM","34000","120000")
danish = sales_man.from_dashes("DANISH AHMED-22300-300000")
print(danish.salary)
class programmers:
    def __init__(self,name,salary,specs):
        self.name=name
        self.salary=salary
        self.specs=specs
    @classmethod
    def from_slashes(cls , str):
        return cls(*str.split("/"))
rohan=programmers("ROHAN SAHIL",33000,"WEB DEVELOPMENT")
harry=programmers("HARIS",1200000,"ALL_ROUNDER")
danish=programmers.from_slashes("DANISH ALI/200000/DEVOPS ENGINEER")
print(f"1",rohan.specs)
print(f"2",harry.specs)
print(f"3",danish.specs)