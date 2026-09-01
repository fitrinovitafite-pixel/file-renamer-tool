import random 
jokes = [
    "Why did the computer go to the doctor? Because it had a virus!",
    "What do you call a sleeping bull? A bulldozer!",
    "Why was the math book sad? Because it had too many problems!"
]
while True: 
	joke = random.choice(jokes)
	print (joke)
	lagi = input("Mau joke lagi? (y/n): ")
	if lagi.lower() == "n":
		break