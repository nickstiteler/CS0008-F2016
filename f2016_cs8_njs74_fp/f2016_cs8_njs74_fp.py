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

# defines the class
class Participant:

    # sets the initial variables
    name = "unknown"
    distance = 0
    runs = 0

    # initializer function
    def __init__(self,n,d=0):
        self.name = n
        self.distance = 0
        if(d==0):
            self.runs = 0
        else:
            self.runs = 1
    # function that finds the specific distance and adds it to a list
    def addDistance(self,d):
        if (d > 0):
            self.distance += d
            self.runs += 1
    # adds all the distances together
    def addDistances(self,ld):
        for d in ld:
            self.addDistance(d)

    # returns the total distance run
    def getDistances(self):
        return self.distance

    # returns the name of the participant
    def getName(self):
        return self.name

    # returns the number of runs
    def getRuns(self):
        return self.runs

    # stringify the object
    def __str__(self):
        return str('Name :',format(self.name,'-20s')+'. Distance Run :',format(self.distance,'9.4f')+\
                   '. Runs :'+format(self.runs,'4d'))

    # joins name runs and distance so they can easily be written to the csv file
    def tocsv(self):
        return ','.join([self.name, str(self.runs), str(self.distance)])

# defining of the process file
def processfile(file):

    # creates the output list
    output = []

    # opens the file whithin the master
    file = open(file,'r')

    # for loop for each line of the file
    for line in file:

        # skips the header line
        if "distance" in line:
            continue

        # removes the \n from the line and splits it at the comma
        temp1 = line.rstrip('\n').split(',')

        # appends the name and distance to the dictionary
        try:
            # append record to output list in the form of a dictionary with 2 keys: name and distance
            # remove unwanted spaces from name and convert distance to float
            output.append({'name': temp1[0].strip(' '), 'distance':float(temp1[1])})

        # skips all the improperly formatted lines
        except:
            print('Invalid row : '+line.rstrip('\n'))

    # closes the file
    file.close()

    # returns the dictionary
    return output

# input for the master file
print('Please enter the name of the master input file to process.')
master = input('Master file name : ')

# strips the '\n' from each line and opens the master
files = [file.rstrip('\n') for file in open(master,'r')]

# creates a list of all the records from each file
rawData = sum([processfile(file) for file in files],[])

# finds the number of files read by finding the number of objects in files
num_files = len(files)

# finds the total number of lines read by looking at tge number of objects in rawData
num_lines = len(rawData)

# totals everyones distances to find the total distance ran overall
total_distance = sum([(item['distance']) for item in rawData])

# creates dictionary called participants
participants = {}

for item in rawData:

    # checks if the name is new or already recorded if it is it adds onto it and adds to the accumulator
    if not item['name'] in participants.keys():
        participants[item['name']] = Participant(item['name'])
    participants[item['name']].addDistance(item['distance'])

# sets the max and min distance variables to zero and an empty string for the name
min_distance = { 'name' : None, 'distance': None }
max_distance = { 'name' : None, 'distance': None }

# creates the dictionary appearances
appearances = {}

for name, object in participants.items():
    # get the total distance run by this participant
    distance = object.getDistances()

    # finds the min distance by seeing if this is less than the previous distance
    if min_distance['name'] is None or min_distance['distance'] > distance:
        min_distance['name'] = name
        min_distance['distance'] = distance

    # finds the max distance by checking to see if the new one is greater than the last
    if max_distance['name'] is None or max_distance['distance'] < distance:
        max_distance['name'] = name
        max_distance['distance'] = distance

    # gets the number of appearances of the partcipants
    participant_appearances = object.getRuns()

    # check if we need to initialize this entry
    if not participant_appearances in appearances.keys():
        appearances[participant_appearances] = []
    appearances[participant_appearances].append(name)

# finds the total amount of participants that ran
participant_total = len(participants)

# finds the number of participants that had multiple runs
multi_records = len([1 for item in participants.values() if item.getRuns() > 1])

# creates new file for the outputs
output_file = open("f2016_cs8_njs74_fp.data.output.csv", 'w')

# write header in file
output_file.write('name,records,distance\n')

# writes to the output file
for name, object in participants.items():
    output_file.write(object.tocsv() + '\n')

# closes the out file
output_file.close()



# Function that is used to format the printed outputs to the correct format
def print_kv(key, value, lenkv=30):
    if len(key)>lenkv:
        lenkv = len(key)

    if isinstance(value, float):
        f_str = '010.5f'
    elif isinstance(value, int):
        f_str = '2d'
    else:
        f_str = 's'
    print(format(key, str(lenkv)+'s') + ": " + format(value,f_str))
    return

# prints the outputs
print('')
print_kv('Number of Input files read   ',num_files)
print_kv('Total number of lines read   ',num_lines)
print('')
print_kv('Total distance run           ',total_distance)
print('')
print_kv('Max distance run             ',max_distance['distance'])
print_kv('  by participant             ',max_distance['name'])
print('')
print_kv('Min distance run             ',min_distance['distance'])
print_kv('  by participant             ',min_distance['name'])
print('')
print_kv('Total number of participants ',participant_total)
print('Number of participants')
print_kv('with multiple records        ',multi_records)


# f2016_cs8_fp.data.txt