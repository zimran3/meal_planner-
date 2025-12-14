import pytest
from code import Meal, WeeklyPlan, ShoppingList

# -----------------------------
# Meal tests
# -----------------------------

def test_create_meal():
    meal = Meal("Pasta", "dinner", ["noodles", "sauce"])
    assert meal.name == "Pasta"

def test_add_ingredient():
    meal = Meal("Eggs", "breakfast", [])
    meal.add_ingredient("eggs")
    assert "eggs" in meal.ingredients

def test_remove_ingredient():
    meal = Meal("Salad", "lunch", ["lettuce"])
    assert meal.remove_ingredient("lettuce") is True

def test_remove_missing_ingredient():
    meal = Meal("Soup", "dinner", [])
    assert meal.remove_ingredient("salt") is False

def test_change_meal_course_valid():
    meal = Meal("Toast", "breakfast", [])
    assert meal.change_meal_course("lunch") is True

def test_change_meal_course_invalid():
    meal = Meal("Toast", "breakfast", [])
    assert meal.change_meal_course("snack") is False


# -----------------------------
# WeeklyPlan tests
# -----------------------------

def test_assign_meal_to_day():
    plan = WeeklyPlan()
    meal = Meal("Pizza", "dinner", [])
    plan.assign_meal("Monday", meal)
    assert meal in plan.get_meals("Monday")

def test_clear_day():
    plan = WeeklyPlan()
    meal = Meal("Rice", "dinner", [])
    plan.assign_meal("Tuesday", meal)
    plan.clear_day("Tuesday")
    assert plan.get_meals("Tuesday") == []


# -----------------------------
# ShoppingList tests
# -----------------------------

def test_generate_shopping_list():
    plan = WeeklyPlan()
    meal = Meal("Burger", "dinner", ["bun", "patty"])
    plan.assign_meal("Friday", meal)

    shopping = ShoppingList()
    shopping.generate_from_plan(plan)
    assert "bun" in shopping.items

def test_remove_duplicates():
    shopping = ShoppingList()
    shopping.add_item("milk")
    shopping.add_item("milk")
    shopping.remove_duplicates()
    assert shopping.items == ["milk"]

