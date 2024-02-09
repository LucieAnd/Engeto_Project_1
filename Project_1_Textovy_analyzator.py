#hlavička
print("-" * 10)
print("project_1.py: První projekt do Engeto Online Python Akademie")
print("\nautor: Lucie Anděrová")
print("e-mail: anderova.l@email.cz")
print("discord: luciea._14885")
print("-" * 10)

#dostupné texty
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

#přihlášení
print("Are you a registered user? Let's find out! ")
registered = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("Username: ")
password = input("Password: ")
print("-" * 30)
if username in registered:
    registered_password = registered[username]

    if password == registered_password:
        print("Hello, " + username.capitalize() + ", good to see you. Let's analyze some texts.")
        print("-" * 30)
#vybrání textu
        choose_text = input(
            "You can choose one of three texts we've prepared. Enter number between 1 and 3 to select: ")
        print("-" * 30)
#převést výběr na text
        if 0 < int(choose_text) <= 3:
            text_number = int(choose_text)
            index = text_number - 1
            print(TEXTS[index])
#zobrazení textu a nadpisu
            text_number = int(choose_text)
            index = text_number - 1
            print(TEXTS[index])
            print("-" * 30)
            print("STATISTICS:")

#počet slov
            count_words = len(TEXTS[index].split())
            print(f"There are {count_words} in the selected text.")

#počet slov s velkým písmenem
            count_titlecase = 0
            split_text = TEXTS[index].split()
            for titlecase in split_text:
                if titlecase.istitle():
                    count_titlecase += 1
            print(f"There are {count_titlecase} titlecase words.")



        else:
            print("Not a valid option, terminating the programme, bye.")
    else:
        print("Unregistered user. Terminating the programme. Goodbye.")
else:
    print("Unregistered user. Terminating the programme. Goodbye.")
