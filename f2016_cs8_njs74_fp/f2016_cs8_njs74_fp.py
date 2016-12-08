# A customer needs to process a number of text files (called data files) that contain names and distance
# run by study participants. The format of those files is as follows:
# Max,34.23
# Barbara,23.00
# Luka,12.87
# …
# In those files, each row is a comma separated list of 2 values: the first one is the name of the participant
# and the second is the distance that the participant has run.
# The names of the input files are stored one per line in an additional file, called the master input list.
# This file has the following structure:
# <data file 1>
# <data file 2>
# <data file 3>
# …
# Write a program that read the master input list file, retrieves the names of the data files and from each
# one of the data files reads every line, extract name and distance. Once the program has all the data in
# memory, it has to compute the following quantities and informations:
# • number of files read in input
# • total number of lines read
# • total distance run (aka the sum of all the distances loaded from provided files)
# • total distance run for each individual participant
# • individual maximum distance run and by which participant
# • individual minimum distance run and by which participant
# • report if there are any participants that appears more than once, how many times and their
# names
# • total number of participants
# Ver. 1 Page 3 of 5
# CS 0008 – Fall 2016 Final Project Due: 2016/12/15
# The program should provide output on the screen similar to the following:
# Number of Input files read : xx
# Total number of lines read : xx
# total distance run : xxxx.xxxxx
# max distance run : xxxx.xxxxx
# by participant : participant name
# min distance run : xxxx.xxxxx
# by participant : participant name
# Total number of participants : xx
# Number of participants
# with multiple records : xx
# The program should also create an output file reporting name of the participant, how many times their
# name appears in the input files and the total distance run. Each row should be as follows:
# Max,3,124.23
# Barbara,2,65.00
# Luka,1,12.87
# …
# A zip file named f2016_cs8_fp.data.zip is provided with this assignment. It contains the following
# additional files that are to be used to test the final project:
# • f2016_cs8_fp.data.txt: master input list
# • f2016_cs8_fp.data.1.csv: data file 1
# • f2016_cs8_fp.data.2.csv: data file 2
# • f2016_cs8_fp.data.3.csv: data file 3
# The output file mentioned above, that has to be created by the student program, should be named:
# • f2016_cs8_<username>_fp.data.output.csv
# Ver. 1 Page 4 of 5
# CS 0008 – Fall 2016 Final Project Due: 2016/12/15
# In this program, the student should make the best use of everything that has learn so far in this class, reuse
# as much as he/she can from assignment #3, improve upon it and he/she has to use a class named
# participants that has 2 properties:
# • name: name of the participant. String.
# • distance: accumulator for total distance run by the participant. Float.
# • runs: accumulator for the total number of runs run by the participant.
# and, at least, the following methods:
# • addDistance(d)
# add single distance to the distance accumulator and increments runs by 1.
# Argument d is a single float.
# • addDistances(ld)
# add an array of distances to distance accumulator. Argument ld is a list of floats.
# • getDistance()
# get the current value of the distance accumulator.
# • getName()
# get the name of the participant of the current instance
# • __init__ (n,d=0)
# initializer method. set name and initial distance if provided. If initial distance is not specified, it
# should be set to zero
# • __str__()
# stringify method. Returns a string with name, total distance run and how many distances the
# object added, according to the following format:
# Name : xxxxxxxxxxxxxxxxxxx. Distance run : yyyy.yyyy. Runs : zzzz
# where xxxxxxxxxxxxxxxxxxx is a right align string of 20 characters for the name, yyyy.yyyy is the
# total distance run with 9 digits, decimal point and 4 decimals, and zzzz is the number of runs
# with 4 digits, no decimals.


# creates new file for the outputs
output_file = open("f2016_cs8_njs74_fp.data.output.csv",'w')

# declares the global dict
global_dict = {}

