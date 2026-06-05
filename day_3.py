#Arithmetic Operations
#integers

print("Addition:", 1 +2)
print("Subtraction:", 2 - 1)
print("Multiplication:", 2 * 3)
# Division in python gives a float
print("Division:", 4 / 2)
print("Division:", 6 / 2)
print("Division:", 7 / 2)
# gives without the decimal part
print("Floor Division:", 7 // 2)
print("Modulus:", 3 % 2)              #gives remainder
print("Floor Division:", 7 // 3)
print("Exponentiation:", 3 ** 2)      # means 3 * 3

# Floats
print("Floating number,PI", 3.14)
print("Floating number, gravity", 9.81)

# Complex numbers 
print("Complex number:", 1 + 1j)
print("Multiplication of complex numbers:", (1 + 1j) * (1 - 1j))

#Declaring the varibles at the top

a = 3 # a is variable name and 3 is an integer value assigned 
b = 2 # b is variable name and 2 is an integer value assigned

# Arithmetic operations with variables
total = a + b
diff = a - b
product = a * b
division = a / b
floor_division = a // b
modulus = a % b
exponentiation = a ** b

print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
floor_division = num_one // num_two

# Printing values with labels
print("Total:", total)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
print("Floor Division:", floor_division)

# CAlculating area of a circle 
radius = 5
# two * means exponentiation or power
area_of_circle = 3.14 * radius ** 2
print("Area of circle:", area_of_circle)

# Calculating area of a rectangle
length = 10
width = 5
area_of_rectangle = length * width
print("Area of rectangle:", area_of_rectangle)

print (3> 2) # Greater than
print (3 >= 2) # Greater than or equal to
print (3 < 2) # Less than
print (3 <= 2) # Less than or equal to
print (3 == 2) # Equal to
print (3 != 2) # Not equal to

print(len('mango') == len('avocado')) # False
print(len('mango') != len('avocado')) # True
print(len('mango') < len('avocado')) # True
print(len('milk') == len('meat')) # True
print(len('milk') != len('meat')) # False
print(len('tomato') == len('potato')) # True
print(len('python') > len('dragon')) # False

# Boolean comparisons
print('True == True:', True == True) # True
print('True == False:', True == False) # False
print('False == False:', False == False) # True
print('True != False:', True != False) # True
print('True != True:', True != True) # False
print('False != False:', False != False) # False

#Another way of comparison
print('True is True:', True is True) # True
print('True is False:', True is False) # False
print('False is False:', False is False) # True

print('1 is 1:', 1 is 1) # True
print('1 is not 2:', 1 is not 2) # True
print('A in Asabeneh:', 'A' in 'Asabeneh') # True
print('B in Asabeneh:', 'B' in 'Asabeneh') # False

print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')
print('4 is 2 ** 2:', 4 is 2 ** 2)

print(3 > 2 and 4 > 3) # True
print(3 > 2 and 4 < 3) # False
print(3 > 2 or 4 > 3) # True
print(3 < 2 or 4 < 3) # True
print(not(3 > 2 and 4 > 3)) # False
print(not(3 > 2 and 4 < 3)) # True

print(not True) # False
print(not False) # True
print(not not True) #True 
print(not not False) #False)
    