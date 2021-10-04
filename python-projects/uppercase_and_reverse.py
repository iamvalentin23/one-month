# Create a function called uppercase_and_reverse that takes a little bit of text, 
# uppercases it all, and then reverses it (flips all the letters around)

def uppercase_and_reverse(sentence):
	return reverse(sentence.upper())

def reverse(sentence):
	return sentence[::-1]

text = uppercase_and_reverse("Do not go gentle into that good night.")  #"THGIN DOOG TAHT OTNI ELTNEG OG TON OD"
print(text)