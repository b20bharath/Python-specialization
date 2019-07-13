#Using regular expression to find the sum of numbers in a text
import re
hand = open('regex_sum_254936.txt')
total = 0
for line in hand:
    line = line.rstrip()
    y = re.findall('[0-9]+',line)
    if len(y)>0:
        for num in y:
            total = total+int(num)
print(total)