# defining of the process file
def processfile(file,gd):

    # opens the file whithin the master
    file = open(file,'r')

    # setting the accumulators
    count = 0
    partial_distance = 0

    # reads the first line of the file so the line name,distance is removed
    file.readline()

    # for loop for each line of the file
    for line in file:

        # removes the \n from the line and splits it at the comma
        line = line.rstrip('\n').split(',')

        # sets the key and the value
        key = str(line[0])
        value = float(line[1])

        # if else for appending to the dictionary if there are multiple names or just one
        if(key in gd):
            gd[key] = gd[key]+[(value)]
        else:
            gd[key] = [value]

        # counts the number of lines in each file
        count += 1

        # sums up the total distance of the file
        partial_distance += value

    # closes the file
    file.close()

    # returns the dictionary, number of lines, and partial distance of each file
    return[gd,count,partial_distance]

# input for the master file
print('Please enter the name of the master input file to process.')
master = input('Master file name : ')

# opens master
file = open(master,'r')

# sets the variables equal to zero
files = 0
total_count = 0
total_distance = 0

# for loop for looping through the master
for line in file:

    # strips master of \n
    line = line.rstrip('\n')

    # calls the process file function
    fh = processfile(line,global_dict)

    # adds the total number of files and adds the total number of lines and distances for each file
    files += 1
    total_count += fh[1]
    total_distance += fh[2]

    # updates the global dictionary
    global_dict.update(fh[0])

# sets the variables for the max value
max_name = ''
max_dist = 0

# for loop for finding the max
for key in global_dict:

    # sets the variable equal to key in global dict
    l_values = global_dict[key]

    # if for findind the max distance and getting the name for that person
    if(max(l_values)>max_dist):
        max_dist = max(l_values)
        max_name = key

# sets variable for min
min_name = ''
min_dist = 1000000

# for loop for finding min
for key in global_dict:

    #sets the variable equal to key in global dict
    r_values = global_dict[key]

    # if for findind the min distance and getting the name for that person
    if(min(r_values)<min_dist):
        min_dist = min(r_values)
        min_name = key

# finds the number of names of all the files
num_names = 0
for key in global_dict:
    num_names += 1

# finds how many multiple records there are
multi_records = 0
for key in global_dict:
    multi = len(global_dict[key])
    if(multi>1):
        multi_records += 1


# writes to the output file
for key in global_dict:
    output_file.write(key+','+str(len(global_dict[key]))+','+str(global_dict[key])[1:-1]+'\n')

# closes the file
file.close

def print_kv(key, value, lenkv=30):
    if len(key)>lenkv:
        lenkv = len(key)

    if isinstance(value, float):
        f_str = '010.5f'
    elif isinstance(value, int):
        f_str = '2d'
    else:
        f_str = 's'
    print(format(key, str(lenkv)+'s') + ": " + format(value, f_str))
    return

class Participant:
    def __init__(self,n,d=0):
        self.name = n
        self.distance = 0
        if(d==0):
            self.runs = 0
        else:
            self.runs = 1
    def addDistance(self,d):
        self.distance += d
        self.runs += 1

    def addDistances(self,ld):
        for d in ld:
            self.addDistance(d)

    def getDistances(self):
        return self.distance


    def getName(self):
        return self.name

    def __str__(self):
        return str('Name :',format(self.name,'-20'),'. Distance Run :',format(self.distance,'-9.4'),' . Runs :',format(self.runs,'4int'))


# prints the outputs
print('')
print_kv('Number of Input files read   ',files)
print_kv('Total number of lines read   ',total_count)
print('')
print_kv('Total distance run           ',total_distance)
print('')
print_kv('Max distance run             ',max_dist)
print_kv('  by participant             ',max_name)
print('')
print_kv('Min distance run             ',min_dist)
print_kv('  by participant             ',min_name)
print('')
print_kv('Total number of participants ',num_names)
print('Number of participants')
print_kv('with multiple records        ',multi_records)

# f2016_cs8_fp.data.txt