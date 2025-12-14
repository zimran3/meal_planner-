# =============================
# Meal Class
# =============================
class Meal:
    """
    Represents a single meal.

    A Meal object stores the name of the meal, the type of course
    (breakfast, lunch, or dinner), and a list of ingredients.
    """

    def __init__(self, name, meal_course, ingredients):
        """
        Initialize a Meal object.

        Args:
            name (str): The name of the meal.
            meal_course (str): The course type (breakfast, lunch, dinner).
            ingredients (list): A list of ingredient strings.
        """
        self.name = name
        self.meal_course = meal_course
        self.ingredients = ingredients

    def __str__(self):
        """
        Return a human-readable string representation of the meal.

        Returns:
            str: A formatted description of the meal.
        """
        return f"{self.name} ({self.meal_course}) - Ingredients: {', '.join(self.ingredients)}"

    def add_ingredient(self, ingredient):
        """
        Add an ingredient to the meal if it is not already present.

        Args:
            ingredient (str): The ingredient to add.
        """
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        """
        Remove an ingredient from the meal if it exists.

        Args:
            ingredient (str): The ingredient to remove.

        Returns:
            bool: True if removed successfully, False otherwise.
        """
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
            return True
        return False

    def count_ingredients(self):
        """
        Count the number of ingredients in the meal.

        Returns:
            int: The number of ingredients.
        """
        return len(self.ingredients)

    def change_meal_name(self, new_name):
        """
        Change the name of the meal.

        Args:
            new_name (str): The new name for the meal.
        """
        self.name = new_name

    def change_meal_course(self, new_course):
        """
        Change the meal course if it is valid.

        Args:
            new_course (str): The new course (breakfast, lunch, dinner).

        Returns:
            bool: True if the course was updated, False otherwise.
        """
        if new_course in ["breakfast", "lunch", "dinner"]:
            self.meal_course = new_course
            return True
        return False

    def get_ingredients_list(self):
        """
        Get a copy of the ingredient list.

        Returns:
            list: A copy of the ingredients.
        """
        return list(self.ingredients)


# =============================
# WeeklyPlan Class
# =============================
class WeeklyPlan:
    """
    Manages meals assigned to each day of the week.

    This class stores meals for all seven days and provides methods
    to assign, remove, and inspect meals for each day.
    """

    def __init__(self):
        """
        Initialize an empty weekly meal plan.
        """
        self.plan = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
            "Sunday": []
        }

    def assign_meal(self, day, meal):
        """
        Assign a meal to a specific day of the week.

        Args:
            day (str): The day of the week.
            meal (Meal): The meal to assign.
        """
        self.plan[day].append(meal)

    def remove_meal(self, day, meal):
        """
        Remove a meal from a specific day.

        Args:
            day (str): The day of the week.
            meal (Meal): The meal to remove.

        Returns:
            bool: True if the meal was removed, False otherwise.
        """
        if meal in self.plan[day]:
            self.plan[day].remove(meal)
            return True
        return False

    def get_meals_for_day(self, day):
        """
        Retrieve all meals assigned to a given day.

        Args:
            day (str): The day of the week.

        Returns:
            list: List of meals for that day.
        """
        return self.plan[day]

    def count_meals_for_day(self, day):
        """
        Count how many meals are assigned to a day.

        Args:
            day (str): The day of the week.

        Returns:
            int: Number of meals for the day.
        """
        return len(self.plan[day])

    def has_meals(self, day):
        """
        Check whether a given day has any meals assigned.

        Args:
            day (str): The day of the week.

        Returns:
            bool: True if meals exist, False otherwise.
        """
        return len(self.plan[day]) > 0

    def clear_day(self, day):
        """
        Remove all meals from a specific day.

        Args:
            day (str): The day to clear.
        """
        self.plan[day] = []

    def clear_week(self):
        """
        Remove all meals from the entire week.
        """
        for day in self.plan:
            self.plan[day] = []

    def get_week_plan(self):
        """
        Retrieve the entire weekly plan.

        Returns:
            dict: Dictionary mapping days to meals.
        """
        return self.plan


