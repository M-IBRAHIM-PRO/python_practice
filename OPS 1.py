class members:
    numbers_of_children = 4
    pass

papa = members() #THIS BRACKETS ARE NECESSARY ELSE PROGRAM WILL ONLY TAKE THE LAST MEMBERS INFORMATION.
mama = members()
"""this is the members list"""
papa.name = "ALLAH BAKHSH"
papa.profession = "Tecnition"
papa.age = 50
mama.name="RIFFAT NAZ"
mama.profession="House wife"
mama.age=45
print(papa.__sizeof__())#THIS RETURNS THE LENGTH OF INSTANCE VARIABLE.
print(papa.__dict__) #THIS DICT GIVES US THE ALL DETAILS IN LIST FORMAT.
print(papa.__reduce__())#THIS PROVIDES THE MEMORY LOCATION OF OBJECT.
print(papa.__dir__())#ITPROVIDES THE NUMBER OF FUNCTIONS WHICH CAN BE APPLIED ON IT AFTER THE MEMBER.)
print(papa.__getattribute__("name"))
print(mama.__eq__(mama))
mama.__setattr__("age",32)#THIS IS USED FOR REPLACEMENT& FORMAT IS (OB)
print(mama.name)
print(mama.__getattribute__("age"))
print(mama.numbers_of_children)
papa.__setattr__("numbers_of_children",1234)
print(papa.numbers_of_children)
print(members.__dict__)
print("HELLO\tSS")
print("HELLO \nTO UET")