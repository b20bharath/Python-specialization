# program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours

hrs = input("Enter Hours:")
h = float(hrs)
rat = input("Enter Rate:")
rate = float(rat)
if h<40 :
    print(h*rate)
else :
    print(40*rate+((h-40)*rate*1.5))