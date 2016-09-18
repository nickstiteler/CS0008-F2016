#
# Template for code submission
# name       : Nicholas Stiteler
# email      : njs74@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Areas of Rectangles
# Example: Starting with Python, Chapter 3, Exercise 2
3
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python


length1 = float(input('Enter First Length'))
width1 = float(input('Enter First Width'))
length2 = float(input('Enter Second Length'))
width2 = float(input('Enter Second Width'))

area1 = length1*width1
area2 = length2*width2

if(area1>area2):
    print('The first rectangle has the greatest area.')
elif(area1<area2):
    print('The second rectangle has the greatest area')
else:
    print('The areas of both rectangles are equal')
