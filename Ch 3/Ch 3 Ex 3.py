#
# Template for code submission
# name       : Nicholas Stiteler
# email      : njs74@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Age Classifier
# Example: Starting with Python, Chapter 3, Exercise 3
3
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# input for the age of the person
age = float(input('Enter the age of the person'))

# if statements and printing of the age classification of the person
if(age<=1):
    print('The person is an infant')
elif(age>1 and age<13):
    print('The person is a child')
elif(age>=13 and age<20):
    print('The person is a teenager')
else:
    print('The person is an adult')
