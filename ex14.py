from sys import argv

script, user_name = argv
prompt = '@@@'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions...")
print(f"Do you like potatoes {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright {user_name}, so you said {likes} about potatoes.
You live in {lives}. I'll have to find a map.
AND you have a {computer} computer???  You should upgrade.
""")
