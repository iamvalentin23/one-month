import random

bars = ["Shoolbred's",
        "The Wren",
        "The Scratcher",
        "ACME",
        "Blind Barber",
        "Lion's Head Tavern"]

people = ["Mattan",
          "Chris",
          "that person you forgot to text back",
          "Kanye West",
          "Samule L. Jackson"]

random_bar = random.choice(bars)
random_person = random.choice(people)

print(f"WAIT, WHAT DOES YOUR STARTUP DO?")
print(f"SO, BASICALLY, IT'S LIKE A {random_bar} for {random_person}")
