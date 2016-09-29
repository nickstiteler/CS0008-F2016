
# Setting the variable for what the units the customer wants to use
units = (input('Enter 1 for usc units and 2 for metric units'))

# I test
units = int(units)

# if/else to determine if the input is valid
if (units==1 or units==2):
    print("units accepted")
else:
    print("ENTER 1 OR 2!!!")
    exit

# Setting variables for the distance and gas
distance = float(input('Please enter the distance driven'))
gas = float(input('Please enter the gas used'))

# If US Customary units are selected
if(units==1):

    # Renaming variables for convenience sake, useful when printing at the end
    usc_distance = distance
    gallons = gas
    gal_cons = usc_distance/gallons

    # Conversion equations for usc to metric
    met_distance = usc_distance*1.60934
    liters = gallons*3.78541
    lit_cons = 100*liters/met_distance

# If metric units are selected
elif(units==2):

    # Renaming variables for convenience
    met_distance = distance
    liters = gas
    lit_cons = 100*liters/met_distance

    # Converting from metric units to usc units
    usc_distance = distance*.621371
    gallons = liters*.264172
    usc_cons = usc_distance/gallons

# if/elif/else for setting what the variable "rating" is equal to
if(lit_cons>20):
    rating = "Extremely poor"
elif(lit_cons<=20 and lit_cons>15):
    rating = "Poor"
elif(lit_cons<=15 and lit_cons>10):
    rating = "Average"
elif(lit_cons<=10 and lit_cons>8):
    rating = "Good"
else:
    rating = "Excellent"

print(\t,\t,"USC"\t,"Metric")
print("Distance______________:"\t,usc_distance,"miles"\t,met_distance,"Km")
print("Gas___________________:"\t,gallons,"gallons"\t,liters,"liters")
print("Consumption___________:"\t,usc_cons,"mpg"\t,lit_cons,"l/100Km")

print('Gas Consumption Rating:',rating)






