text = "X-DSPAM-Confidence:    0.8475";
start = text.find('0')
number = text[start : 30]
number = float(number)
print(number)
