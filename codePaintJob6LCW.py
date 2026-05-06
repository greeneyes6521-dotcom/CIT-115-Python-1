# Python Programming - CIT-115-D01 - 2026SP 
# Linda Wolowicz 4-23-2026 
# Assignment: Paint Estimator

#1: Share what you liked about this assignment?
# Liked that I learned that math.ceil is a function in python that rounds upward to nearest int.
# Liked learning that can use tuples to group the states and their tax rate in one variable which
# makes it easier when having many variables. 

#2: Share what you struggled with?
# Had trouble with the SAVE_EST_TO_FILE Joseph helped me with getting it to write 
# to the file.
# Struggled with alligning and indentation Joseph helped me with that and fixing the tuple (list).
# Struggled with where some of the error handling should be Joseph also helped me with that.

#3:Explain what a function is and how to code and use one?
# AFunction is a piece of code that that you give input and returns output you can use multiple times in different programs.
# There are built in functions and functions that you can create.
# You can create your own functions by defining them.
# EX. def What_Is_Your_Age():  #creates a function that asks for input of age 
#         age = input("Enter your age: ")  #User input here
#         print("You are, age, "years old, ") #Output
#     What_Is_Your_Age()  # runs the function

#4:Share 2 reasons why you should code functions:
#1:Saves you from writing the same code multiple times
#2:Makes the code easier to read.


#Get input from user for:
#getFloatInput
#state with tax rate
#Square feet of wall
#paint price
#feet per gallon 
#labor hours per gallon
#labor charge per hour





import math
#Get user input until a positive number
def get_float_input(prompt):  
    while True:
        try:
            fAmountLCW = float(input(prompt))
            if fAmountLCW <= 0:
                print("Amount must not be less than 0.")
                continue
            return fAmountLCW
        except ValueError:
            print("Must be a number")
            
#Get State with tax rate until a correct state abbreviation
def get_State_Tax_Rates(sSTATE_ABBR):
    
    if sSTATE_ABBR == "CT" or sSTATE_ABBR == "VT":
        return 0.06
    elif sSTATE_ABBR == "MA": 
        return 0.0625
    elif sSTATE_ABBR == "ME": 
        return 0.085
    elif sSTATE_ABBR == "NH": 
        return 0.0    
    elif sSTATE_ABBR == "RI": 
        return 0.07
    else:
        return None
                
                
#Find gallons round up and calculate.##
def get_Gallons_Of_Paint(fSquareFeetLCW, fFeetPerGallonLCW): 
    return math.ceil(fSquareFeetLCW / fFeetPerGallonLCW)    

#Find total labor hours per gallonand calculate.
def get_Labor_Hours(iGallonsLCW, fHoursPerGallonLCW):        
    return iGallonsLCW * fHoursPerGallonLCW

#Find labor cost and calculate.
def get_Labor_Cost(fLaborHoursLCW, fLaborRateLCW):
    return fLaborHoursLCW * fLaborRateLCW

#Find paint cost and calculate.
def get_Paint_Cost(iGallonsLCW, fPricePerGallonLCW):
    return iGallonsLCW * fPricePerGallonLCW

#Get sales tax and calculate.
def get_Sales_Tax(fSubtotalLCW, fTAX_RATE):
    return fSubtotalLCW * fTAX_RATE 

##Save to file..Loop inside writes each line to file and prints ##
def SAVE_EST_TO_FILE(sLast_Name, fCost_Data):      
    sFilenameLCW = f"{sLast_Name}_PaintJobOutputLCW.txt"
    with open(sFilenameLCW, "w") as file:
        for sLine in fCost_Data:
            print(sLine)            
            file.write(f"{sLine}\n")
    print(f"Estimate saved to file: {sFilenameLCW}")  
 
def main():
   print("==== Paint Job Estimator ====")

# Prompt for inputs.                        
   fSquareFeetLCW = get_float_input("Enter square feet of wall: ")
   fPricePerGallonLCW = get_float_input("Enter paint price per gallon: ")
   fFeetPerGallonLCW = get_float_input("Enter square feet per gallon: ")
   fHoursPerGallonLCW = get_float_input("Enter labor hours per gallon: ")
   fLaborRateLCW = get_float_input("Enter labor charge per hour: ")
   while True:
               sSTATE_ABBR = input("Enter the abbreviation for the state where job is. (CT, MA, ME, NH, RI, VT): " ).strip().upper()
               fTAX_RATE = get_State_Tax_Rates(sSTATE_ABBR)
               if fTAX_RATE is not None:
                   break
               else:
                   print("Can only be state CT,MA,ME,NH,RI,VT.")
        
#Calculations
   iGallonsLCW = get_Gallons_Of_Paint(fSquareFeetLCW, fFeetPerGallonLCW)
   fLaborHoursLCW = get_Labor_Hours(iGallonsLCW, fHoursPerGallonLCW)
   fLaborCostLCW = get_Labor_Cost(fLaborHoursLCW, fLaborRateLCW)
   fPaintCostLCW = get_Paint_Cost(iGallonsLCW, fPricePerGallonLCW)
   fLSubTotalLCW = fLaborCostLCW + fPaintCostLCW
   fSalesTaxLCW = get_Sales_Tax(fLSubTotalLCW, fTAX_RATE)
   fTotalCostLCW = fLSubTotalLCW + fSalesTaxLCW

# Prompt for customer last name until a name is entered
   while True:
               sLast_Name = input("Enter customers last name: ").strip().title()
               if sLast_Name != '':
                 break
               else:
                    print("Must enter last name.")
    
# Create estimate outputs
   sPaintJobOutput = (f"--------------------------------------",
                  f"Paint Job Estimate for {sLast_Name}",
                  f"--------------------------------------",
                  f"Gallons Needed: {iGallonsLCW}",
                  f"Labor Hours: {fLaborHoursLCW:.2f}",
                  f"Paint Cost: ${fPaintCostLCW:,.2f}",
                  f"Labor Cost: ${fLaborCostLCW:,.2f}",                
                  f"Sales Tax: ${fSalesTaxLCW:,.2f}",
                  f"Total Cost: ${fTotalCostLCW:,.2f}")

##Write to file
   sFilename = SAVE_EST_TO_FILE(sLast_Name, sPaintJobOutput)
                           
# Output
                             
if __name__ == "__main__":
    main()




















 



