# Positional Arguments
# when you call a function, Python must match each argument in the function call with a parameter in the function definition.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# Keyword Arguments
# Keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the
# arguments, so when you pass the argument to the function, there's no confusion 

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster')

# Default values:
# when writing a function, you can define a default value for each parameter. 

def describe_pet1(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


