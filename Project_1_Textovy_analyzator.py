# head
line = "-" * 60
print(line)
print("project_1.py: První projekt do Engeto Online Python Akademie")
print("\nautor: Lucie Anděrová")
print("e-mail: anderova.l@email.cz")
print("discord: luciea._14885")
print(line)

# available texts
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# log in
print("Are you a registered user? Let's find out! ")
registered = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("Username: ")
password = input("Password: ")
print(line)

registered_password = registered.get(username)

if registered_password is not None and password == registered_password:
    print(f"Welcome, {username.capitalize()}, good to see you. Let's analyze some texts.")
    print(line)
else:
    print("Unregistered user. Terminating the program. Goodbye.")
    exit()

# choosing text
choose_text = input(
    "You can choose one of three texts we've prepared. Enter number between 1 and 3 to select: ")
print(line)

# selected text
if choose_text.isdigit() and 1 <= int(choose_text) <= len(TEXTS):
    index = int(choose_text) - 1
    selected_text = TEXTS[index]
    print(f"You have selected: {selected_text}")
    print(line)
    print("STATISTICS:")

# how many words
    split_text = selected_text.split()
    count_words = len(split_text)
    print(f"There are {count_words} in the selected text.")

# how many titlecase, uppercase, lowercase words, numbers, sum
    count_titlecase = 0
    count_uppercase = 0
    count_lowercase = 0
    count_numeric = 0
    numbers = []
    for word in split_text:
        if word.istitle():
            count_titlecase += 1
        elif word.isupper():
            count_uppercase += 1
        elif word.islower():
            count_lowercase += 1
        elif word.isnumeric():
            count_numeric += 1
            numbers.append(int(word))
    total = sum(numbers)
    print(f"There are {count_titlecase} titlecase words.")
    print(f"There are {count_uppercase} uppercase words.")
    print(f"There are {count_lowercase} lowercase words.")
    print(f"There are {count_numeric} numeric strings.")
    print(f"The sum of all the numbers is {total}.")
    print(line)
    print("LEN|    OCCURRENCES    | NR.")
    print(line)

# bar graf
    length_count = dict()
    characters_to_remove = ",."
    list_without_special_characters = [s.replace(",", "").replace(".", "") for s in split_text]
    for words in list_without_special_characters:
        length = len(words)
        if length in length_count:
            length_count[length] += 1
        else:
            length_count[length] = 1
    sorted_keys = sorted(length_count.keys())
    for key in sorted_keys:
        print(f"{key:2} | {'*' * length_count[key]:17} | {length_count[key]}")
    print(line)

else:
    print("Not a valid option, terminating the program, bye.")