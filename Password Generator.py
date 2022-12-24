import random


main_Language = input(
    "Which main language you wanna use? Enter RU / EN to pick: \nКакой основной язык использовать. Впиши RU / EN чтобы выбрать: ").lower()
while main_Language == "ru":
    upper_letters = "ЙЦУКЕНГШЩЗДЛОРПАВЫФЯЧСМИТЬ"
    lower_letters = upper_letters.lower()
    digits = "1234567890"
    symbols = ".;/'[],{"

    everything = ""

    language = input(
        "Какой язык вы хотите использовать в пароле? (ru / en / both): ")

    if language == "both":
        upper_letters += "QWERTYUIOPLKJHGFDSAZXCVBNM"

    elif language == "en":
        upper_letters = "QWERTYUIOPLKJHGFDSAZXCVBNM"
        lower_letters = upper_letters.lower()

    print("Press 'y' to add")

    upper = input("Заглавные буквы: ").lower()

    if upper == "y":
        print("< Заглавные буквы были добавлены >")
    else:
        print("< Заглавные буквы были удалены >")

    lower = input("Маленькие буквы: ").lower()

    if lower == "y":
        print("< Маленькие буквы были добавлены >")
    else:
        print("< Маленькие буквы были удалены >")

    digit = input("Цифры: ").lower()

    if digit == "y":
        print("< Цифры были добавлены >")
    else:
        print("< Цифры были удалены >")

    syms = input("Символы: ").lower()

    if syms == "y":
        print("< Символы были добавлены >")
    else:
        print("< Символы были удалены >")

    if upper == "y":
        everything += upper_letters
    if lower == "y":
        everything += lower_letters
    if digit == "y":
        everything += digits
    if syms == "y":
        everything += symbols

    while True:
        try:
            length = int(input("Введите длину пароля: "))
        except Exception:
            print("Пожалуйста, введите корректную длинну пароля.")
        else:
            break

    while True:
        try:
            amount = int(input("Введите количество паролей: "))
        except Exception:
            print("Пожалуйста, введите корректное количество паролей.")
        else:
            break

    for x in range(amount):
        password = "".join(random.sample(everything, length))
        print(password)
        continue

    a = input(
        "Введите 'x' чтобы продолжить и любой другой символ чтобы выйти: ").lower
    if a == "х" or "x":
        continue
    else:
        break


while main_Language == "en":
    upper_letters = "ЙЦУКЕНГШЩЗДЛОРПАВЫФЯЧСМИТЬ"
    lower_letters = upper_letters.lower()
    digits = "1234567890"
    symbols = ".;/'[],{"

    everything = ""

    language = input(
        "Which language you wanna use in password? (ru / en / both): ")

    if language == "both":
        upper_letters += "QWERTYUIOPLKJHGFDSAZXCVBNM"

    elif language == "en":
        upper_letters = "QWERTYUIOPLKJHGFDSAZXCVBNM"
        lower_letters = upper_letters.lower()

    print("Press 'y' to add")

    upper = input("Upper letters: ").lower()

    if upper == "y":
        print("< Upper keys were added >")
    else:
        print("< Upper keys were removed >")

    lower = input("Lower letters: ").lower()

    if lower == "y":
        print("< Lower keys were added >")
    else:
        print("< Lower keys were removed >")

    digit = input("Digits: ").lower()

    if digit == "y":
        print("< Digits were added >")
    else:
        print("< Digits were removed >")

    syms = input("Symbols: ").lower()

    if syms == "y":
        print("< Symbols were added >")
    else:
        print("< Symbols were removed >")

    if upper == "y":
        everything += upper_letters
    if lower == "y":
        everything += lower_letters
    if digit == "y":
        everything += digits
    if syms == "y":
        everything += symbols

    while True:
        try:
            length = int(input("Enter length of password: "))
        except Exception:
            print("Please enter correct length of password.")
        else:
            break

    while True:
        try:
            amount = int(input("Enter amount of passwords: "))
        except Exception:
            print("Please enter correct amount of password.")
        else:
            break

    for x in range(amount):
        password = "".join(random.sample(everything, length))
        print(password)

    a = input("Print 'X' to continue or any key to quit: ").lower
    if a == "x":
        continue
    else:
        break
