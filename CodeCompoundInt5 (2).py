# Python Programming - CIT-115-D01 - 2026SP
# Linda Wolowicz: 04-18-2026 
# Assignment: Compound Intrest with Loops

#1: Share what you liked about this assignment?
# I liked that I got it to work even though it was done in two loops 
#2: Share what you struggled with?
# Struggled with ammount of loops to write for the best efficiancy. My original had
# only 2 loops so was not as efficiant. Also struggle with the for loops and how to
# include them logically in the code. 


#3: Explain the common difference of Python while and for loops.
# While loops are used when the number of times a loop needed to continue is not known.
# For loops are used when the number of times a loop needed is known.

#4: How many loops in total did you code? 6

# Share 3 things you learned on this assignment.
#
#
#
#
#
#
# Ask the user for deposit, intrest rate and goal amounts.
print("HELLO")

while True:          #Loop1
    try:
        fDepositLCW = float(input("What is your Deposit amount? "))
        if fDepositLCW > 0:
            break
        print("Amount cannot be zero or less.")
    except ValueError:
         print("Must be a number.")
         
while True:         #Loop2
    try:
        fINT_RATE = float(input("Enter the interest rate in percentage. "))
        if fINT_RATE  > 0:
            break
        print("Amount cannot be zero or less.")
    except ValueError:
         print("Must be a number.")  

while True:         #Loop3
    try:
        iMO_TO_SHOW    = int(input("Enter the number of months you would like to see calculated. "))
        if iMO_TO_SHOW > 0:
            break
        print("Amount cannot be zero or less.")
    except ValueError:
         print("Must be a number.")  

while True:       #Loop4 
    try:
        fGOAL_A   = float(input("What is your goal amount? "))
        if fGOAL_A >= 0:
            break
        print("Amount must be zero or more.")
    except ValueError:
         print("Must be a number.")
            
# Find the number of months and the total amount.
fNumOfMLCW = 0
fTotalLCW = fDepositLCW

# Calculate the monthly interest rate from the annual percentage rate.
fMONTH_RATE = fINT_RATE / 100 / 12
                 #Loop5
# Loop until the total number of months = user input.
while fNumOfMLCW < iMO_TO_SHOW:
      fNumOfMLCW += 1  
      fTotalLCW += fTotalLCW * fMONTH_RATE  # Multiply the monthly rate by the total to get new total.
      print(f"Month {fNumOfMLCW}: ${fTotalLCW:,.2f} ")
                 #Loop6  
fNumOfMLCW = 0
fTotalLCW = fDepositLCW
# Loop until the total amount equals or is more than the goal amount.   
while fTotalLCW <= fGOAL_A: 
      fNumOfMLCW += 1
      fTotalLCW += fTotalLCW * fMONTH_RATE # Multiply the monthly rate by the total to get new total.

if fGOAL_A > fDepositLCW:
    print(f"Your goal will be reached in {fNumOfMLCW} months and your total amount will be ${fTotalLCW:,.2f} ")

       
       
            
            
          
           
               
