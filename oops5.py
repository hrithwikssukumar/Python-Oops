class Employee:
    def __init__(self, emp_id, salary):
        self._id = emp_id          # Private attribute for employee ID
        self._salary = salary      # Private attribute for employee salary

    # Getter for _id
    def get_id(self):
        return self._id

    # Setter for _id
    def set_id(self, emp_id):
        self._id = emp_id

    # Getter for _salary
    def get_salary(self):
        return self._salary

    # Setter for _salary
    def set_salary(self, salary):
        if salary < 0:
            print("Salary cannot be negative.")
        else:
            self._salary = salary


# Example usage
employee = Employee(101, 50000)

# Accessing private attributes using getter methods
print("Employee ID:", employee.get_id())
print("Employee Salary:", employee.get_salary())

# Modifying private attributes using setter methods
employee.set_id(102)
employee.set_salary(55000)

# Accessing updated values
print("Updated Employee ID:", employee.get_id())
print("Updated Employee Salary:", employee.get_salary())

# Attempting to set a negative salary
employee.set_salary(-1000)  # This will show a warning
