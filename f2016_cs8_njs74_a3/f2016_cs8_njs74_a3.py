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


out_file = open("output.txt",'w')

global_dict = {}

def processfile(file,gd):

    file = open(file,'r')

    count = 0

    partial_distance = 0

    file.readline()

    for line in file:

        line = line.rstrip('\n').split(',')

        key = str(line[0])

        value = float(line[1])

        if(key in gd):
            gd[key] = gd[key]+[(value)]
        else:
            gd[key] = [value]

        count += 1

        partial_distance += value

    file.close()

    return[gd,count,partial_distance]

print('Please enter the name of the master input file to process.')
master = input('Master file name : ')

file = open(master,'r')

files = 0

total_count = 0

total_distance = 0

for line in file:

    line = line.rstrip('\n')

    fh = processfile(line,global_dict)

    files += 1

    total_count += fh[1]

    total_distance += fh[2]

    global_dict.update(fh[0])

max_name = ''
max_dist = 0

for key in global_dict:

    l_values = global_dict[key]

    if(max(l_values)>max_dist):
        max_dist = max(l_values)
        max_name = key

min_name = ''
min_dist = 1000000

for key in global_dict:

    r_values = global_dict[key]

    if(min(r_values)<min_dist):
        min_dist = min(r_values)
        min_name = key

for key in global_dict:





print('')
print('Number of Input files read :',files)
print('Total number of lines read :',total_count)
print('')
print('Total distance run',total_distance)
print('')
print('Max distance run :',max_dist)
print('  by participant :',max_name)
print('')
print('Min distance run :',min_dist)
print('  by participant :',min_name)
print('')
print('Total number of participants :',)
print('Number of participants')
print('with multiple records :',)







