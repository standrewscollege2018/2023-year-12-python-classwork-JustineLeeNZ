''' basics of functions - Justine  Lee - 21/2/2023 '''

# ***** define functions ******
def say_hello():
    ''' function eg with no parameters - Justine Lee - 21/02/2023 '''
    print("Hi there!")
 
 
def addition(num1, num2):
    ''' function eg with parameters - Justine Lee - 21/02/2023 '''
    
    # display - The sum of the two numbers is ....
    print(f"The sum of the two numbers is {num1 + num2}")
     
     
     

# **** main program *****
# eg with NO input 
say_hello()

# eg with input (2 parameters)
num_a = int(input("first num:"))
num_b = int(input("second num:"))
addition(num_a, num_b)
