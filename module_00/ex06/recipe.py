cookbook = {'sandwich':
            {'ingredients': ['ham', 'bread', 'cheese', 'tomator'],
             'meal': 'lunch',
             'prep_time': 10},
            'cake':
            {'ingredients': ['flour', 'sugar', 'eggs'],
             'meal': 'dessert',
             'prep_time': 60},
            'salad':
            {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
             'meal': 'lunch',
             'prep_time': 15}}


def print_recipe(recipe_name):
    if recipe_name not in cookbook:
        print("\nThis recipe doesn't exist.")
        return -1
    recipe = cookbook[recipe_name]
    print(f"""\nRecipe for {recipe_name}:
Ingredients list: {recipe['ingredients']}
To be eaten for {recipe['meal']}.
Takes {recipe['prep_time']} minutes of cooking.""")


def delete_recipe(recipe_name):
    ret = cookbook.pop(recipe_name, -1)
    if (ret == -1):
        print("\nThis recipe doesn't exist.")
        return -1
    else:
        print(f"""\n{recipe_name} has been deleted.""")


def add_recipe(recipe_name, ingredients, meal, prep_time):
    cookbook[recipe_name] = {'ingredients': ingredients,
                             'meal': meal,
                             'prep_time': prep_time}


def print_cookbook():
    if (len(cookbook) == 0):
        print("\nThe cookbook is empty. Add a new recipe !")
    else:
        print("\nIn this cookbook you will find recipes for:")
        for recipe in cookbook.keys():
            print(f"""  - {recipe}""")


prompt = "\nPlease select an option by typing the corresponding number:\n\
1: Add a recipe\n\
2: Delete a recipe\n\
3: Print a recipe\n\
4: Print the cookbook\n\
5: Quit\n>> "

while (1):
    print(prompt, end='')
    user_input = input()
    if (user_input == "1"):
        print("\nPlease enter the new recipe name:\n>> ", end='')
        recipe_name = input()
        if recipe_name == "":
            print("\nA recipe has to have a name !")
            continue
        if recipe_name in cookbook:
            print("\nThis recipe already exist, its content will be updated.")
        print("\nWhat are the new recipe ingredients ? \
(separated by a comma):\n>> ", end='')
        ingredients = input()
        ingredients = ingredients.split(',')
        print("\nWhat type of meal is it ? \
(breakfast, lunch, dinner, dessert ...):\n>> ", end='')
        meal = input()
        print("\nHow long does it take to prepare ? \
(in minutes):\n>> ", end='')
        prep_time = input()
        add_recipe(recipe_name, ingredients, meal, prep_time)
        print(f"""\n{recipe_name} has been added to the cookbook !""")

    if (user_input == "2"):
        print("\nEnter the recipe's name you want to erase:\n>> ", end='')
        user_input = input()
        delete_recipe(user_input)
    elif (user_input == "3"):
        print("\nEnter the recipe's name to get its details:\n>> ", end='')
        user_input = input()
        print_recipe(user_input)
    elif (user_input == "4"):
        print_cookbook()
    elif (user_input == "5"):
        print("\nCookbook closed.")
        break
    else:
        print("\nThis option does not exist,\
please type the corresponding number.\n\
To exit, enter 5.")
