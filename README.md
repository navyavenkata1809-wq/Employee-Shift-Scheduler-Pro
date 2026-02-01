# Employee Schedule Management System

---

## Overview

The Employee Schedule Management System is a multi-language project implemented in Python and C++. It is designed to automate workforce scheduling while following defined labor rules and employee preferences. The system helps organizations manage shifts efficiently and fairly.

---

## Project Objective

The main objective of this project is to create an automated scheduling system that assigns employees to shifts in a balanced and conflict-free manner. It ensures that all rules are followed and that employee preferences are considered whenever possible.

---

## Key Features

### Multi-Day Scheduling

* Supports scheduling for a complete 7-day work week.
* Ensures balanced distribution of work across all days.

### Constraint Enforcement

* Maximum of 5 working days per week per employee.
* Maximum of 1 shift per day per employee.
* Minimum of 2 employees per shift.

### Conflict Resolution

* Automatically reallocates employees if their preferred shift is already full.
* Prevents over-allocation and overlapping schedules.

### Priority Logic

* Implements a preference ranking system.
* Attempts to assign employees to their preferred shifts first.
* Improves employee satisfaction and fairness.

---

## Technical Specifications

### Python Implementation

* Programming Paradigm: Object-Oriented Programming (OOP).
* Core Logic: Uses list comprehensions and dictionary mappings for tracking schedules.
* Version Requirement: Python 3.x or above.

### C++ Implementation

* Programming Paradigm: Procedural and Structured.
* Core Logic: Uses Standard Template Library (STL), including std::map and std::vector.
* Version Requirement: C++11 or higher.

---

## Project Structure

* employee_scheduler.py    : Python source file
* scheduler.cpp            : C++ source file
* README.md                : Project documentation

---

## Installation Requirements

### For Python

* Python 3.x installed on the system
* Basic knowledge of command-line usage

### For C++

* GCC compiler (g++) or any C++ compatible compiler
* Support for C++11 standard

---

## How to Run the Project

### Running the Python Version

1. Make sure Python 3 is installed.
2. Open Command Prompt, Terminal, or VS Code terminal.
3. Navigate to the project directory.
4. Run the following command:

       python employee_scheduler.py

### Running the C++ Version

1. Make sure a C++ compiler is installed.

2. Open Command Prompt or Terminal.

3. Navigate to the project directory.

4. Compile the program using:

       g++ scheduler.cpp -o scheduler

5. Run the executable file:

       ./scheduler

---

## Output Description

* Displays the weekly schedule for all employees.
* Shows assigned shifts for each day.
* Indicates reassigned shifts if conflicts occur.

---

## Advantages of the System

* Reduces manual scheduling effort.
* Minimizes human errors.
* Ensures fair workload distribution.
* Improves productivity and planning.

---

## Future Enhancements

* Add a graphical user interface (GUI).
* Integrate database support for data storage.
* Enable real-time schedule updates.
* Add mobile application support.

---

## Author and Credits

Developed as an academic assignment for learning workforce management and scheduling algorithms.

---

## License

This project is intended for educational purposes. It may be modified and reused with proper credit.

---
