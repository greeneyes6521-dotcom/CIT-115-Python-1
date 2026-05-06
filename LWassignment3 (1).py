# Python Programming - CIT-115-D01 - 2026SP 
# Linda Wolowicz 3-20-2026 
# Assignment: Code temperature converter

#1: Share what you liked about this assignment?
# I liked the feeling of finally getting it to work after two weeks with a help session with Joseph.

#2: Share what you struggled with?
# Struggled with the order process and nesting sequence and once again over thought it and used 
# the if statements more than was needed to make it work. also struggled on how to get user input to
# equal more than one specified unit,f or c.


#3: Explain how the if/else and if/elif/else works and how they differ.
# If/else has two paths one if true and one if false. If/else must be indented for each if statement so can
# take up alot of space so can become confusing to read.
# If/elif/else is more readable by making decision structures nested so takes up less space so simpler to read.

#4: Which one did you code for this assignment and why did you choose it?
# I coded with the if/elif/else and, chose it because tried using the if else
# and ended up with a mess that caused confusion when trying to make sense of what
# I was trying to write.

# Share 3 things you learned on this assignment:
#1.I learned how to make the sUnitLCW = either C or c or F or f.
#2.I learned that using nested structure is less confusing to read when trying to get a code to work.
#3.I learned that a single assignment operator can have more than one meaning depending
#on how it is being assigned.

# Welcome message:

print("Welcome to Linda's temperature converter.")

# Prompt user for a temperature:
# Prompt user for a unit F for farenheit or C for celcius:
# in uper and lowercase.

# variables
# iTempLCW
# sUnitLCW
# fTempConvert
iTempLCW = float(input("What is the temperature: " ))
sUnitLCW = input("Enter the temperature F for Farenheit or C for Celcius: ")

#If user input is F,f and temp is greater than 212, issue error message:
#If user input is F,f and temp is less than 212,calculate, format, and output message:
#If user input is C,c and temp is greater than 100, issue error message:
#If user input is C,c and temp is less than 100,calculate, format, and output message:
if sUnitLCW == "F" or sUnitLCW == "f":
  if iTempLCW > 212:
     print("Temp can not be greater than 212 degrees Farenheit.")    
  else:
     fTempConvert = (5.0/9) * (iTempLCW - 32)
     print(f"The celcius equivalent is: {fTempConvert:.1f} ")
     
elif sUnitLCW == "C" or sUnitLCW == "c":
     if iTempLCW > 100:
        print("Temp can not be greater than 100 degrees Celcius. " )   
     else:
         fTempConvert = ((9.0/5.0) * iTempLCW)+ 32
         print (f"The farenheit equivalent is: {fTempConvert:.1f} ")
# If user enters input other than F or C issue error message:
if not (sUnitLCW == "F" or sUnitLCW == "f" or sUnitLCW == "C" or sUnitLCW == "c"): 
   print("You must enter an F or C")       

# THE END .......

              
    






















    
