# Python Programming - CIT-115-D01 - 2026SP 
# Linda Wolowicz 4-26-2026 
# Assignment:# Real Estate Sales Analyzer

#1: Share what you liked about this assignment?
# I liked that it took me a bit less than 2 weeks to finish.

#2: Share what you struggled with?
# Struggled with alligning it properly kept getting errors.

# Struggled with getting the first input statement first.

# Had a hard time with getting the code to accept 0 for input had the wrong operator.

# I struggled the type of division in the get_Median function finally figured out
# it was interger division. Still have a hard time with the three types.

#: Explain what a list is and how it works?
# A list is a type of sequence that holds multiple data types. It stores multiple
# items in a single variable and makes it easier and mre organied when coding
# multiple variables instead of coding statements for each one.

#: Give an example of how a list could be used in one of your previous projects?
# Could of been used in the grade analyer by creating an empty list and adding the
# 4 grades that were seperate variables into one variable.


#Calculate and output: Minimum value, Maximum value, Total value, Get average,median value, and commission earned.

# BDJ Real Estate Sales Analyzer

import math

# Float input function. Get user input until a number 0 or greater is entered.
def get_Float_Input(prompt):
    
    while True:
        try:
            fValueLCW = float(input(prompt))
            if fValueLCW < 0:
                print("Value must be 0 or greater.")
            else:
                return fValueLCW
        except ValueError:
            print("Please enter a number.")
            
# Median function to sort and get middle value of numbers.
def get_Median(fNumbersLCW):
    fSortNumLCW = sorted(fNumbersLCW)
    
# Get total number of entries and find the middle of them.
    iMidNum1LCW = (len(fSortNumLCW) - 1) // 2 
    iMidNum2LCW = len(fSortNumLCW) // 2
    
    return (fSortNumLCW[iMidNum1LCW] + fSortNumLCW[iMidNum2LCW ]) / 2 
       
# Total function, get sales total.
def get_Total(fNumbersLCW):
    fTotalLCW = 0

    for number in fNumbersLCW:
        fTotalLCW += number
        
    return fTotalLCW

# Average function, get sales average.
def get_Average(fNumbersLCW):
    fTotalLCW = get_Total(fNumbersLCW)
    
    return fTotalLCW / len(fNumbersLCW)

# Minimum function, get sales minimum.
def get_Minimum(fNumbersLCW):

    return min(fNumbersLCW)

# Maximum function, get maximum sales.
def get_Maximum (fNumbersLCW):

    return max(fNumbersLCW)

# Commission rate function. multiply the sales by 3% to get commission.
def get_Commission_Total(fNumbersLCW): 
    fCommissionLCW = 0
    for number in fNumbersLCW:
        fCommissionLCW += number * 0.03
        
    return fCommissionLCW

def main():

    fSalesListLCW = []
# Get first value and add values to the list.  
    fSaleAmountLCW = get_Float_Input("Enter property sales value: ")
    fSalesListLCW.append(fSaleAmountLCW)
    
    while True:
        
        sChoiceLCW = input("Enter another value Y or N: ").upper()
        
        while sChoiceLCW  != "Y" and sChoiceLCW != "N":
            sChoiceLCW = input("Enter Y or N: ").upper()
            
 # Exit loop if N is inputted.           
        if  sChoiceLCW == "N":
            break
        
# Get another value and add to the list.
        fSaleAmountLCW = get_Float_Input("Enter property sales value: ")
        fSalesListLCW.append(fSaleAmountLCW)
        
# Calculate
    fMinimumLCW = get_Minimum(fSalesListLCW)
    fMaximumLCW = get_Maximum(fSalesListLCW)
    fTotalLCW = get_Total(fSalesListLCW)
    fAverageLCW = get_Average(fSalesListLCW)
    fMedianLCW = get_Median(fSalesListLCW)
    fCommissionLCW = get_Commission_Total(fSalesListLCW)

    print("\n--- Sales Summary ---")
    print(f"Minimum Sale: ${fMinimumLCW:,.2f}")
    print(f"Maximum Sale: ${fMaximumLCW:,.2f}")
    print(f"Total Sales:  ${fTotalLCW:,.2f}")
    print(f"Average Sale: ${fAverageLCW:,.2f}")
    print(f"Median Sale:  ${fMedianLCW:,.2f}")
    print(f"Commission:   ${fCommissionLCW:,.2f}")

if __name__ == "__main__":
    main()


         
        










    














