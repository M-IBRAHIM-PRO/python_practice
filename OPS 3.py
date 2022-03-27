class employ:
    employ_ID=1232#the variable name must match
    def __init__(self, name, salary, subj, classes, ag):
            self.name = name
            self.salary = salary
            self.subject = subj
            self.clas = classes
            self.age = ag
    @classmethod
    def change_employ_ID(cls,new_ID):
        cls.employ_ID=new_ID
        # the variable name must match(employ_ID)
shakil = employ("saleem", 33200, "Urdu", "9th & 10th", 24)
harry = employ("ali",23000,"languages","B.A",34)
print(harry.employ_ID)
harry.change_employ_ID(2232)
print(shakil.clas)
print(shakil.employ_ID)
harry.change_employ_ID(3413)#This will be the name of function
#This will change the value for all the objects in the class.
print(harry.employ_ID)
print(shakil.employ_ID)