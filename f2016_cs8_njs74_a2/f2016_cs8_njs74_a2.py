
case = True
while (case):

    file_name = input('Enter the file name, or enter "quit", "q", or an "empty string" if you have no more files.')
    def processFile(file_name):
        file_name = open(file_name, 'r')

        partial_distance = 0
        numline = 0
        for line in file_name:
            numline +=1

            line = line.rstip("\n")
            temp = line.split(",")
            distance = float(temp[1])
            partial_distance = distance


        file_name.close()




        def printKV(key, value,klen=0):
            KL = max(len(key),klen)
            if(isinstance(value,str)):
                FS = '20s'
            elif isinstance(value,float):
                FS = '10.3f'

        print(format(key,str(KL)+'s'))

        format(value,FS)


        printKV('Partial Total Number of lines',num_line)

        printKV('Partial Distance Ran',partial_distance)


    processFile(file_name)

    if (file_name == 'quit' or file_name == 'q'):
        case = False