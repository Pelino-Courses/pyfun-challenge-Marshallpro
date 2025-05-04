from abc import ABC, abstractmethod
from typing import List, Iterator, Optional

class Name:
    """Descriptor for Name Validation"""
    def __set_name__(self, owner, name):
        self._name = f"_{name}"
    
    def __get__(self, instance, owner):
        return getattr(instance, self._name, None)
    
    def __set__(self, instance, value):
        if not isinstance(value, str) or not value.isalpha():
            raise ValueError("Name must contain only letters")
        setattr(instance, self._name, value)

class Person(ABC):
    """Base class for all persons in the university"""
    first_name = Name()
    last_name = Name()

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
    
    @abstractmethod
    def get_role(self) -> str:
        """Return the role of the person"""
        pass
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(Person):
    """Class representing a student"""
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self._enrollments: List['Enrollment'] = []
    
    def enroll(self, course: 'Course'):
        """Enroll student in a course"""
        enrollment = Enrollment(self, course)
        self._enrollments.append(enrollment)
        course.add_enrollment(enrollment)
    
    def __iter__(self) -> Iterator['Course']:
        """Iterate through student's courses"""
        return (enrollment.course for enrollment in self._enrollments)
    
    def __add__(self, other: 'Student') -> List['Course']:
        """Combine course lists of two students"""
        return list(set(self) | set(other))
    
    def get_role(self) -> str:
        return "Student"

class Instructor(Person):
    """Class representing an instructor"""
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self._courses: List['Course'] = []
    
    def assign_course(self, course: 'Course'):
        """Assign instructor to teach a course"""
        if course not in self._courses:
            self._courses.append(course)
            course.instructor = self
    
    def get_role(self) -> str:
        return "Instructor"

class Course:
    """Class representing a university course"""
    def __init__(self, code: str, title: str):
        self.code = code
        self.title = title
        self.instructor: Optional[Instructor] = None
        self._enrollments: List['Enrollment'] = []
    
    def add_enrollment(self, enrollment: 'Enrollment'):
        """Add an enrollment to the course"""
        if enrollment not in self._enrollments:
            self._enrollments.append(enrollment)
    
    def __iter__(self) -> Iterator[Student]:
        """Iterate through enrolled students"""
        return (enrollment.student for enrollment in self._enrollments)
    
    @classmethod
    def create_lab_course(cls, code: str, title: str) -> 'Course':
        """Factory method for lab courses"""
        print("Creating lab course...")
        return cls(code, title)
    
    @classmethod
    def create_lecture_course(cls, code: str, title: str) -> 'Course':
        """Factory method for lecture courses"""
        print("Creating lecture course...")
        return cls(code, title)
    
    def __str__(self):
        return f"{self.code}: {self.title}"

class Enrollment:
    """Class representing student enrollment in a course"""
    def __init__(self, student: Student, course: Course):
        self.student = student
        self.course = course
    
    def __str__(self):
        return f"{self.student} enrolled in {self.course}"

class TeachingAssistant(Student, Instructor):
    """Class representing a teaching assistant"""
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
    
    def get_role(self) -> str:
        return "Teaching Assistant"

def main():
    # Create people
    stud1 = Student("Emmy", "Marshall")
    stud2 = Student("Olii", "Manzi")
    prof = Instructor("Dr", "Pelin")
    assistant = TeachingAssistant("Emmanuel", "Nshuti")

    # Create courses
    Ent101 = Course.create_lecture_course("Ent101", "Entrepreneurship")
    Math102 = Course.create_lab_course("Math102", "Mathematics for engineers II")

    # Assign instructor
    prof.assign_course(Ent101)
    assistant.assign_course(Math102)

    # Enroll students
    stud1.enroll(Ent101)
    stud2.enroll(Ent101)
    stud1.enroll(Math102)
    assistant.enroll(Math102)  # TA is also a student

    # Display student's courses
    print(f"\n{stud1.first_name}'s Courses:")
    for course in stud1:
        print(f"- {course.title}")

    # Combine course loads
    print("\nCombined course list of Emmy and Olii:")
    combined = stud1 + stud2
    for course in combined:
        print(f"- {course.title}")

    # Display students in a course
    print(f"\nStudents in {Ent101.title}:")
    for student in Ent101:
        print(f"- {student}")

    # Display roles
    print("\nRoles:")
    print(f"{prof}: {prof.get_role()}")
    print(f"{assistant}: {assistant.get_role()}")

if __name__ == "__main__":
    main()