# Python Programming - CIT-115-D01 - 2026SP 
# Linda Wolowicz 5-02-2026 
#Assignment Capstone: Banking System


# Share what you liked about this assignment.
# I liked that I learned more on structuring code,and the more I practice reread and go over classwork
# the more I understand.

# Share what you struggled with.
# Struggled with the content of the main() function. 
# struggled with the file.write in produce statement function had to go over chapter7
# found the solution in list methods.
# Could not figure out how to add the box around the transaction history.

# Explain in 100 to 150 words what you learned this semester and how each of your
# previous coding assignments helped to prepare you to code this project?

# I have learned some of the building blocks to writing code. Each coding assignment 
# introduced new concepts and helped me learn through trial and error.
# Each new assignment added new learning outcomes and built a better understending
# of previous things learned. Working with variables, loops, functions, input
# valadation, reading and writing files, error handling, and formatting. 
# The temperature converter and grade analyer assignments helped with if/elif
# conditional statements. The compound interest with loops and lists and realestate 
# assignments helped me with loops. The paint estimator assignment helped with
# file writing and functions. Overall each assignment helped me to uunderstand a little  
# more for the next assignment. Even this project is a learning step to a better 
# understanding of programming.



#1 Deposit money
#2 Withdraw money
#3 checkbalance
#view Transaction history
#apply intrest calculatins
#exit(when exiting make sure to produce statement report by calling ProduceStatement() function()
# need to get balance, list of transactions, menu choice 1-6

#first Create functions 1.PromptForInput, 2. Deposit, 3.Withdraw, 4. CheckBalance, 5.TransactionHistory,
# 6.IntrestApplication, 7.ProduceStatement, 8.have a main()function.
#main() balance,transactions,choice of options,


#Input function to get correct input greater than 0 from user.
def Prompt_For_Input(prompt):
    
    while True:
        try:
            fAmountLCW = float(input(prompt))
            if fAmountLCW > 0:
                return fAmountLCW
            
            else:
                print("Enter a number that is greater than 0.")
           
        except ValueError:
            print("Enter a number.")
            
#Function to get,calculate,store and, show amount in decimals with thousands seperators. 
def Deposit(fBalanceLCW, lstTransHistoryLCW):
    
    fDepositLCW = Prompt_For_Input("Enter deposit amount: ")
    fBalanceLCW = fBalanceLCW + fDepositLCW
    lstTransHistoryLCW.append(f"Deposit: ${fDepositLCW:,.2f}")
    
    print(f"Deposit successful. New balance: ${fBalanceLCW:,.2f}")
    return fBalanceLCW

#Function to get withdrawal amount, check if enough money in account,subtract money from balance,
#stores amount and shows amount in decimals with thousands seperators.
def Withdraw(fBalanceLCW, lstTransHistoryLCW):
    
    fWithdrawLCW = Prompt_For_Input("Enter withdrawal amount: ")
    if fWithdrawLCW > fBalanceLCW: 
        print("Insufficient funds.")
    else:
        fBalanceLCW = fBalanceLCW - fWithdrawLCW
        lstTransHistoryLCW.append(f"Withdraw: ${fWithdrawLCW:,.2f}")
        
        print(f"Withdrawal successful. New balance: ${fBalanceLCW:,.2f}") 
    return fBalanceLCW

#Shows current balance.
def Check_Balance(fBalanceLCW):
    
    print(f"Current Balance: ${fBalanceLCW:,.2f}")
    
#Function that shows all transactions in list. checks if list is empty, takes in first transaction,
#second transaction,and so on, can be one or many.
def Transaction_History(lstTransHistoryLCW):
    
    print("\n---- Transaction History ----")
   
    if len(lstTransHistoryLCW) == 0:
        print("No transactions. ")
        
    else:
        for sTransactionLCW in lstTransHistoryLCW:
            
            print(sTransactionLCW)
    print("------------------------------")
    
#Asks for user interest rate on account, calculates, adds monthly interest, stores to list amount and shows amount
#in decimals with thousands seperators.  
def Interest_Application(fBalanceLCW, lstTransHistoryLCW):
    
    if fBalanceLCW == 0:
        print("Balance is 0. No interest added.")
    else:
        
        fIntRateLCW = Prompt_For_Input("Enter interest rate: ")
        fInterestLCW = fBalanceLCW * (fIntRateLCW / 100 / 12)
        fBalanceLCW = fBalanceLCW + fInterestLCW
        lstTransHistoryLCW.append(f"Interest added: ${fInterestLCW:,.2f}")
    
        print(f"Interest applied: ${fInterestLCW:,.2f}")
        print(f"New balance: ${fBalanceLCW:,.2f}")
    return fBalanceLCW

#Creates a text file saves all transactions and final balance, shows output to user with amounts in decimals with
#thousands separators.  
def Produce_Statement(fBalanceLCW, lstTransHistoryLCW):
    
    FILE_NAME = "lcwBankStatements.txt"

    with open(FILE_NAME, "w") as file:
        
        file.write("Linda W's Python Mini Banking System\n")
        file.write("Transaction History\n")
        file.write("-------------------\n")
        
        if len(lstTransHistoryLCW) == 0:
            file.write("\nNo transactions\n")

        else:
            for item in lstTransHistoryLCW:      
            
#item represents one transaction from the list .title() capitalizes first letter of every word in string.
                file.write(item.title() + "\n")
        file.write("-------------------\n")
        file.write(f"\nNumber of Transactions: {len(lstTransHistoryLCW)}\n")
        file.write(f"Ending Balance: ${fBalanceLCW:,.2f}\n")

    
#Starts the program,  shows menu options, calls the functions.

def main():
   #Empty list
    lstTransHistoryLCW = []
    print("Welcome to Linda W's Python Mini Banking system".title())
   
    fBalanceLCW = 0.0
#loop until the user enters 6 to exit
    while True:
        
        print("\nMenu:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Apply Interest")
        print("6. Exit")

        sChoiceLCW = input("Choose an option (1-6): ").strip()
       
        
        if sChoiceLCW == "1":
            fBalanceLCW = Deposit(fBalanceLCW, lstTransHistoryLCW)
        elif sChoiceLCW == "2":
            fBalanceLCW = Withdraw(fBalanceLCW, lstTransHistoryLCW)
        elif sChoiceLCW == "3":
            Check_Balance(fBalanceLCW)
        elif sChoiceLCW == "4":
            Transaction_History(lstTransHistoryLCW)
        elif sChoiceLCW == "5":
            fBalanceLCW = Interest_Application(fBalanceLCW, lstTransHistoryLCW)
        elif sChoiceLCW == "6":
            Produce_Statement(fBalanceLCW, lstTransHistoryLCW)
            
            print("Thank you for using the banking system.")
            print("Statement generated. Goodbye.")
            break
        
        else:
            print("Invalid option. Choose 1-6. ")

if __name__ == "__main__":
    main()

    


    
    












    













    


