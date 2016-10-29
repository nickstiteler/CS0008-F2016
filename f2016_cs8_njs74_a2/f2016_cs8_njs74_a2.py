
total_distance = 0
total_line = 0

case = True
while (case):

    file_name = input('Enter the file name, or enter "quit", "q", or an "empty string" if you have no more files.')

    def processFile(file_name):
        file_name = open(file_name, 'r')

        partial_distance = 0
        numline = 0
        for line in file_name:


            line = line.rstrip("\n")
            temp = line.split(",")
            distance = float(temp[1])
            partial_distance += distance
            numline += 1

            global total_distance
            global total_line

            total_distance += partial_distance
            total_line += numline

        file_name.close()




        def printKV(key,value,klen=0):
            KL = max(len(key),klen)
            if(isinstance(value,str)):
                FS = '20s'
            elif isinstance(value,float):
                FS = '10.3f'
            printKV('', numline)
            printKV('', partial_distance)

            print(format(key,str(KL)+'s'))

            format(value,FS)




    processFile(file_name)


    if (file_name == 'quit' or file_name == 'q'):
        case = False

#        printKV('Partial Total Number of lines',numline)

#        printKV('Partial Distance Ran',partial_distance)