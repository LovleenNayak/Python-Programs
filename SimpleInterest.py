#Calculating Simple Interest

class interest:
    def simpleInterest(self,principal,time,rate):
        simple_interest = float((principal*time*rate)/100)
        total_amount = float(principal+simple_interest)
        print("Simple Interest : Rs {}0 only".format(total_amount))
    def compoundInterest(self,principal,time,rate,period):
        compound_interest = float(principal*(1+(rate/(period*100)))**(period*time))
        print("Compound Interest : Rs {}0 only".format(compound_interest))

interest = interest()
while True:
    print("Interest Calculation")
    print("====================")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Exit")
    userChoice = int(input("Please Enter between 1-3 : "))
    if userChoice is 1:
        print("Enter the Following details")
        print("===========================")
        p = float(input("Principal : "))
        r = float(input("Rate of Interest : "))
        t = float(input("Time in Year : "))
        interest.simpleInterest(p,r,t)
    elif userChoice is 2:
        print("Enter the Following details")
        print("===========================")
        p = float(input("Principal : "))
        r = float(input("Rate of Interest : "))
        t = float(input("Time in Year : "))
        period = int(input("Time Period : "))
        interest.compoundInterest(p,r,t,period)
    elif userChoice is 3:
        print("Thank You !!!")
        quit()
    else:
        print("OOP !!! Incorrect Details")