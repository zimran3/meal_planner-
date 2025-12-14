# Rice.py – Meal Planner App
INST 326 group project,  
Rice.py is a Python-based meal planner designed to help users organize their weekly meals and simplify grocery shopping. The application allows users to create meals with ingredients, assign meals to specific days of the week, view a complete weekly plan, and automatically generate a shopping list based on selected meals.

This project was developed as part of the INST 326 Final Group Project and demonstrates object-oriented programming principles, testing with pytest, and clean software design.

# What the Program Does
- Lets the user add meals with a name, meal type, and ingredients
- Stores meals inside a weekly plan (Monday–Sunday)
- Shows the full weekly meal schedule
- Creates a shopping list from all meals added to the plan
- Allows the user to view, update, and clear lists
- Uses multiple classes that work together

# Classes We Created
* Meal
Represents a single meal and its ingredients.
This class stores the meal name, course type (breakfast, lunch, or dinner), and a list of ingredients. It provides methods to add, remove, and count ingredients, as well as update meal information.

* WeeklyPlan
Stores meals assigned to each day of the week.
This class allows meals to be assigned, removed, counted, and cleared for specific days or the entire week.

* ShoppingList
Collects ingredients from the weekly meal plan and creates a grocery list.
This class ensures ingredients are gathered correctly and avoids duplicates.

* MealPlannerApp
Runs the main menu and connects all the other classes.
This class provides a console-based interface that allows the user to interact with the program.
Each class includes eight or more methods, including special methods such as __init__, as required by the project instructions.

# How to Run the Program:
1. Clone the repository from GitHub.
2. Open a terminal in the project directory.
3. Run the program using:
   python meal_planner.py

# Testing the Program
All testing is done using pytest.
To run the tests:
1. Install dependencies:
   pip install -r requirements.txt
2. Run pytest:
   pytest
All tests should pass successfully.

# Project structure: 
meal_planner.py        # Main program and class definitions
test_meal_planner.py   # Pytest test cases
requirements.txt       # Project dependencies
README.md              # Project documentation
.gitignore             # Ignored files and folders

# Team members:
* Maisha Subin
* Zainab Imran
* Shuvanga Timilsina
* Skye Crane 

# Video Presentation
Our final video explains:
The purpose of the project
How the program works
How the classes interact
What we learned while building it

(Link to be added here)


