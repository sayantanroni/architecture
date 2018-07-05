import random
class Bank:
    balance=0
    cust_id=''

    print("HELLO CUSTOMER! START BANKING WITH THE BEST SERVICES,PLEASE REGISTER TO CONTINUE ")

    def __init__(self):

        self.cust_id=random.randint(1000,10000)
        print('''Hello! Your account has been successfully created
        your acc id ''',self.cust_id)
        initial_amt = int(input("Any initial deposit?"))
        self.balance = self.balance + initial_amt
        print("""Your current balance is """,self.balance)
        self.menu()

    def menu(self):
       x=input( print('''***KOLKATA BANK***
        1.DEPOSIT                            2.WITHDRAW
        3.PRINT BALANCE                      4.EXIT

        PLEASE ENTER YOUR CHOICE HERE: '''))

       if x=='1':
           self.deposit()
       elif x=='2':
            self.withdraw()
       elif x=='3':
            self.print_balance()
       else:
           print("BYE")

    def deposit(self):
        a=int(input("Enter the amount to be deposited "))
        self.balance= self.balance+a
        print("Amount successfully deposited.. ")
        self.print_balance()

    def  withdraw(self):
        b=int(input("Enter the amount you want to withdraw "))
        print("Please wait until your request is processed ")
        if b<self.balance:
            self.balance=self.balance-b

            print("Please collect your money.. ")
            print("Amount withdrawn successfully")
            X=input("Do you want a reciept of the transaction ?" )
            if(X=='Y' or X=='y'):
                print("Here's your receipt..")
            elif(X=='N' or X=='n'):
                print("OK. Thank you.")
            self.print_balance()
        else:
            print("Sorry,Insufficient Balance ")
            self.menu()

    def print_balance(self):
        print("Your remaining balance is ",self.balance)
        self.menu()


hdfc=Bank()