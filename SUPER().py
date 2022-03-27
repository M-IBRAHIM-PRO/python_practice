class A:
    classvar1="THIS IS THE VARIABLE IN \"CLASS A\""
    def __init__(self):
        self.var1="WE ARE INSIDE CONSTRUCTOR OF CLASS A"
        self.classvar1="THIS IS INSTANTANEOUS VARIABLE IN A"
        self.seperate = "THIS INSTANS VAR IS SPECIAL IN A"
class B(A):
    classvar1="THIS IS THE VARIABLE IN \"CLASS B\""
    def __init__(self):
        self.var1 = "WE ARE INSIDE CONSTRUCTOR OF CLASS B"
        self.classvar1 = "THIS IS INSTANTANEOUS VARIABLE IN B"
        super().__init__()
        print(super().classvar1)#THIS WILL CALL THE SUPER CLASS VARIABLE &
        # this is only used to call variable not instance variable\constructors.
#() ARE NECESSARY TO GET ACESS TO THE CONSTRUCTOR.
a= A()
b=B()
#FIRST OF ALL IT WILL SEARCH FOR INSTANCE VARIABLE&THAN IT WILL GO FOR VARIABLE.
print(b.var1,b.seperate,b.classvar1)