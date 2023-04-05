# Animal is-a object     # ## ?? 是注释填空，你要在后面填上正确的is-a 和has-a 的正确概念
class Animal(object):
    pass

# Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        # Dog has-a name
        self.name = name

# Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name

# Person is-a object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

## ?? Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ?? Employee has-a salary
        self.salary = salary

## ?? Fish is-a object
class Fish(object):
    pass

## ?? Salmon is-a fish
class Salmon(Fish):
    pass

## ?? Halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a dog  #与第一行是不是相反？？  应该是Dog is-a Rover ??
rover = Dog("Rover")

##??  Satan is-a Cat
satan = Cat("Satan")

##??  Mary is-a person
mary = Person("Mary")

##??  Mary's pet is-a satan
mary.pet = satan

##?? Employee's frank is-a 12000
frank = Employee("Frank", 12000)

##??  Frank's pet is-a rover
frank.pet = rover

##  Fish has-a flipper
flipper = Fish()

##?? Salmon has-a crouse
crouse = Salmon()

##??  Halibut has-a harry
harry = Halibut()
