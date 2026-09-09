realpin=1111
balance=200000
attempts=4

for i in range(1,attempts):
      
    pin=int(input("Enter the ATM pincode: "))

    if pin==realpin :
        print("YOU are successfully loged in!")
        amount=int(input("Enter the amount of withdrawal: "))
        if amount<=balance:
            print("you are able to withdraw your amount",amount)
            yn=int(input("Type 1 to know the balance or skip checking balance:  "))
            if yn==1:
                print("Account balance=",balance-amount)
            print("Thank you for making secured withdrawal")
            break
        else:
            print("You are not able to withdraw",amount,"since your balance is",balance)
    else:
        print("""Please enter the correct pin!
              Try again""")
        attempts=attempts+1
if attempts>3:
    print("You have reached the limits!")
        
        




