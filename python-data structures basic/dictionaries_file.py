# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
address = list()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        lst = line.split()
        address.append(lst[1])
count = dict()
bigword = None
bigcount = None
for word in address:
    count[word] = count.get(word,0) + 1
    if bigword is None or count[word]>bigcount:
        bigcount = count[word]
        bigword = word
print(bigword,bigcount)