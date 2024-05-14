## Passing in Arbitrary Number of Arguments

def make_pizza(*toppings):
    """print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Sometimes you won't know ahead of time how many arguments a function needs to accept. Fortunately, Python allows a function
# to collect an arbitrary number of arguments from the calling statement.

# The asterisk (*) in the parameter name "*toppings" tell Python to make an empty "tuple" called "toppings" and pack whatever
# values it receives into this tuple.

# Mixing Positional and Arbitrary Arguments

def make_pizza1(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza1(16, 'pepperoni')
make_pizza1(12, 'mushrooms', 'green peppers', 'extra cheese')

## Using Arbitrary Keyword Arguments:
# Sometimes you will want to accept an arbitrary number of arguments, but you won't know ahead of time what kind of information
# will be passed to the function. 
# In this case, you can write functions that accept as many key-value pairs as the calling statement provides.
# One example involves building user profiles: you know you'll get information about a user, but you're not sure what kind of
# information you'll receive. 

def build_profile(first,last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                                location='princeton',
                                field='physics')
print(user_profile)

# The double asterisks(**) before the parameter **user_info cause Python to create an empty dictionary called "user_info" and pack whatever name-value
# pairs it receives into this dictionary.
# within the function, you can access the key-value pairs in user_info just as you would for any dictionary.

"""
Storing Your functions in Modules:
You can go a step further by storing your functions in a separate file called a "module" and then "importing" that module
into your main program.

1. import an Entire Module
    import module_name

using as to Give a module an Alias
    import module_name as md
    
    import pizza as p
    p.make_pizza(16, 'pepperoni')
    
2. import specific Functions
    from module_name import function_name

using as to Give a Function an Alias
    from module_name import function_name as fn

    from pizza import make_pizza as mp
    mp(16, 'pepperoni')
    
3. import All Functions in a Module
    from pizza import *
    make_pizza(16, 'pepperoni')


"""