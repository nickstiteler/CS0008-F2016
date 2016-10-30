# Defining of the variables for total distance and total line number
total_distance = 0
total_line = 0

# Input for the first file
file_name = input('Enter the first file name.')

# Setting the initial case for the while loop
case = True

# While loop for the entire program
while (case):

    # Function for the reading the file
    def processFile(file_name):

        # Opening and reading of the file
        file_name = open(file_name, 'r')

        # Defining the local variables for number of lines and partial distance
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

            # Sets the total distance and total number of lines as global
            global total_distance
            global total_line

            # Addition of the partial distances and the number of lines to find the total of each
            total_distance += partial_distance
            total_line += numline

        # This simply closes the file when it is done being used
        file_name.close()



        # This is the function for printing and allows the print statements to only need formatted once
        def printKV(numline,partial_distance,klen=0):

            # Formatting of the print statements
            KL = max(len(numline),klen)
            if(isinstance(partial_distance,str)):
                FS = '20s'
            elif isinstance(partial_distance,float):
                FS = '10.3f'
            print('Partial Total # of lines:', numline)
            print('Partial distance run', partial_distance)

            print(format(numline,str(KL)+'s'))

            format(partial_distance,FS)


        # Calling the printKV function
        printKV(numline,partial_distance,klen=0)

    # Calling the processFile function
    processFile(file_name)

    # Input for the next file or if the there are none its ends the program by entering quit or q
    file_name = input('Enter the next file, or enter "q" or "quit" if you have no more files.')
    if (file_name == 'quit' or file_name == 'q'):
        case = False

#        printKV('Partial Total Number of lines',numline)

#        printKV('Partial Distance Ran',partial_distance)