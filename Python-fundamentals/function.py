# Program to prompt the user for hours and rate per hour using input to compute gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. The function should return a value

def computepay(h,r):
    if h<40 :
        return h*r
    else :
        return (40*r+((h-40)*r*1.5))

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
p = computepay(float(hrs),float(rate))
print(p)