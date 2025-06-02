import random

def gamble(money):
    gambling = random.randint(1,100)
    if gambling == 1:
        winprompt = 1
    if gambling != 1:
        winprompt = 0
    return winprompt
    

money = 1000
winprompt = 0

action = input()

if action == "gamble":
    output = gamble(money)
    if output == 1:
        print("vyhrar")
        money = money + 10000
        print(money)
    if output == 0:
        print("prohrar")
        money = money - 20
        print(money)
