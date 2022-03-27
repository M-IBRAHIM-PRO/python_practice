#METHOD NUMBER 1
class teachers:
    def print_details(self):
        return f"Name is {self.name}.\nSalary is {self.salary}.\nSubject is {self.sub}.\nDeals with {self.classes} Class"
shakila = teachers()
shakila.name="Shakela Ahmed"
shakila.salary= 34000
shakila.classes="11th,12th"
shakila.sub="Mathematics"
shakila.age=23
print(shakila.print_details())
#METHOD NUMBER 2
class employ:
  def __init__(self, name, salary, subj, classes, ag):
    self.name = name
    self.salary = salary
    self.subject = subj
    self.clas = classes
    self.age = ag
shakil=employ("saleem",33200,"Urdu","9th & 10th",24)
print(shakil.clas)
