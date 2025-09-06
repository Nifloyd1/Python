#---------------------------------LETTER CONVERTER----------------------------------
# this function takes your 'grade_input' and checks what its in the range of to determine what gets printed,
# though it really gets done in the 'MAIN LOOP'
def grade_calc(grade_value):
    if grade_value in range(90, 101):  # checks from 90 to 100
        print("You have an A!")
    elif grade_value in range(80, 90):  # checks from 80 to 89
        print("You have a B!")
    elif grade_value in range(70, 80):  # checks from 70 to 79
        print("You have a C!")
    elif grade_value in range(60, 70):  # checks from 60 to 69
        print("You have a D!")
    elif grade_value in range(0, 60):  # checks from 0 to 59
        print("You have a F!")
    else:  # to handle grades outside 0-100 range
        print("That's not a valid grade.")

#-----------------------------------MAIN LOOP-----------------------------------
# takes your input, makes sure its an INT, sends it up to our func to see what range its in, and gives you a 'quit' option.
while True:
    print(f'\n-----------GRADE CALCULATOR---------------')
    grade_input = input("What is your grade? (enter 'quit' to exit) - ")

    if grade_input.lower() == 'quit': # gives you the 'quit' option.
        print('\nThank You for Using Grade Calculator (Created By Nifloyd)')
        print('\n')
        break
   
    try:
        if '%' in grade_input: # removes the '%' before converting to an int and doesnt run without '%' present
            grade_input = grade_input.replace('%', '')
        
        grade = int(grade_input) # takes 'grade_input', makes sure its an int, and turns it into 'grade' for the range to be checked
        print('\n') # adds a newline before the result for better spacing
        
        grade_calc(grade)  # pass the int 'grade' to the function
    except ValueError:
        print("\nPLEASE INPUT A WHOLE NUMBER!") # if error this will print