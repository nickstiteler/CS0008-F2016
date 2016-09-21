#
# Template for code submission
# name       : Nicholas Stiteler
# email      : njs74@pitt.edu
# date       :
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Roman Numerals
# Example: Starting with Python, Chapter 3, Exercise 4
3
# Notes:
# any notes to the instructor and/or TA goes here
# ...and now let's program with Python


number = input('Enter a number one through ten')

number=int(number)

if not(number>=1 and number<=10):
    print("error enter a number one to ten")
    exit
elif(number==1):
    print("The Roman Numeral is 'I'")
elif(number==2):
    print("The Roman Numeral is 'II'")
elif(number==3):
    print("The Roman Numeral is 'III'")
elif(number==4):
    print("The Roman Numeral is 'IV'")
elif(number==5):
    print("The Roman Numeral is 'V'")
# ect ect ect ect



