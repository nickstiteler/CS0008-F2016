#
# MN: header with user, instructor and course info is missing
#


#
# MN: here is where you should have defined the function
# Function for the reading the file
def processFile(file_name):

    # Opening and reading of the file
    file_name = open(file_name, 'r')

    # Defining the local variables for number of lines and partial distance#
    partial_distance = 0
    numline = 0

    # For loop for determining the number of lines and the distance in the file
    for line in file_name:

        # This strips the file of \n
        line = line.rstrip("\n")

        # This splits the file into two columns to be read
        temp = line.split(",")

        # This only allows for the distance no the name to be read
        distance = float(temp[1])

        # This allows for the addition of the distances and the number of lines
        partial_distance += distance
        numline += 1

        # MN: DO NOT USE globals unless it is really necessary
        # Sets the total distance and total number of lines as global
        #global total_distance
        #global total_line

        # MN: you do not this here
        #     specification requested that you passed back partial number of lines and distance for the file
        # Addition of the partial distances and the number of lines to find the total of each
        #total_distance += partial_distance
        #total_line += numline

    # This simply closes the file when it is done being used
    file_name.close()

    # MN: here you processed all the line sin your file
    #     so partial_distance and numline have the quantities that you need to pass back
    return numline, partial_distance
# end function processFile

# MN: here is where you should have defined the function
# MN: also the parameters passed in assume the wrong functionality based on their names
# This is the function for printing and allows the print statements to only need formatted once
#def printKV(numline,partial_distance,klen=0):
def printKV(key, value, klen=0):

    # Formatting of the print statements
    KL = max(len(key),klen)
    if(isinstance(value,str)):
        FS = '20s'
    elif isinstance(value,float):
        FS = '10.3f'
    # MN: where is the conditional branch for integers
    elif isinstance(value,int):
        FS = '10d'
    # MN: we need to take care of the case where the value is none of the above
    else:
        FS = '20s'

    # MN: this function should be a generalization for printing
    #     you should not hardcode which qunatities you are printing
    #print('Partial Total # of lines:', numline)
    #print('Partial distance run', partial_distance)

    print(format(key,str(KL)+'s') + ' : ' + format(value,FS))

    # MN: not sure what are the next 2 statements are for
    #print(format(numline,str(KL)+'s'))
    #format(partial_distance,FS)
# end function printKV


# Defining of the variables for total distance and total line number
total_distance = 0
total_line = 0

# Input for the first file
file_name = input('Enter the first file name.')

# Setting the initial case for the while loop
case = True

# While loop for the entire program
while (case):

    #
    # MN: why do you define this function within a loop
    #     a function should be defined only once and possibly never in a loop
    #     Please where I moved the function definition
    # MN: specification required to pass a file handle/object to the processfile function
    # Function for the reading the file
#    def processFile(file_name):
#
#        # Opening and reading of the file
#        file_name = open(file_name, 'r')
#
#        # Defining the local variables for number of lines and partial distance
#        partial_distance = 0
#        numline = 0
#
#        # For loop for determining the number of lines and the distance in the file
#        for line in file_name:
#
#            # This strips the file of \n
#            line = line.rstrip("\n")
#
#            # This splits the file into two columns to be read
#            temp = line.split(",")
#
#            # This only allows for the distance no the name to be read
#            distance = float(temp[1])
#
#            # This allows for the addition of the distances and the number of lines
#            partial_distance += distance
#            numline += 1
#
#            # Sets the total distance and total number of lines as global
#            global total_distance
#            global total_line
#
#            # Addition of the partial distances and the number of lines to find the total of each
#            total_distance += partial_distance
#            total_line += numline
#
#        # This simply closes the file when it is done being used
#        file_name.close()


        # MN: with this indentation, you are defining the function printKV within the function processFile
        #     which is defined within the while loop.
        #     it needs to be defined outside the loop and outside the other function, at least in this case
        # This is the function for printing and allows the print statements to only need formatted once
#        def printKV(numline,partial_distance,klen=0):
#
#            # Formatting of the print statements
#            KL = max(len(numline),klen)
#            if(isinstance(partial_distance,str)):
#                FS = '20s'
#            elif isinstance(partial_distance,float):
#                FS = '10.3f'
#            print('Partial Total # of lines:', numline)
#            print('Partial distance run', partial_distance)
#
#            print(format(numline,str(KL)+'s'))
#
#            format(partial_distance,FS)

        # MN: this call to printKV does not respect the specifications
        # Calling the printKV function
        #printKV(numline,partial_distance,klen=0)

    # MN: this call is wrong because we need to save the 2 quantities that the function return
    # Calling the processFile function
    #processFile(file_name)
    partial_numline, partial_distance = processFile(file_name)

    # MN: update totals
    total_distance += partial_distance
    total_line += partial_numline

    # MN: print partials
    printKV('Partial number of lines',partial_numline)
    printKV('Partial total distance',partial_distance)

    # Input for the next file or if the there are none its ends the program by entering quit or q
    file_name = input('Enter the next file, or enter "q" or "quit" if you have no more files.')
    if (file_name == 'quit' or file_name == 'q'):
        case = False

#        printKV('Partial Total Number of lines',numline)
#        printKV('Partial Distance Ran',partial_distance)

# MN: once you exit the while loop you need to print the totals
printKV('Total Number of lines',total_line)
printKV('Total Distance Ran',total_distance)

