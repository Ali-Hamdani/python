an_letters = "aeouiAEOUI"

word = input("I will cheer for you! Enter a word: ")  
times = int(input("Enthusiasm level (1-10): "))

#i = 0
#while i < len(word):  
#	char = word[i]
for i in range(len(word)):
	if word[i] in an_letters:
		print("Give me an " + word[i] + "! " + word[i])  	
	else:
		print("Give me a	" + word[i] + "! " + word[i])  	
	#i += 1
print("What does that spell?")  
for i in range(times):
	print(word, "!!!")



