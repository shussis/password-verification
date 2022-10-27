#ПРОВЕРКА НА ПОВТОР ПАРОЛЯ

password = input()
repeat = input()

def proverka(text1, text2):
    if text1==text2:
        print("Correct")
    else:
        print("Wrong")

proverka(password,repeat)