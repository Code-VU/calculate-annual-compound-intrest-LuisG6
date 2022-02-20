def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundIntrest()
# This first 3 lines are provided for you
    def CompoundInterest():

        principal = float(input("Principle (amount): "))
        time =      float(input("Time:               "))
        rate =      float(input("Rate:               "))

        amount = principal*(1 + (rate / 100))**time
        compoundInterest = amount - principal

        print(f"Principal amount: {principal}")
        print(f"Time:             {time}")
        print(f"Rate:             {rate}")
        print(f"Compound Interst: {compoundInterest}")
        print("---")
    try:
        CompoundInterest()
        CompoundInterest()
        CompoundInterest()
    except:
        print("please enter a number")
 #print("Compound Interest: "+str(intrest))

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateCompoundInterest() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN

#calculateCompoundInterest()
