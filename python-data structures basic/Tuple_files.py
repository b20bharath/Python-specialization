# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hours = list()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        lst = line.split()
        hours.append((lst[5].split(':'))[0])
count = dict()
for hour in hours:
    count[hour] = count.get(hour,0)+1
msgFre = sorted([(k,v) for k,v in count.items()])
for i in range(len(msgFre)):
    tup =  msgFre[i]
    print(tup[0],tup[1])