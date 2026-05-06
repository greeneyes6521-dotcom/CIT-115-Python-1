# Python Programming - CIT-115-D01 - 2026SP
# Linda Wolowicz 4-03-2026
# Assignment: Grade Analzyer

#1: Share what you liked about this assignment?
# I liked that I got it to work on my own even though it was not as efficiant and missing
# some requirements but also liked learning how to make it more efficiant.

#2: Share what you struggled with?
# I struggled with getting the average calculation one time for both scenarios. I struggled
#  with dropping the lowest score with less if's
#  My starting version worked but had alot of if's Joseph helped me to figure how to correct that.
# I struggled with how to add the exit into the code.
# I also struggle with setting up the order of the steps still in coding.

#3: Share how you figured out the drop lowest grade.
# I compared the values of the inputted grades by asking if the first grade was
# less than or equal to the second grade the third grade and fourth grade to determine if
# the first grade was lowest if it was not the lowest it would continue to the next step of
# comparing the second grade to the third and fourth grade and so on until it ends at the
# last grade if no other outcomes equals the conditions.(This is where my first version had
# all if statements and was not as efficient) 
 
#4: Share 3 things you learned on this assignment:
#1. I learned where I can apply the system exit.
#2. I learned that I could get the same output with only 1 fAverage = calculation. 
#3. I also learned about the Ctrl+H function (Thank you Joseph!) it makes it much easier
#   to replace or correct repetive words so less typing. 
     
#Prompt for the persons name that the Grade Analyzer is for.
sName = input("What is the name of the person for whom you are entering the grades of? " )
#Variables stored
iGr1_LCW = float(input("Enter Grade1: ")) 
iGr2_LCW = float(input("Enter Grade2: "))                                                 
iGr3_LCW = float(input("Enter Grade3: "))                                                
iGr4_LCW = float(input("Enter Grade4: "))

# Condition for grade not being less than 0 and exiting program
if iGr1_LCW < 0 or iGr2_LCW < 0 or iGr3_LCW < 0 or iGr4_LCW < 0:
   print ("Grade can not be lower than 0")
   raise SystemExit

# Option to drop the lowest score  
sDropLow = input("Would you like to drop the lowest grade Y for yes or N for no: ")

# Condition for entering only these options or exiting program
if sDropLow != "Y" and sDropLow != "y" and sDropLow != "N" and sDropLow != "n":
   print("Enter a Y or N: ") 
   raise SystemExit

# Drop the lowest score and calculate the lowest score if input is y 
if sDropLow == "Y" or sDropLow == "y":

   if iGr1_LCW <= iGr2_LCW and iGr1_LCW <= iGr3_LCW and iGr1_LCW <= iGr4_LCW:
      fLowG_LCW  = iGr1_LCW
   
   elif iGr2_LCW <= iGr3_LCW and iGr2_LCW <= iGr4_LCW:
      fLowG_LCW = iGr2_LCW   
  
   elif iGr3_LCW <= iGr4_LCW:
      fLowG_LCW = iGr3_LCW
     
   else:
      fLowG_LCW = iGr4_LCW
# Divisor equals this if the drop grade equals y   
iDivisor_LCW = 3

# if answer is n not to drop lowest score then do this calculation
if sDropLow == "N" or sDropLow == "n":
   fLowG_LCW = 0
   iDivisor_LCW = 4
   
# Divisor^equals this if the drop grade is n  
fAverage_LCW = (iGr1_LCW + iGr2_LCW + iGr3_LCW + iGr4_LCW - fLowG_LCW) / iDivisor_LCW
                                                                                  
#convert number entered to a letter grade
if fAverage_LCW >= 97.0:
   sLetGR_LCW = "A+"
elif fAverage_LCW >= 94.0:                                                                  
     sLetGR_LCW = "A"  
elif fAverage_LCW >= 90.0:                                                                    
     sLetGR_LCW = "A-"   
elif fAverage_LCW >= 87.0:
     sLetGR_LCW = "B+"
elif fAverage_LCW >= 84.0:
     sLetGR_LCW = "B" 
elif fAverage_LCW >= 80.0:
     sLetGR_LCW = "B-"
elif fAverage_LCW >= 77.0:
     sLetGR_LCW = "C+"
elif fAverage_LCW >= 74.0:
     sLetGR_LCW = "C"    
elif fAverage_LCW >= 70.0:
     sLetGR_LCW = "C-"
elif fAverage_LCW >= 67.0:
     sLetGR_LCW = "D+"
elif fAverage_LCW >= 64.0:
     sLetGR_LCW = "D"
elif fAverage_LCW >= 60.0:
     sLetGR_LCW = "D-"  
else:   
    sLetGR_LCW = "F"
print(f"{sName} has an average of: {fAverage_LCW:.1f} and their grade is: {sLetGR_LCW}. ")
   

      
                
 
     

    



