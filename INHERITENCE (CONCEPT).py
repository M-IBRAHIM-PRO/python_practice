class employee:
    __number_of_medical_leaves=30#THIS__ BEFORE A VARIABLE REPRESENTS A Private DATA& to acess it _class name__name of variable.
    def __init__(self, name,years, salary):
        self.name = name
        self.years = years
        self.salary = salary
    def print_details(self):
        return f"THE EMPLOYEE NAME IS {self.name}.\nHE HAS SPEND {self.years} WITH ORGANIZATION.SALARY IS {self.salary}"
    @classmethod
    def from_dashes(cls, str):
        return cls(*str.split("-"))

class programmers(employee):
    number_of_languages=2
    def __init__(self, name,years, salary,languages):
        self.name = name
        self.years = years
        self.salary = salary
        self.languages=languages
    def print_prog_details(self):
        return f"THE EMPLOYEE NAME IS {self.name}.\nHE HAS SPEND {self.years} WITH ORGANIZATION.SALARY IS {self.salary} " \
               f"\nPROFICIENT IN {self.languages}"

class cool_programmer(programmers):
    number_of_languages = 3
    def __init__(self, name,years, salary,languages,sports):
        self.name = name
        self.years = years
        self.salary = salary
        self.languages=languages
        self.sports = sports
    def print_progc_details(self):
        return f"THE EMPLOYEE NAME IS {self.name}.\nHE HAS SPEND {self.years} WITH ORGANIZATION.SALARY IS {self.salary} " \
               f"\nPROFICIENT IN {self.languages} & \nALSO GOOD IN {self.sports}"
hassan=employee("HASSAN ALI",2,40000)
hassan.name="HASSAN ALI"
hassan.exp_years=2
hassan.salary=40000
ali=employee.from_dashes("ALI AHMAD-7-230000")
ahmed=employee("AHMED HASSAN",2,30000)
print(hassan._employee__number_of_medical_leaves)
print(ali.salary)
print(ali.print_details())
print(hassan.print_details())
ahmer=programmers("AHMER ALI ",4,400000,['PYTHON, C#'])
saad=programmers.from_dashes("SAAD HASSAN-4-20000-[PYTHON, C++]")
print(ahmer.print_prog_details())
print(saad.print_prog_details())#TWO FUNCTIONS ARE USED AT A TIME ONE FROM EMPLOYEE CLASS & SECOND FROM PROGRAMMERS CLASS
danial=cool_programmer .from_dashes("DANAIL JAMES-20-700000-[PYTHON, C++, C SHARP]-[CRICKET, BEDMINTON, SPRINT]")
print(danial.print_progc_details())
