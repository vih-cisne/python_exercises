from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)                                 


def clean_ingredients(dish_name, dish_ingredients):

    return dish_name, set(dish_ingredients)
    """
    :param dish_name: str
    :param dish_ingredients: list
    :return: tuple of (dish_name, ingredient set)
    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """



def check_drinks(drink_name, drink_ingredients):

    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:

            return drink_name + ' Cocktail'

    return drink_name + ' Mocktail'
    """
    :param drink_name: str
    :param drink_ingredients: list
    :return: str drink name + ("Mocktail" or "Cocktail")
    The function should return the name of the drink followed by "Mocktail" if the drink has
    no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.
    """

def verifying_category(ingredients, category_data):

    for ingredient in ingredients:
        if ingredient not in category_data:
            return False
    
    return True


def categorize_dish(dish_name, dish_ingredients):
    data = [('VEGAN', VEGAN), ('VEGETARIAN', VEGETARIAN), ('PALEO', PALEO), ('KETO', KETO), ('OMNIVORE', OMNIVORE)]

    for (category_name, category_data) in data:
        if verifying_category(dish_ingredients, category_data):
            return dish_name + ': ' + category_name
    """
    :param dish_name: str
    :param dish_ingredients: list
    :return: str "dish name: CATEGORY"
    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    """


def tag_special_ingredients(dish):
    special_ingredients = []

    for ingredient in dish[1]:
        if ingredient in SPECIAL_INGREDIENTS:
            special_ingredients.append(ingredient)

    return (dish[0], set(special_ingredients))            
    """
    :param dish: tuple of (str of dish name, list of dish ingredients)
    :return: tuple of (str of dish name, set of dish special ingredients)
    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """


def compile_ingredients(dishes):
    compiled_ingredients = []

    for dish in dishes:
        for ingredient in dish:
            compiled_ingredients.append(ingredient)
    
    return set(compiled_ingredients)


    """
    :param dishes: list of dish ingredient sets
    :return: set
    This function should return a `set` of all ingredients from all listed dishes.
    """


def separate_appetizers(dishes, appetizers):
    result = [dish for dish in dishes if dish not in appetizers]

    return list(set(result))

    """
    :param dishes: list of dish names
    :param appetizers: list of appetizer names
    :return: list of dish names
    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """


def singleton_ingredients(dishes, intersection):
    result = []
    
    for dish in dishes:
        for ingredient in dish:
            if ingredient not in intersection:
                result.append(ingredient)
    
    return set(result)


    """
    :param intersection: constant - one of (VEGAN_INTERSECTION,VEGETARIAN_INTERSECTION,PALEO_INTERSECTION,
                                            KETO_INTERSECTION,OMNIVORE_INTERSECTION)
    :param dishes:  list of ingredient sets
    :return: set of singleton ingredients
    Each dish is represented by a `set` of its ingredients.
    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category.
    The function should return a `set` of ingredients that only appear in a single dish.
    """


