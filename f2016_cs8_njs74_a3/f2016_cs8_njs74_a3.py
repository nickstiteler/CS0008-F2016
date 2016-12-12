#
#
# name       : Nicholas Stiteler
# email      : man8@pitt.edu
# date       : 11/18/2016
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
#
# Description:
# This is the third assignment of CS0008
#
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
# one of them reads every line, extract name and distance. Once the program has all the data in memory,
# it has to compute the following quantities and informations:
# • number of files read in input
# • total number of lines read
# • total distance run (aka the sum of all the distances loaded from provided files)
# • total distance run for each individual participant
# • individual maximum distance run and by which participant
# • individual minimum distance run and by which participant
# • report if there are any participants that appears more than once, how many times and their
# names
# • total number of participants
# The program should provide an terminal output similar to the following:
# Number of Input files read : xx
# Total number of lines read : xx
# total distance run : xxxx.xxxxx
# max distance run : xxxx.xxxxx
# by participant : participant name
# CS 0008 – Fall 2016 Assignment #3 Due: 2016/11/18
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
# A zip file named f2016_cs8_a3.data.zip is provided with this assignment. It contains the following
# additional files that are to be used to test assignment #3:
# • f2016_cs8_a3.data.txt: master input list
# • f2016_cs8_a3.data.1.csv: data file 1
# • f2016_cs8_a3.data.2.csv: data file 2
# • f2016_cs8_a3.data.3.csv: data file 3
# The output file mentioned above, that has to be created by the student program, should be named:
# • f2016_cs8_<username>_a3.data.output.csv
# In this program, the student should make the best us of everything that has learn so far in this class:
# functions, for loops, while loops, lists, sets and dictionaries.

# creates new file for the outputs
# MN: respect file naming convention as described in specification/assignment
#out_file = open("output.txt",'w')
out_file = open("f2016_cs8_njs74_a3.output.txt",'w')

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
    # MN: here you are working with the maximum run distance fo the participant and not with the total distance run (the you obtain with sum of all the distances run)
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
    # MN; same as max
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
    out_file.write(key)
    out_file.write(',')
    out_file.write(str(len(global_dict[key])))
    out_file.write(',')
    # MN: you had to print the total distance run 
    #out_file.write(str(global_dict[key])[1:-1])
    out_file.write(str(sum(global_dict[key])))
    out_file.write('\n')

# closes the file
file.close

# prints the outputs
print('')
print('Number of Input files read   :',files)
print('Total number of lines read   :',total_count)
print('')
print('Total distance run           :',total_distance)
print('')
print('Max distance run             :',max_dist)
print('  by participant             :',max_name)
print('')
print('Min distance run             :',min_dist)
print('  by participant             :',min_name)
print('')
print('Total number of participants :',num_names)
print('Number of participants')
print('with multiple records        :',multi_records)







