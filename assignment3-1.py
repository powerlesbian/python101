hrs = input("Enter Hours:")
hours = float(hrs)

rte = input("Please enter rate per hour:")
rate = float(rte)

if hours <= 40:
    print (hours*rate)
elif hours>40:
    othours = hours-40
    multiplier=1.5
    otpayable = rate*multiplier*othours

    print ("OT hours:",otpayable, "Standard hours:", 40*rate)
    print (40*rate+(othours*rate*multiplier))
    