# =============================
# ShoppingList Class
# =============================
class ShoppingList:
    """
    Represents a shopping list generated from meals.

    This class collects ingredients from a weekly meal plan
    and ensures there are no duplicates.
    """

    def __init__(self):
        """
        Initialize an empty shopping list.
        """
        self.items = []

    def add_item(self, item):
        """
        Add an item to the shopping list.

        Args:
            item (str): The ingredient to add.
        """
        self.items.append(item)

    def remove_item(self, item):
        """
        Remove an item from the shopping list if it exists.

        Args:
            item (str): The ingredient to remove.

        Returns:
            bool: True if removed, False otherwise.
        """
        if item in self.items:
            self.items.remove(item)
            return True
        return False

    def clear_list(self):
        """
        Remove all items from the shopping list.
        """
        self.items.clear()

    def count_items(self):
        """
        Count how many items are in the shopping list.

        Returns:
            int: Number of items.
        """
        return len(self.items)

    def has_item(self, item):
        """
        Check if an item exists in the shopping list.

        Args:
            item (str): The ingredient to check.

        Returns:
            bool: True if present, False otherwise.
        """
        return item in self.items

    def generate_from_plan(self, weekly_plan):
        """
        Generate the shopping list from a WeeklyPlan object.

        Args:
            weekly_plan (WeeklyPlan): The weekly meal plan.
        """
        self.clear_list()
        for meals in weekly_plan.get_week_plan().values():
            for meal in meals:
                for ingredient in meal.ingredients:
                    if ingredient not in self.items:
                        self.items.append(ingredient)

    def get_list(self):
        """
        Retrieve a copy of the shopping list.

        Returns:
            list: A list of shopping items.
        """
        return list(self.items)


# =============================
# MealPlannerApp Class
# =============================
class MealPlannerApp:
    """
    Console-based application that connects meals,
    weekly planning, and shopping list generation.
    """

    def __init__(self):
        """
        Initialize the Meal Planner application.
        """
        self.meals = []
        self.weekly_plan = WeeklyPlan()
        self.shopping_list = ShoppingList()

    def add_meal(self):
        """
        Create a new meal based on user input and store it.
        """
        name = input("Meal name: ").strip()
        course = input("Meal type (breakfast/lunch/dinner): ").strip().lower()

        if course not in ["breakfast", "lunch", "dinner"]:
            print("Invalid meal type.")
            return

        ingredients = []
        print("Enter ingredients (type 'done' to finish):")
        while True:
            item = input("- ").strip()
            if item.lower() == "done":
                break
            if item:
                ingredients.append(item)

        self.meals.append(Meal(name, course, ingredients))
        print("Meal added successfully.")

    def view_meals(self):
        """
        Display all saved meals.
        """
        if not self.meals:
            print("No meals saved.")
            return

        for i, meal in enumerate(self.meals, start=1):
            print(f"{i}. {meal}")

    def remove_meal(self):
        """
        Remove a meal from the saved meal list.
        """
        self.view_meals()
        try:
            choice = int(input("Choose meal number to remove: "))
            removed = self.meals.pop(choice - 1)
            print(f"Removed meal: {removed.name}")
        except (ValueError, IndexError):
            print("Invalid selection.")

    def assign_meal_to_day(self):
        """
        Assign a selected meal to a specific day of the week.
        """
        day = input("Enter day of the week: ").strip().title()
        self.view_meals()

        try:
            choice = int(input("Choose a meal number: "))
            self.weekly_plan.assign_meal(day, self.meals[choice - 1])
            print("Meal assigned successfully.")
        except (ValueError, IndexError):
            print("Invalid selection.")

    def view_weekly_plan(self):
        """
        Display the full weekly meal plan.
        """
        for day, meals in self.weekly_plan.get_week_plan().items():
            print(f"\n{day}:")
            if not meals:
                print("  No meals assigned.")
            for meal in meals:
                print(f"  - {meal}")

    def generate_shopping_list(self):
        """
        Generate and display the shopping list from the weekly plan.
        """
        self.shopping_list.generate_from_plan(self.weekly_plan)
        print("\nShopping List:")
        for i, item in enumerate(self.shopping_list.get_list(), start=1):
            print(f"{i}. {item}")

    def run(self):
        """
        Run the main application menu loop.
        """
        while True:
            print("\n--- Meal Planner ---")
            print("1. Add meal")
            print("2. View meals")
            print("3. Remove meal")
            print("4. Assign meal to day")
            print("5. View weekly plan")
            print("6. Generate shopping list")
            print("7. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_meal()
            elif choice == "2":
                self.view_meals()
            elif choice == "3":
                self.remove_meal()
            elif choice == "4":
                self.assign_meal_to_day()
            elif choice == "5":
                self.view_weekly_plan()
            elif choice == "6":
                self.generate_shopping_list()
            elif choice == "7":
                print("Goodbye!")
                break
            else:
                print("Invalid option.")


# =============================
# Program Entry Point
# =============================
if __name__ == "__main__":
    app = MealPlannerApp()
    app.run()

