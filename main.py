TEXT_TO_REPLACE = "[name]"

def retrieve_names():
    """ The readlines() method returns a list containing each line in the file as a list item """
    with open ("./Input/Names/invited_names.txt") as names_file:
        return names_file.readlines()

def retrieve_letter():
    """ The read() method returns a string with the contents of the file """
    with open ("./Input/Letters/starting_letter.txt") as letter_file:
        return letter_file.read()

def create_file(guest_name):
    new_letter = original_letter.replace(TEXT_TO_REPLACE, guest_name)
    with open(f"./Output/ReadyToSend/letter_for_{guest_name}.txt", mode="a") as file:
        file.write(new_letter)

original_letter = retrieve_letter()
names = retrieve_names()
names.sort()

for name in names:
    """ The strip() method removes any whitespace from the beginning or the end """

    name = name.strip()
    print(f"Creating letter for {name}...")
    create_file(name)