
total_distance = 0
total_line = 0

file_name = input('Enter the first file name.')

case = True
while (case):



    if (file_name == 'quit' or file_name == 'q'):
        case = False
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
            print('', numline)
            print('', partial_distance)

            print(format(key,str(KL)+'s'))

            format(value,FS)



        printKV(key,value,klen=0)
    processFile(file_name)

    file_name = input('Enter the next file, or enter "q" or "quit" if you have no more files.')
    if (file_name == 'quit' or file_name == 'q'):
        case = False

#        printKV('Partial Total Number of lines',numline)

#        printKV('Partial Distance Ran',partial_distance)