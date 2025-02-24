class Employee:
    def __init__(self, emp_id, salary):
        self._id = emp_id          
        self._salary = salary      

    def get_id(self):
        return self._id

    
    def set_id(self, emp_id):
        self._id = emp_id

    
    def get_salary(self):
        return self._salary

    
    def set_salary(self, salary):
        if salary < 0:
            print("Salary cannot be negative.")
        else:
            self._salary = salary



employee = Employee(101, 50000)


print("Employee ID:", employee.get_id())
print("Employee Salary:", employee.get_salary())


employee.set_id(102)
employee.set_salary(55000)


print("Updated Employee ID:", employee.get_id())
print("Updated Employee Salary:", employee.get_salary())

employee.set_salary(-1000)  
