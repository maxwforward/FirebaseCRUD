#======================================================================================================================
# Function for executing CRUD for Firebase Database
#======================================================================================================================
def firebaseCRUD(databaseURL, option):

    # Import Library
    from firebase import firebase

    # Create Firebase Application
    firebase = firebase.FirebaseApplication(databaseURL, None)

    #******************************************************************************************************************
    # Create
    #******************************************************************************************************************
    if option is '1':

        # Create boolean value for loop
        integerEntered = False

        # Initialize variable for number of fields
        numberOfFields = 0

        #--------------------------------------------------------------------------------------------------------------
        # While loop
        #--------------------------------------------------------------------------------------------------------------
        while integerEntered is False:

            # Get number of fields from user input
            numberOfFields = input('Enter the number of fields: ')
            print('\n')

            # Try converting user input to an integer
            try:
                numberOfFieldsInteger = int(numberOfFields)
                integerEntered = True
            # If ValueError occurs, display error message
            except ValueError:
                print('ERROR - Please enter an integer value')
                print('\n')

        # Create a list for the names of each field
        fieldNamesList = [None] * int(numberOfFields)

        # Initialize a counter
        counter = 0

        #--------------------------------------------------------------------------------------------------------------
        # Enter the names of each field
        #--------------------------------------------------------------------------------------------------------------
        for x in fieldNamesList:
            message = 'Enter a name for field #' + str(counter + 1) + ': '
            fieldNamesList[counter] = input(message)
            counter += 1

        # Print a newline
        print('\n')

        # Create a list for the names of each field
        fieldValuesList = [None] * int(numberOfFields)

        # Initialize a counter
        counter = 0

        #--------------------------------------------------------------------------------------------------------------
        # Enter the values for each field
        #--------------------------------------------------------------------------------------------------------------
        for x in fieldValuesList:
            message = "Enter a value for the field '" + str(fieldNamesList[counter]) + "': "
            fieldValuesList[counter] = input(message)
            counter += 1

        # Convert the two lists into a dictionary
        data = dict(zip(fieldNamesList, fieldValuesList))

        # Print a newline
        print('\n')

        # Get the path where the data should be stored from user input
        dataPath = input('Enter the path where the data should be stored in the database: ')

        # Post the data to the database and store the result
        result = firebase.post(dataPath, data)

        # Print a newline
        print('\n')

        # Print the result
        print('Create Result = ', result)

    #******************************************************************************************************************
    # Read
    #******************************************************************************************************************
    elif option is '2':

        # Get the path where data should be read from user input
        dataPath = input('Enter the path in the database where data should be read from: ')

        # Get data from Firebase and store the result
        result = firebase.get(dataPath, '')

        # Print a newline
        print('\n')

        # Print the result
        print('Read Result = ', result)

    #******************************************************************************************************************
    # Update
    #******************************************************************************************************************
    elif option is '3':

        # Get the path of the data to update from user input
        dataPath = input('Enter the path in the database where data should be updated, including the name of the data: ')
        print('\n')

        # Get the name of the field to update from user input
        fieldName = input('Enter the name of the field to be updated: ')
        print('\n')

        # Get the updated value from user input
        message = "Enter a new value for the field '" + fieldName + "': "
        updatedValue = input(message)
        print('\n')

        # Update the data
        firebase.put(dataPath, fieldName, updatedValue)

        # Print message
        print('Record Updated')

    #******************************************************************************************************************
    # Delete
    #******************************************************************************************************************
    elif option is '4':

        # Get the path where data to delete is located from user input
        dataPath = input('Enter the path where data to delete is located in the database: ')
        print('\n')

        # Get the name of the data to delete from user input
        dataDelete = input('Enter the name of the data to delete: ')
        print('\n')

        # Delete the data
        firebase.delete(dataPath, dataDelete)

        # Print message
        print('Record Deleted')
