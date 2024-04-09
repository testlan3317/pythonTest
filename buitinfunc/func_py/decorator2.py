# example 2 pass func as parameter

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    # storeing the function in a variable
    greeting = func("""Hi, Iam created by a function passed as an argument.""")
    print(greeting)

greet(shout)
greet(whisper)
