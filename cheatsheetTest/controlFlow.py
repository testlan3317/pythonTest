# switch...case
response_code = 201

match response_code:
    
    case 200:
        print('ok')

    case 201:
        print('Created')

    case 300:
        print('Multiple Choices')

    case 307:
        print('Temporary Redirect')
    
    case 404:
        print('404 Not Found')

    case 500 | 502:     # the pipe character allows 
        print('Internal Server Error')


# Matching by the length of an Iterator
today_response = [200, 300, 404, 500]
match today_response:
    case [a]:
        print(f"One reponse today: {a}")
    case [a, b]:
        print(f"Two responses today: {a} and {b}")
    case [a, b, *rest]:
        print(f"All responses: {a}, {b}, and {rest}")

# All responses: 200, 300, [400, 500]


# Matching Builtin Classes
resp_code = "300"
match resp_code:
    case int():
        print('Code is a number')
    case str():
        print('Code is a string')
    case _:
        print('Code is neither a string nor a number')

# Code is a string


# For .... else statement
for i in [1,2,3,4,5]:
    if i == 3:
        break
else:
    print('Only executed when no item is equal to 3')


# Ending a Program with sys.exit()

import sys
while True:
    feedback = input('Type exit to exit: ')
    if feedback == 'exit':
        print(f'You typed {feedback}')
        sys.exit()
        