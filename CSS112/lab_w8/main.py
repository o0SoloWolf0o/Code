# Must use the following features
# - Single inhertance Or multiple inhertance
# - Composition
# - Polymorphism
# - __init__()
# - __super__()
# - @classmethod
# - @staticmethod


class Math:

    def addNumbers(x, y):
        return x + y

    def minusNumbers(x, y):
        return x - y

    def multiplyNumbers(x, y):
        return x * y

    def divideNumbers(x, y):
        return x / y


class internship():
    organization = "KMUTT"

    def __init__(self, name, age, salary, idem):
        self.name = name
        self.age = age
        self.salary = salary
        self.idem = idem

    def _showdata(self):
        print("Name", self.getName())
        print("Age", self.getAge())
        print("Salary", self.getSalary)
        print("Id", self.getId)

    def _oneyearincome(self):
        return self.salary * 12

    def setName(self, newname):
        self.name = newname

    def setAge(self, newage):
        self.age = newage

    def setSalary(self, newsalary):
        self.salary = newsalary

    def setId(self, newidem):
        self.idem = newidem

    def setCom(self, org):
        self.organization = org

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getSalary(self):
        return self.salary

    def getId(self):
        return self.idem

    def getCom(self):
        return self.organization


class employee(internship):
    salary = 20000

    def __init__(self, name, age, salary, idem, year):
        self.year = year
        super().__init__(name, age, salary, idem)

    def checkyear1(self):
        y = self.year
        if y >= 5:
            return "You are a employee"
        else:
            return "You are not qualified"
        
    def _oneyearincome(self):
        return self.salary * 12

    def setName(self, newname):
        self.name = newname

    def setAge(self, newage):
        self.age = newage

    def setSalary(self, newsalary):
        self.salary = newsalary

    def setId(self, newidem):
        self.idem = newidem

    def setCom(self, org):
        self.organization = org

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getSalary(self):
        return self.salary

    def getId(self):
        return self.idem

    def getCom(self):
        return self.organization


class long_term_employee(internship):
    salary = 20000

    def __init__(self, name, age, salary, idem, year):
        self.year = year
        super().__init__(name, age, salary, idem)

    def new_salary(cls, salary, year):
        return cls(salary * year)

    def checkyear2(self):
        y = self.year
        if y >= 10:
            return "You are a Long term Employee"
        else:
            return "You are not qualified"

    def _oneyearincome(self):
        return self.salary * 12

    def setName(self, newname):
        self.name = newname

    def setAge(self, newage):
        self.age = newage

    def setSalary(self, newsalary):
        self.salary = newsalary

    def setId(self, newidem):
        self.idem = newidem

    def setCom(self, org):
        self.organization = org

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getSalary(self):
        return self.salary

    def getId(self):
        return self.idem

    def getCom(self):
        return self.organization


class worker():

    def worker(self, worker):
        self.worker = worker


class manager():

    def __init__(self, worker, manager):
        self.manager = manager
        super().__init__(worker)


employee.print_years = classmethod(employee.checkyear1)
long_term_employee.print_years = classmethod(long_term_employee.checkyear2)