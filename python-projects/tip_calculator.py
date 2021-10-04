# Write a script that takes a dollar amount and recommennds a tip (15%, 18% and 20%)
import random

subtotal = float(input("What is your bill sub-total? ").strip('$'))
rounded_subtotal = float(f"{subtotal:.2f} \n")

tip_selection = float(input("Please enter your tip percentage: "))

rounded_tip_selection = float(f"{tip_selection:.2f} \n")

total = rounded_subtotal * (1 + rounded_tip_selection / 100)

greetings = ["Thank you for visiting us",
			"We hope to see you again soon",
			"Have a safe drive home"]

random_greetings = random.choice(greetings)

print(f"{random_greetings}.")
print(f"Your total with tip is ${total:.2f}")