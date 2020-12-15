# Import function from other file
from firebaseCRUD import firebaseCRUD

# Print message
print('\n')
print('Welcome to the Python Firebase Application!')
print('\n')

# Get database URL from user input
databaseURL = input('Please enter the database URL: ')
print('\n')

# Create boolean value for loop
exitProgram = False

#======================================================================================================================
# While loop
#======================================================================================================================
while exitProgram is False:

    # Select Option
    print('Which action would you like to perform on the database?')
    print('1 - Create')
    print('2 - Read')
    print('3 - Update')
    print('4 - Delete')
    print('5 - Exit')
    option = input()

    # Perform selected option
    if option in {'1', '2', '3', '4'}:
        print('\n')
        firebaseCRUD(databaseURL, option)
        print('\n')
    elif option is '5':
        exitProgram = True
    # Display error message if user selects invalid option
    else:
        print('\n')
        print('ERROR - Please enter a number corresponding to the action you would like to perform ')
        print('\n')