class customer():
    #print("Hi dear customer\nchoose an option: \n           Balance enquiry\n           Cash deposit\n           Withdrawl")
    minimum_balance=1000
    def __init__(self,Name,Acc_no,Cust_id,Phone_no,Email_id,Avail_Bal):
        self.name=Name
        self.Acc_no=Acc_no
        self.cust_id=Cust_id
        self.Phone_no=Phone_no
        self.Email_id=Email_id
        self.Avail_bal=Avail_Bal
        

    def balance_enquiry(self):
        print(f"\nBalance in Acc is {self.Avail_bal}")
        return self.Avail_bal
    
    def cash_deposit(self,amt):
        self.Avail_bal+=amt
        print(f"\nDeposited Rs.{amt} Available balance is Rs.{self.Avail_bal}")
        return self.Avail_bal

    def withdrawl(self,amt):
        if amt>self.Avail_bal:
            print("\nInsufficient funds.Available balance is ",self.Avail_bal)        
        if amt<=self.Avail_bal:
            if ((self.Avail_bal-amt)<(self.minimum_balance)):
                print("\nsorry!Minimum balance balance should be Rs.1000")
            else:
                self.Avail_bal-=amt
                print(f"\nCash withdrawn is {amt} and Available balane is {self.Avail_bal}")
            return self.Avail_bal
        
class privileged_class(customer):
    print("OD lomit is Rs.50000")

    def overdraft_loan_facility(self,amt):
        b=self.Avail_bal-amt
        if b<=-50000:
            print("\nSorry!Transaction amount exceeds the loan limit.")
        if b>-50000:
            self.Avail_bal-=amt
            print(f"\nAmount Withdrawn is {amt} and the available balance is {self.Avail_bal}")

#Inheritance
s=privileged_class('ram',7896541364,77854139,62631058792,'der@kk.com',150000)
s.balance_enquiry()
s.cash_deposit(50000)
s.withdrawl(175000)
s.overdraft_loan_facility(15000)
s.overdraft_loan_facility(200000)


#Object creation
Ravi=customer('Ravi',30852672049,110990347,9493595563,'Chiruteja135@gmail.com',2000)
Dharma=customer('Dharma',74185296312,923105840,824729379,'dtrmediaworks@gmail.com',5000)
Vinod=customer('Vinod',32165498741,45678912,8019329557,'vinodkumar.vinnu8@gmail.com',100000)
Sathya=customer('Sathya',10234679892,55478634,9052630765,'Satya@gmail.com',1000)
Chiru=customer('chiru',8693111500808,1109563547,608145685,'ycycr0@gmail.com',500)

#Balance enquiry 
Ravi.balance_enquiry()  #OUTPUT: Balance in Acc is 2000
Dharma.balance_enquiry()#OUTPUT:Balance in Acc is 5000
Vinod.balance_enquiry() #OUTPUT:Balance in Acc is 100000
Sathya.balance_enquiry()#OUTPUT:Balance in Acc is 1000
Chiru.balance_enquiry() #OUTPUT:Balance in Acc is 500

#Deposit
Ravi.cash_deposit(500)     #OUTPUT:Deposited Rs.500 Available balance is Rs.2500
Vinod.cash_deposit(50000)  #OUTPUT:Deposited Rs.50000 Available balance is Rs.150000
Dharma.cash_deposit(10)    #OUTPUT:Deposited Rs.10 Available balance is Rs.5010
Sathya.cash_deposit(666)   #OUTPUT:Deposited Rs.666 Available balance is Rs.1666
Chiru.cash_deposit(444)    #OUTPUT:Deposited Rs.444 Available balance is Rs.944

#Withdrawl
Ravi.withdrawl(25000)   #OUTPUT:Insufficient funds.Available balance is  2000
Ravi.withdrawl(200)     #OUTPUT:Cash withdrawn is 200 and Available balane is 1800
Ravi.withdrawl(1000)    #OUTPUT:sorry!Minimum balance balance should be Rs.1000
Dharma.withdrawl(1000)  #OUTPUT:Cash withdrawn is 1000 and Available balane is 4000
Dharma.withdrawl(5000)  #OUTPUT:Insufficient funds.Available balance is  4000
Dharma.withdrawl(3500)  #OUTPUT:sorry!Minimum balance balance should be Rs.1000
Vinod.withdrawl(10)     #OUTPUT:Cash withdrawn is 10 and Available balane is 99990
Sathya.withdrawl(10000) #OUTPUT:Insufficient funds.Available balance is  1000
Chiru.withdrawl(500)    #OUTPUT:sorry!Minimum balance balance should be Rs.1000

#Mixed
Sathya.balance_enquiry()    #OUTPUT:Balance in Acc is 1666
Sathya.cash_deposit(36000)  #OUTPUT:Deposited Rs.36000 Available balance is Rs.37666
Sathya.cash_deposit(20000)  #OUTPUT:Deposited Rs.20000 Available balance is Rs.57666
Sathya.withdrawl(60000)     #OUTPUT:Insufficient funds.Available balance is  57666
Sathya.withdrawl(34598)     #OUTPUT:Cash withdrawn is 34598 and Available balane is 23068


###########################THANK YOU##################################################







