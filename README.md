[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/1FUBMkxR)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19390759)
# pyfun-challenges-2025

## [Instructions](https://github.com/Pelino-Courses/pyfun-challenges-2025/blob/main/INSTRUCTIONS.md)

## Question 1: Package Management
**Scenario:** You're starting a new project that needs to handle date manipulations. Rather than writing date arithmetic from scratch, you need to utilize an existing package.

**Task:** Write Python code that:
1. Imports the `datetime` module
2. Creates a function to calculate the difference between two dates in days
3. Includes proper docstrings with examples
4. Handles potential errors when invalid date formats are provided

## Question 2: Custom Functions with Default Arguments
**Scenario:** You're building a text processing utility for your team. You need a function that formats text by adding prefixes, suffixes, and applying various transformations.

**Task:** Create a function called `format_text` that:
1. Takes a string input as a required argument
2. Has optional parameters with default values for:
   - `prefix` (default: "")
   - `suffix` (default: "")
   - `capitalize` (default: False)
   - `max_length` (default: None)
3. Returns the formatted text according to the parameters
4. Includes comprehensive docstrings with examples
5. Validates inputs and raises appropriate exceptions with custom error messages

## Question 3: Functions with Arbitrary Arguments
**Scenario:** You're creating a command-line calculator that needs to handle an arbitrary number of inputs and operations.

**Task:** Develop a set of functions that:
1. Implements a `calculate` function that accepts any number of positional arguments and keyword arguments
2. Positional arguments are numbers to be calculated
3. Keyword arguments represent operations to apply (e.g., `add=True`, `multiply=True`)
4. Includes proper error handling for invalid inputs
5. Features comprehensive docstrings explaining usage
6. Creates a helper function using `*args` and `**kwargs` to process the inputs

## Question 4: Basic OOP Implementation
**Scenario:** You're designing a simple inventory management system for a small shop. The system needs to track products, their quantities, and prices.

**Task:** Create a class structure that:
1. Defines a `Product` class with appropriate attributes (name, price, quantity)
2. Implements methods for:
   - Adding and removing inventory
   - Calculating total value of a product (price × quantity)
   - Displaying product information
3. Includes proper validation for inputs (e.g., price and quantity cannot be negative)
4. Features comprehensive docstrings for the class and its methods
5. Implements appropriate error handling

## Question 5: Inheritance and Method Overriding
**Scenario:** You're building a library of geometric shapes for a graphics application. You need to create a hierarchy of shapes with shared and specific behaviors.

**Task:** Develop a class hierarchy that:
1. Creates a base `Shape` class with common attributes and methods
2. Implements specific shape classes (`Circle`, `Rectangle`, `Triangle`) that inherit from `Shape`
3. Overrides methods appropriately for each shape (e.g., area calculation)
4. Implements proper validation in each class's `__init__` method
5. Includes a `__str__` method for human-readable representation of each shape
6. Uses class methods where appropriate
7. Documents all classes and methods with comprehensive docstrings

## Question 6: Advanced OOP with Multiple Inheritance and Custom Iterators
**Scenario:** You're developing a simulation system for a university that needs to track students, courses, and enrollments. The system needs to handle complex relationships and provide various ways to access and iterate through the data.

**Task:** Create a comprehensive OOP solution that:
1. Implements multiple classes with appropriate inheritance:
   - `Person` as a base class
   - `Student` and `Instructor` classes that inherit from `Person`
   - `Course` class that contains information about a course
   - `Enrollment` class to track student-course relationships
2. Uses multiple inheritance to create a `TeachingAssistant` class (both `Student` and has some `Instructor` capabilities)
3. Implements custom iterators for:
   - Iterating through a student's courses
   - Iterating through enrolled students in a course
4. Overloads operators where appropriate (e.g., `+` to combine course loads)
5. Implements proper type hints throughout the codebase
6. Creates abstract base classes where appropriate
7. Uses descriptors to validate and control access to critical attributes
8. Includes comprehensive exception handling
9. Features factory methods for creating different types of courses
