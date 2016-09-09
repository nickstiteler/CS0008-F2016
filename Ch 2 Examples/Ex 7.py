#
#Template for code submission
# name       : Nicholas Stiteler
# email      : njs74@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Example: Chapter 2 Excersice 7
3
# This program will take the inputs of miles driven and gallons used and will
# convert them into kilometers driven, liters used, and liters used per 100 kilometers
#
# First the variables are identified by using the inputs of mile driven and liters used
x = float(input('miles driven'))
y = float(input('gallons used'))
# Then the equation are created. k is the conversion mi to km, l is the conversion G to L
# and c is the equation used to find L per 100 km used
k = x/.62137
l = y/.26417
c = (100*y)/x
# The next three lines are just the printing of the solutions
print(k,'km')
print(l,'L')
print(c,'L per 100 km')