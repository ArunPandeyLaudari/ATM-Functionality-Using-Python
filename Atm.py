class Atm:
    
    def __init__(self):
       self.pin=""
       self.balance=0

       self.menu()
    def menu(self):
        user_input=input("""How would you like to procedd?
                          1.Enter 1 to create a pin 
                          2.Enter 2 to deposit
                          3.Enter 3 to withdraw
                          4.Enter 4 to check balance
                          5.Enter 5 to Exit """)
        if user_input =="1":
            self.create_pin()
            self.menu()
        elif user_input=="2":
            self.deposit()
            print("deposit") 
            self.menu()
        elif user_input=="3":
            self.withdraw()
            print("withdraw")
            self.menu()
        elif user_input=="4":
            self.check_balance()
            print("check balance")
            self.menu()
        else:
            print("Exit")

    def create_pin(self):
        self.pin = input("Enter your pin") 
        print("Pin create sucessfully")

    def deposit(self):
        temp=input("Enter your pin")
        if temp==self.pin:
            amount=int(input("Enter deposit amount"))
            self.balance+=amount
            print("Deposit sucessfully")                 
        else:
            print("invalid pin")            

    def withdraw(self):
        temp=input("Enter pin")
        if temp==self.pin:
            amount=int(input("Enter the amount"))
            if amount < self.balance:
                self.balance-=amount
                print("withdraw sucessfully")
            else:
                print("No sufficient amount")    
        else:
            print("Invalid pin")


    def check_balance(self):
        temp=input("Enter the pin")
        if temp==self.pin:
            print(self.balance) 
        else:
            print("invalid pin") 
            
b=Atm()