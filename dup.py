import random
import getpass
import os
'''def encode():
    atmpinno=''
    while True:
        x=msvcrt.getch()
        if x=='\r':
            break
        sys.stdout.write('*')
        atmpinno +=x
        print('\n'+atmpinno)'''

def homepage():
    print("="*121)
    home_page=print('''
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
                
                                                                             ------->9 FORGOT PIN
                
                ''')
    print("="*121)

def captcha():
    import random
    #alphabets
    alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
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
    r5=random.choice(alph)
    #r6=print(r1,r2,r3,r4,r5)
    global r7
    r7=f'{r1}{r2}{r3}{r4}{r5}'
    print(r7)
    r8=f'{r5}{r5}{r3}{r3}{r3}{r3}{r3}{r3}{r3}{r3}{r3}{r3}'
    print(r8)

def deposit():
    os.system('clear')
    accno=input("Enter the account no: ")
    amt=int(input("Enter the amount to be deposited: "))
    print("Available balace in the account is",amt+random.randint(500,50000))
    
def withdrawl():
    os.system('clear')
    amt1=int(input("Enter the amount to be withdrawn: "))
    #encode()
    atmpinno=getpass.getpass("Enter the pin no: ")
    if amt1 >10000:
        otp=int(input("Enter the OTP received on your RMN: "))
        print("please collect the cash",amt1,"Available balance in the account is ",random.randint(1000,2000))
    else:
        print("please collect the cash",amt1,"Available balance in the account is ",random.randint(1000,2000))

def balance_enquiry():
    os.system('clear')
    pin=int(input("ENETR THE PIN NO: "))
    av_bal=print("Available balance in the account is  ",random.randint(1,1000))
    
def pin_change():
    os.system('clear')
    old_pin=int(input("PLEASE ENTER YOUR OLD PIN: "))
    new_pin=int(input("SET NEW PIN: "))
    confirm_new_pin=int(input("CCONFIRM NEW PIN NO: "))
    if old_pin ==new_pin:
        print("\nNEW PIN AND OLD PIN CANT BE SAME.KINDLY CHANGE")
        pin_change()
    if new_pin != confirm_new_pin:
        print("\nPIN NUMBER DOESNT MATCH.TRY AGAIN.")
        pin_change()
    elif new_pin==confirm_new_pin:
        print("*********** PIN CHANGED SUCCESSFULLY ***********")
    else:
        pass
    
def mini_Statement():
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
   
def cardless_cash():
    os.system('clear')
    act_no=int(input("Enter the account no: "))
    tpin=int(input("Enter the Tpin: "))
    mobile_no=int(input("Enter the mobile no: "))
    amt=int(input("Enter the amount: "))
    print("collect the cash Rs.{0} from ATM, Cash balance {1}".format(amt,random.randint(2000,5000)))
    
def login_to_net_banking():
    os.system('clear')
    user_name=input("USER NAME: ")
    password=input("PASSWORD: ")
    print("Enter Captcha Shown below")
    captcha()
    cpt=input("enter captcha here: ")
    if cpt==r7:
        print("captcha verified.")
        os.system('clear')
        otp=int(input("Enter the otp received on your mobile no: "))
        print("LOGGED INTO NET-BANKING SUCCESSFULLY\n\nUSER NAME: ",user_name)
        print("ACCOUNT NO: ",random.randint(31235548487246,89999999999999))
    if cpt!=r7:
        print("invalid captcha.Try again")
        login_to_net_banking()
    else:
        pass
    
def fund_transfer():
    def ben_maintainance():
        ben_name=input("Enter benificiary name: ")
        ben_acc_no=int(input("Enter beneficiary account number: "))
        Conf_no=int(input("Confirm the beneficiary account number: "))
        ifsc=input("Enter IFSC code of the branch: ")
        if ben_acc_no!=Conf_no:
            print("Account no and confirm acc no doesnt match.Try again.")
            ben_maintainance()
        elif ben_acc_no==Conf_no:
            otp=int(input("Enter OTP received on your mobile no: "))
            print("Beneficiary has been added to your list.You can perform the transaction after an hour.")

    def initiate_ft():
        print("Please select the beneficiary from the drop down list.")
        input("Enter the transaction amount: ")
        input("Enter transaction password: ")
        print("Please wait while your transaction is being processed.")
        input('')
        print("Transaction successfull.\nTransaction Id")

"""
def forgot_pin():
"""
homepage()
input("please select option: ")
