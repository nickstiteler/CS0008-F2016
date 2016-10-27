
case = True
while (case):

    file_name = input('Enter the file name, or enter "quit" or "q" if you have no more files.')
    def processFile(file_name):
        file_name = open(file_name, 'r')


        numline = 0
        for line in file_name:
            numline +=1
        print(numline)

        total_distance = 0
        for distance in file_name:
            partial_distance = 0
            for distance in file_name:
                partial_distance += file_name.split(',')
            print(partial_distance)
        file_name.close()



    if (file_name == 'quit' or file_name == 'q'):
        case = False


    processFile(file_name)