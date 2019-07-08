# prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values
fname = input("Enter file name: ")
fh = open(fname)
avg = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count+1
    flot = float(line[line.find(":")+1:])
    avg = avg + flot
print(avg/count)