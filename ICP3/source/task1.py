#creating a class called employee
class Employee:
    count = 0
#assigning the variables in class
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

    def get_avg_salary(self):
        return 'The Average Salary is {0}'.format(round(self.salary/12, 2))

# creating a child class fulltimeemployee from parent class employee
class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        super().__init__(name, family, salary, department)

#giving inputs to to the classes
emp = Employee("rahul", "Family 1", 15000, "designing")
full_emp = FullTimeEmployee("raja", "Family 2", 20000, "HR")
#printing the averages of the salaries
print(emp.get_avg_salary())
print(full_emp.get_avg_salary())