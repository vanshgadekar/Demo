import os

# Greeting User 
print("\nWelcome Sir\n")

# Command for input card
print("Enter Your Card!\n")

# To give command choose operation
print("Please select below option")

# Types of operation to perform
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. Pin change")
print("5. Exit")




# Creating class for ATM
class ATM():
    
        
    # Contructor for User Information
    def __init__(self,balance,name,pin):
            self.balance = balance
            self.name = name
            self.pin =  pin
      
    # Deposit function 
    def deposit(self,amount):
                
        if amount > 0:
            self.balance += amount
            print("You Deposited :",amount)
            print("Your Total balance is:",self.balance)
        else:
            print("Invalid Amount Entered!")
                
            
    # Withdraw function     
    def withdraw(self,amount):
            
        if amount > 0 and amount <= self.balance :
            self.balance -= amount
            print("You Withdraw :",amount)
            print("Your Total balance is:",self.balance)
        else:
            print("Insufficeint Money!")
                       
                
    def check(self):
        print("Your total balance Rs.",self.balance)
            
         
pin = int(input("Enter your PIN :"))
b = ATM(500,"vansh",pin)

if b.pin == 123:
    print("Pin Accepted!")
    while True:
        oper = int(input("Enter number of operation:")) 
        attempt = 0
         
        if oper == 1:
            pin = int(input("Enter your PIN :"))
            if pin == b.pin:
                deposit_amount = float(input("Enter Deposit Amount :"))
                b.deposit(deposit_amount)
            else:
                print("Invalid Pin!")
                
        elif oper == 2:
            pin = int(input("Enter your PIN :"))
            if pin == b.pin:
                withdraw_amount = float(input("Enter Withdraw Amount :"))
                b.withdraw(withdraw_amount)
            else:
                print("Invalid Pin!")
        
        elif oper == 3:
            pin = int(input("Enter your PIN :"))
            if pin == b.pin:
                b.check()

            else:
                print("Invalid Pin!")
                attempt += 1
                if attempt >= 3:
                    print("Too many attempts....try later!")
    
                 
            
        elif oper == 4:
            old_pin = int(input("Enter old pin :"))
            
            if old_pin == pin:
                new_pin = int(input("Enter new pin :"))
                b.pin = new_pin
                print("Pin changed sucessfully!")
                
            else:
                print("Wrong Pin!")
        
        elif oper == 5:
            print("Exiting....")
            break
    
        else :
            print("Invalid Operator!")
                
else:
    print("Incorrect Pin!")
    

                        





    