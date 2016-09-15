#
# Template for code submission
# name       : Nicholas Stiteler
# email      : njs74@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Program that asks for the number of cookies wanted and gives you the amount of ingredients needed
# Example: CH 2 EX 10
3
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python

# Intial equation for the input of the number of cookies wanted
c = float(input('Number of cookies wanted'))
# Equation for each individual ingredient
s = 300*c/48
b = 240*c/48
f = 330*c/48
# Printing of the amount of ingredients required
print(s,'grams of sugar,',b,'grams of butter, and',f,'grams of flour')