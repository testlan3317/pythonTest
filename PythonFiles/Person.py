def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

def build_person1(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person1('jimi', 'hendrix', age=27)
print(musician)

"""
we add a new optioinal parameter age to the funciton definition and assign the parameter the special value None, which
is used when a variable has no specific value assign to it. You can think of None as a placeholder value.

In conditional tests, None evaluates to False. If the function call includes a value for age, that value is stored in the
dictionary. 

"""
