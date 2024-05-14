"""
The asser Statement:
when it encounters an assert statement, Python evaluates the accompanying expression, which is hopefully true. 
If the expression is false, Python raises an AssertionError exception.
Syntax:
  assert Expression [, Arguments]

If the assertion fails, Python use ArgumentExpression as the argument for the AssertionError.
AssertionError can be caught and hadled like any other exception, using try-except statement. 
If they are not handled, they will terminate the program and produce a traceback.

"""

def KelvinToFhrenheit(Temperature):
    assert (Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature-273)*1.8)+32

print(KelvinToFhrenheit(273))
print(int(KelvinToFhrenheit(505.78)))
print(KelvinToFhrenheit(-5))