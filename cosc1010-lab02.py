# Deacon Steiner
# UWYO COSC 1010
# 09/17/24
# Lab 02 
# Lab Section: 11
# Sources, people worked with, help given to: 
# your
# comments
# here

your_variable_here = "CHANGE ME (Unfinished sections)"

## Section ONE

# Complete the following print statement to print out "Hello, COSC1010"
print("Hello, COSC1010") # Should print "Hello, COSC1010"

# Assign the string above to a variable named hello_message and print that variable
hello_message = "Hello, COSC1010" # Assigns "Hello, COSC1010" to variable called hello_message
print(hello_message) # prints the string stored in hello_message

# Assign the string "cowboy joe" to a variable, and print that variable with title casing
horse = "cowboy joe" # Assigns "cowboy joe" to variable called horse
print(horse.title()) # Prints the message stored in horse, with proper title case

# Complete the following f-string print message 
    # You will need to create your own variables and insert them  
    # the final message should read `The University of Wyoming was founded in 1886`
uni_name = "University of Wyoming" # Assigns "University of Wyoming" to variable called uni_name
uni_year = 1886 # Assigns 1886 (as an integer) to variable called uni_name
print(f"The {uni_name} was founded in {uni_year}") # Prints the message with the added variables (concatenated with an f-string)

# Now let's do some math with variables 
    # Create two variables x and y and assign them the values 5 and 10 respectively 
    # Complete the following print statements using your variables
    #All math must be done within the braces in the f-strings
x = 5 # Assigns 5 to variable x (integer)
y = 10 # Assigns 10 to variable y (integer)
# Prints out each operation (I didn't write a specific comment for each operation, code smarter not harder)
print(f"x + y = {x + y}") # Should output 15
print(f"x - y = {x - y}") # Should output -5
print(f"x * y = {x * y}") # Should output 50
print(f"x / y = {x / y}") # Should output 0.5

# String concatenation 
    # Finally we will take a look at string concatenation
    # String concatenation combines two strings together
    # It is done using the + operator
    # Create three variables:
        # first_name, which is your first name 
        # last_name, which is your last name
        # space, which is a space character 
    # Use string concatenation to print out your full name 
first_name = "Deacon" # Assign "Deacon" to variable first_name
last_name = "Steiner" # Assign "Steiner" to variable last_name
space = " " # created a space variable

print(first_name + space + last_name) # Print my full name
