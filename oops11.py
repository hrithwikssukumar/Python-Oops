class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = {}  # Dictionary to store subject and grade

    # Method to add or update grades for a subject
    def add_or_update_grade(self, subject, grade):
        if 0 <= grade <= 100:  # Ensure grade is within valid range
            self.grades[subject] = grade
            print(f"Grade for '{subject}' has been added/updated to {grade}.")
        else:
            print("Grade must be between 0 and 100.")

    # Method to calculate GPA
    def calculate_gpa(self):
        if not self.grades:
            print("No grades available to calculate GPA.")
            return 0.0
        total_points = sum(self.grades.values())
        gpa = total_points / len(self.grades)
        return round(gpa, 2)

    # Method to display student details
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print("Grades:")
        for subject, grade in self.grades.items():
            print(f"  {subject}: {grade}")
        print(f"GPA: {self.calculate_gpa()}")


# Example usage
student = Student("Ajay Yadav", 101)

# Adding/updating grades
student.add_or_update_grade("Mathematics", 85)
student.add_or_update_grade("Physics", 90)
student.add_or_update_grade("Chemistry", 88)
student.add_or_update_grade("History", 76)

# Displaying student details
print("\nStudent Details:")
student.display_details()

# Update a grade
print("\nUpdating Grade:")
student.add_or_update_grade("History", 80)

# Display updated details
print("\nUpdated Student Details:")
student.display_details()
