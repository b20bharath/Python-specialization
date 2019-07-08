# find() and string slicing to extract the number at the end of the line

text = "X-DSPAM-Confidence:    0.8475";
x = text[text.find("0"):]
print(float(x))
