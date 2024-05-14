favorite_languages={
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

alien_0 = {'color':'green','speed':'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
#If there’s a chance the key you’re asking for might not exist, consider
#using the get() method instead of the square bracket notation.

'''
If you leave out the second argument in the call to get() and the key doesn’t
exist, Python will return the value None. The special value None means “no value
exists.” This is not an error: it’s a special value meant to indicate the absence of
a value.
'''

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned.")
for language in favorite_languages.values():
    print(language.title())

#This approach pulls all the values from the dictionary without checking for repeats. 
#That might work fine with a small number of values, but in a poll with a large number of respondents, 
#this would result in a very repetitive list. 
#To see each language chosen without repetition, we can use a set. A "set" is a collection in which each item must be unique:
print("set -- unique")
for language in set(favorite_languages.values()):
    print(language.title())

# Note:You can build a set directly using braces and separating the elements with commas:
languages = {'python', 'ruby', 'python', 'c'}
print(f"type: {type(languages)}" )
print(languages)
