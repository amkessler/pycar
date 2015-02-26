# About variable assignment, data types and comparison operators

# ----- Strings -----
# Create a variable and assign it some string value
my_string = "We're going to learn Python at #NICAR15"

# Print your string
print my_string

# Print the length of your string
print len(my_string)

# Print the data type of your string
print type(my_string)

# Print the lowercase version of your string
print my_string.lower()

# Print the uppercase version of your string
print my_string.upper()

# Print the titlecase version of your string
print my_string.title()

# Print your string concatenated with your string
print my_string + my_string

# ----- Integers -----
# Create a variable and assign it some integer value
my_integer = 10

# Print your integer
print my_integer

# Print the data type of your integer
print type(my_integer)

# Print the sum of your integer plus ten
print my_integer + 10

# Print the sum of your integer minus ten
print my_integer - 10

# Print the product of your integer multiplied by ten
print my_integer * 10

# Print the quotient of your integer divided by ten
print my_integer / 10

# ----- Comparison operators -----
# https://docs.python.org/2/library/stdtypes.html

# With integers ...

# Create two variables, x and y.
# Assign x an integer value of 5.
# Assign y an integer value of 15.
x = 5
y = 15

# Print the Python equivalent of "Is x greater than y?"
print x > y

# Print the Python equivalent of "Is x greater than or equal to y?"
print x >= y

# Print the Python equivalent of "Is x less than y?"
print x < y

# Print the Python equivalent of "Is x less than or equal to y?"
print x <= y

# With mixed types (integer vs. string) ...

# Create two variables, foo and bar.
# Assign foo an integer value of 10.
# Assign bar a string value of "10".
foo = 10
bar = "10"

# Print the Python equivalent of "Is foo equal to bar?"
print foo == bar

# Print the Python equivalent of "Is foo not equal to bar?"
print foo != bar

# Print the Python equivalent of "Is foo equal to bar?"
# In this case, use the int() function to cast bar as an integer
print foo == int(bar)

# ----- Using the built-in len() function -----
# Assign a string value to foo
foo = "2"

# Print the Python equivalent of "Is the length of foo equal to the length of bar?"
print len(foo) == len(bar)

# ----- Lists -----
# Create a list with one string and one integer
my_list = ["We're going to learn Python at #NICAR15", 10]

# Print the value of your list
print my_list

# Print the length of your list
print len(my_list)

# Print the data type of your list
print type(my_list)
