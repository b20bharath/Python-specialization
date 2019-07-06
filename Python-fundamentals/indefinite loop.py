# Program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number

largest = 0
smallest = None
while True :
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            flNum = float(num)
        except:
            print("Invalid input")
            continue
        if largest<flNum:
            largest = flNum
        if smallest is None:
            smallest = flNum
        elif smallest>flNum:
            smallest = flNum
            
print("Maximum is", int(largest))
print("Minimum is", int(smallest))