import os
import random
import getpass

class customer():
    def __init__(self,name,acc_no,cus_id,phone_no,email_id):
        self.name=name
        self.acc_no=acc_no
        self.cus_id=cus_id
        self.phone_no=phone_no
        self.email_id=email_id

    def captcha(self):
        import random
        #alphabets
        alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        alph_u=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        #symbols
        sy=['!','@','#','$','%','^','&','*','(',')','_','+']
        #numbers
        x=[]
        for i in range(0,101):
            x.append(i)
            i+=1
        r1=random.choice(alph)
        r2=random.choice(sy)
        r3=random.choice(x)
        r4=random.choice(sy)
        r5=random.choice(alph_u)
        #r6=print(r1,r2,r3,r4,r5)
        global r7
        r7=f'{r1}{r2}{r3}{r4}{r5}'
        r9=random.randint(10000000000,90000000000)
        global r8
        r8=f'{r5}{r1}{r9}'    

    def deposit(amt):
        os.system('clear')
        amt=int(input("Enter the amount to be deposited: "))
        print("Available balace in the account is",amt+random.randint(500,50000))

    def withdrawl(amt1):
        os.system('clear')
        amt1=int(input("Enter the amount to be withdrawn: "))
        #encode()
        atmpinno=getpass.getpass("Enter the pin no: ")
        if amt1 >10000:
            otp=int(input("Enter the OTP received on your RMN: "))
            print("please collect the cash",amt1,"Available balance in the account is ",random.randint(1000,2000))
        else:
            print("please collect the cash",amt1,"Available balance in the account is ",random.randint(1000,2000))
        
    def balance_enquiry(pin):
        os.system('clear')
        pin=int(input("ENETR THE PIN NO: "))
        print("Available balance in the account is  ",random.randint(1,1000))

    def pin_change(self):
        os.system('clear')
        old_pin=int(input("PLEASE ENTER YOUR OLD PIN: "))
        new_pin=int(input("SET NEW PIN: "))
        confirm_new_pin=int(input("CCONFIRM NEW PIN NO: "))
        if old_pin ==new_pin:
            print("\nNEW PIN AND OLD PIN CANT BE SAME.KINDLY CHANGE")
            self.pin_change()
        if new_pin != confirm_new_pin:
            print("\nPIN NUMBER DOESNT MATCH.TRY AGAIN.")
            input('')
            self.pin_change()
        elif new_pin==confirm_new_pin:
            print("*********** PIN CHANGED SUCCESSFULLY ***********")
        else:
            pass

    def mini_Statement(self):
        os.system('clear')
        print('''
        02/02/2023  cash deposit    Cr  Rs.200/-
        03/02/2023  cash deposit    Cr  Rs.1000/-
        03/02/2023  cash withdrawl  Dr  Rs.3000/-
        06/02/2023  ATM Withdrawl   Dr  Rs.500/-
        08/02/2023  cash withdrawl  Dr  Rs.2500/-
        -----------------------------------------
            Available Cash balance''',(random.randint(1000,5000)))
        print('''    -----------------------------------------''')
    
    def cardless_cash(self):
        os.system('clear')
        tpin=int(input("Enter the Tpin: "))
        mno=int(input("Enter the mobile no: "))
        amt=int(input("Enter the amount: "))
        print("collect the cash Rs.{0} from ATM, Cash balance {1}".format(amt,random.randint(2000,5000)))

    def fund_transfer(self):
        os.system('clear')
        self.captcha()
        up=int(input('''
                                        FUND TRANSFER
                1 ADD BENEFICIARY                               2.INITIATE TRANSACTION
                '''       ))
        def ben_maintainance():
            ben_name=input("Enter benificiary name: ")
            ben_acc_no=int(input("Enter beneficiary account number: "))
            Conf_no=int(input("Confirm the beneficiary account number: "))
            ifsc=input("Enter IFSC code of the branch: ")
            if ben_acc_no!=Conf_no:
                print("Account no and confirm acc no doesnt match.Try again.")
                input('')
                ben_maintainance()
            elif ben_acc_no==Conf_no:
                otp=int(input("Enter OTP received on your mobile no: "))
                print("Beneficiary has been added to your list.You can perform the transaction after an hour.")
                input('')
                os.system('clear')
        def initiate_ft():
            print("Please select the beneficiary from the drop down list.")
            input("Enter the transaction amount: ")
            input("Enter transaction password: ")
            print("Please wait while your transaction is being processed.")
            input('')
            print("Transaction successfull\nTransaction Id",r8)
        if up==1:
            ben_maintainance()
        else:
            initiate_ft()

    def login_to_net_banking(self):
        self.captcha()
        os.system('clear')
        print("USER NAME:",self.name,"\nAccount no: ",self.acc_no)
        password=input("ENTER LOGIN PASSWORD: ")
        print("Enter Captcha Shown below")
        print(r7)
        cpt=input("enter captcha here: ")
        if cpt==r7:
            print("captcha verified.")
            os.system('clear')
            otp=int(input("Enter the otp received on your mobile no: "))
            print("LOGGED INTO NET-BANKING SUCCESSFULLY\n")
        if cpt!=r7:
            print("invalid captcha.Try again")
            self.login_to_net_banking()
        else:
            pass

print("Hi Dear customer!!\nPlease fill the following details before we proceed further\n")

c1=customer(name=input("Name: "),acc_no=int(input("Acc no: ")),cus_id=int(input("Customer Id: ")),phone_no=int(input("Mobile no: ")),email_id=input("Emails Id: "))

def start():
    print("="*121)
    print('''
                                            "WELCOME TO CHIRU'S BANK"

                    ----------------                                           --------------------                       
                    |  1 DEPOSIT     |                                         |    2 WITHDRAWL     |
                    ----------------                                           --------------------

                    -----------------                                           -------------------
                    |3 BALANCE ENQUIRY|                                        |    4 PIN CHANGE    |
                    -----------------                                           -------------------

                    -----------------                                           -------------------
                    |5 MINI STATEMENT |                                        |  6 CARD-LESS CASH  |
                    -----------------                                           -------------------
                    
                    -----------------                                           -------------------
                    |7 FUND TRANSFER  |                                        |8 NET BANKING LOGIN |
                    -----------------                                           -------------------
                    ''')
    print("="*121)
    i=int(input("Choose a option: "))
    os.system('clear')
    if i==1:
        c1.deposit()
    elif i==2:
        c1.withdrawl()
    elif i==3:
        c1.balance_enquiry()
    elif i==4:
        c1.pin_change()
    elif i==5:
        c1.mini_Statement()
    elif i==6:
        c1.cardless_cash()
    elif i==7:
        c1.fund_transfer()
    elif i==8:
        c1.login_to_net_banking()

while True:
    start()
    cont=int(input("\nDO U LIKE TO DO ANOTHER TRANSACTION? 1.Yes/2.No\n"))
    if cont==1:
        continue
    else:
        print("\n\n                       Thank u for using CHIRU BANK SERVICES\n\n\t\t              ****HAVE A NICE DAY****")
        break