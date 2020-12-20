from sys import argv

script, user_name, first, second = argv
prompt = "Go on:"

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

print("Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer you have?")
computer = input(prompt)

print(f"Alright, so you said you {likes} about me and you live in {lives} Not sure where that is. And you have a {computer} computer. Nice """)
print(first)
print(second)
