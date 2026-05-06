
# Python Programming - CIT-115-D01 - 2026SP 
# Linda Wolowicz 2-24-2026
# Assignment: Code Compound Intrest


#1. share what did you like about this assignment?
#  I liked that I'm learning by practicing and making mistakes. I also liked finally seeing the correct output.

#2. share what you struggled with?

#   I struggled alot on this assignment. I over thought alot of it and rearanged input I already had done
# correctly. I struggled with how to set up the equasion. One reason for this is I thought you had to
# have a constant and variable in all mathmatical input. Annother is I thought I had to enter in the
# (1+r/m) first, for example: (1+r/m)* PV * m*t. So didnt understand formatting order of the equasion input.
# I knew which were adding dividing multiplying and to the power of just not what to do with that info in
# format order.
# I also forgot the ^ < > alignment values while doing this project.
 
#3. explain why you needed () on the mathmatical formula at the top of this document?
#    You needed () to tell the program to do that part of the formula first.

#4 share your top 3 things you learned on this assignment?

#4.1 To re read chapters  and rewatch videos when stuck on parts of assignments.

#4.2 That you do not have to have both a constant and a variable in math.

#4.3 To try to concentrate on doing one step at a time in order even if stuck.



# Input and convert all required data.
#1. Assign input type to variables.
#Variables
#fPVLW: is present value, type is float. 
#fRLW: is intrest rate, type is float.
#fTLW: is period of time in month and years, type is float.
#fMLW: is how many times compounding happens per period of time, type is float.
#2. Assign variables into floats.
#3. Input what you want the user to enter.

fPVLW = float(input("Enter your starting deposit. "))
fRLW = float(input("Enter the interest rate. "))
fTLW = float(input("How much time in years whole and partial? "))
fMLW = float(input("How many times compounded per period? "))


# Calculate
#1.Make the fRLW into /100 which is a percent in the equasion.
#2.Make the fFV into the equasion result.
fRLW = fRLW /100
fFV = fPVLW * (1 + fRLW / fMLW ) ** (fMLW * fTLW) 

# Output:
#1. Make output a string
#2. Add in $,thousands seperator and, decimal placement.
 
print (f"Your future value in 2 years will be. ${fFV:^10,.2f} ") 

 


















