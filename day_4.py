
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
