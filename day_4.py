
# Single line comment
letter ='P'            # A string could be a single character or a bunch of text
print(letter)
print(len(letter))
greeting = 'Hello, World!'
print(greeting)
print(len(greeting))
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

# Multiline String 
multiline_string = ''' I am a Salon Operator and Braider, I have been
in the industry for 20 years. I have a passion for learning and 
teaching people how to braid hair.'''
print(multiline_string)
multiline_string = """I am a Salon Operator and Braider, I have been
in the industry for 20 years. I have a passion for learning and 
teaching people how to braid hair"""
print(multiline_string)

# String Concaneation 
first_name = ' Stackx '
last_name = 'Codex '
space = ' '
full_name = first_name + space + last_name
print(full_name)
# Check length of string using len() built in functions 
print(len(first_name))
print(len(last_name))
print(len(full_name) > len(last_name))
print(len(full_name))

# Unpacking characters in a string 
language = 'Python'
a, b, c, d, e, f = language
print(a) 
print(b)
print(c)
print(d)
print(e)
print(f)

# Accessing characters in a string be index
language = 'Python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
third_letter = language[2]
print(third_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)

#If we want to start from the right and we can use negative indexing, -1 is the last index
language + "Python"
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)

#Slicing
language = 'Python'
first_three = language[0:3]
print(first_three)
last_three = language[-3:6]
print(last_three)

# Skipping characters while slicing
language = 'Python'
pto = language[0:6:2]
print(pto)

# Escape sequences
print(' hope everyone is enjoying the python challenge.\n Do you?')
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5') 
print('Day 4\t3\t5')
print('This is a back slash symbol (\\)')
print('In every pragmming language it starts with \"Hello, World!\"')

# String Methods
# capitalization(): Converts the first character of the string into Capital letter
challenge = 'thirty days of python'
print(challenge.capitalize())

# count(): returns occurences of substring in a string, count(subsstring, start=.., end=..)
chanllenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))

# endswith(): Checks if a string ends with a specified ending 
challenge = 'thirty days of python'
print(challenge.endwith('on'))
print(challenge.endwith('tion'))

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument 
challenge = 'thirty\tdays\yof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))

# find(): Return the index of the first occurence of substring 
challenge(challenge.find('y'))
print(challenge.find('th'))

# format() Formats string into nicer output 
first_name = 'Stackx'
last_name = 'Codex'
job = 'Salon Operator and Braider'
country = 'USA'
sentence = 'I am {} {}. I am a {}. I live in {}. '.format(
    first_name ,last_name, job, country)
print(sentence)

radius = 10
pi = 3.14 
area = pi # radius ## 2
result = 'The area of a circle with {} is {}'.format(str(radius), str(area))
print(result)

#indexing(): Returns the index of substring 
challenge ='thirty days of python'
print(challenge.find('y'))
print(challenge.find('th'))

# isalnum(): Checks alphanumeric characters 
challenge = 'ThityDaysofPython' 
print(challenge.isalnum())

