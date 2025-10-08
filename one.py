class Employee():
    Name = None
    Post = None
    Salary = None

    def __init__(self, name, post, salary):
        self.Name = name
        self.Post = post
        self.Salary = salary


    def calculate_salary(self):
        return self.Salary*1.5

    def display_info(self):
        salary = self.calculate_salary(self.Salary)
        print("Имя: ", self.Name,"Должность: ", self.Post, "Зарплата: ", salary)

class Developer(Employee):
    Hour = None
    Bet = None
    def __init__(self, Hour, Bet, name, post, salary):
        super(Developer, self).__init__(name, post, salary)
        self.Hour = Hour
        self.Bet = Bet

    def calculate_salary(self, Hour, Bet):
        D_salary = Hour*Bet
        return D_salary

    def display_info(self):
        salary = self.calculate_salary(self.Salary)
        print("Имя: ", self.Name,"Должность: ", self.Post, "Зарплата: ", salary)

class Manager(Employee):
    Worker = None
    def __init__(self, Worker, name, post, salary):
        super(Manager, self).__init__(name, post, salary)
        self.Worker = Worker

    def calculate_salary(self, salary):
        M_salary = salary + salary*0.3
        return M_salary

    def display_info(self):
        salary = self.calculate_salary()
        print("Имя: ", self.Name,"Должность: ", self.Post, "Зарплата: ", salary)


manager = Manager(100, "Ivan", "manager", "1000")
manager.display_info()
