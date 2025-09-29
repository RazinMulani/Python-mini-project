# import random module
import random

# Create list of Subject, Actions and Placaes
Subjects = [
    "Sharuk khan",
    "Prime Minister Narendr Modhi",
    "Salman Khan",
    "A Group of Monky",
    "A car",
    "A Mahabaleshwar",
    "The American Tourist"
]

Actions = [
    "Winning",
    "Run",
    "Nepotism",
    "Water Stop",
    "declare wars on",
    "launches",
    "orders",
    "celebrates"
]

Place_or_things = [
    "in Pakistan",
    "in Mumbai local Train",
    "a bathroom",
    "A plate of samosa",
    "during IPL match",
    "at India Gate",
    "inside parliament with pakistans terorist"
]

# 3. start the headline genration loop

while True:
    subject = random.choice(Subjects)
    action = random.choice(Actions)
    plce_or_thing = random.choice(Place_or_things)

    heading = f"BRAKING NEWS: {subject} {action} {plce_or_thing}"
    print("\n" + heading)

    user_input = input("\n Do you want another headline(yes/no):").strip().lower()
    if user_input == "no":
        break

# print goodby message
print("\n Thanks for using fake news genrator. Have you good day...😇")