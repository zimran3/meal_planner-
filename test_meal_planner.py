import pytest
from meal_planner import Meal, WeeklyPlan, ShoppingList


# =============================
# Meal tests
# =============================

def test_meal_creation():
    meal = Meal("Pasta", "dinner", ["noodles", "sauce"])
    assert meal.name == "Pasta"
    assert meal.meal_course == "dinner"
    assert meal.count_ingredients() == 2


def test_add_and_remove_ingredient():
    meal = Meal("Salad", "lunch", [])
    meal.add_ingredient("lettuce")
    assert "lettuce" in meal.ingredients
    assert meal.remove_ingredient("lettuce") is True
    assert meal.ingredients == []


def test_change_meal_course_valid():
    meal = Meal("Eggs", "breakfast", [])
    assert meal.change_meal_course("lunch") is True


def test_change_meal_course_invalid():
    meal = Meal("Eggs", "breakfast", [])
    assert meal.change_meal_course("snack") is False


# =============================
# WeeklyPlan tests
# =============================

def test_assign_meal_to_day():
    plan = WeeklyPlan()
    meal = Meal("Pizza", "dinner", [])
    result = plan.assign_meal("Monday", meal)
    assert result is True
    assert meal in plan.get_meals_for_day("Monday")


def test_clear_day():
    plan = WeeklyPlan()
    meal = Meal("Rice", "dinner", [])
    plan.assign_meal("Tuesday", meal)
    plan.clear_day("Tuesday")
    assert plan.get_meals_for_day("Tuesday") == []


def test_has_meals():
    plan = WeeklyPlan()
    meal = Meal("Soup", "lunch", [])
    plan.assign_meal("Wednesday", meal)
    assert plan.has_meals("Wednesday") is True


# =============================
# ShoppingList tests
# =============================

def test_add_and_remove_item():
    shopping = ShoppingList()
    shopping.add_item("milk")
    assert shopping.has_item("milk") is True
    assert shopping.remove_item("milk") is True


def test_generate_from_plan_no_duplicates():
    plan = WeeklyPlan()
    meal1 = Meal("Pasta", "dinner", ["noodles", "sauce"])
    meal2 = Meal("Salad", "lunch", ["lettuce", "sauce"])

    plan.assign_meal("Friday", meal1)
    plan.assign_meal("Friday", meal2)

    shopping = ShoppingList()
    shopping.generate_from_plan(plan)

    items = shopping.get_list()
    assert "sauce" in items
    assert items.count("sauce") == 1


def test_clear_shopping_list():
    shopping = ShoppingList()
    shopping.add_item("eggs")
    shopping.clear_list()
    assert shopping.count_items() == 0
