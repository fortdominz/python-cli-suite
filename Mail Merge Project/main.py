PLACEHOLDER = "[name]"

names_file = open("./Input/Names/invited_names.txt", "r")
names = names_file.readlines()

letter_file = open("./Input/Letters/starting_letter.txt", "r")
letter_contents = letter_file.read()

for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
    completed_letter = open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w")
    completed_letter.write(new_letter)
