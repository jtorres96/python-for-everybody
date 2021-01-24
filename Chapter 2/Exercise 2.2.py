# Exercise 2.2: Write a program that uses input to prompt a user for their name and then welcomes them.

# For this we will use the input() function and string concatenation:

name = input("Enter your name: ") # We set the function to ask for the user's name. Keep in mind that the variable will be a string, so if we input a number, it will be stored as a string, and therefore we can't perform any calculations with this...
print ("Hello " + name) # We use the string stored in variable "name" and using string concatenation we print out a welcoming message.

# Pretty simple right? However, this implementation raises a problem: What happens if we need to input data types different from strings? We will see this issue come up in future exercises.
