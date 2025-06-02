import random

def gamble(chances):
    gambling = random.randint(1,chances)
    if gambling == 1:
        winprompt = 1
    if gambling != 1:
        winprompt = 0
    return winprompt
    

money = 1000
winprompt = 0
chances = 0
wanted = 0
run = 1
beh = 0
actions = [
           "gamble - gamble away your life savings",
           "steal - when the funds are getting low",
           "run - when you need to vanish, fast",
           "help - list commands"
           ]

while run == 1:
    action = input()

    if action == "gamble":
        output = gamble(100)
        if output == 1:
            print("vyhrar")
            money = money + 10000
            print(money)
        else:
            print("prohrar")
            money = money - 20
            print(money)

    if action == "help":
        print(actions)

    if action == "steal":
        output = gamble(5)
        if output == 1:
            print("sukces")
            money = money + 1000
            print(money)
        else:
            print("no sukces")
            wanted = wanted + 1
            print("Wanted ",wanted)

    if wanted > 0:
        output = gamble(10-wanted)
        if output == 1:
            print("polizei have cometh, run or pray")
            utek = input()
            if utek == "run":
                beh = gamble(2)
                if beh == 1:
                    print ("uspech")
                if beh == 2:
                    print ("neuspech")
                    beh = 0
            if beh == 0:
                bernak = gamble(30)
                if bernak == 1:
                    print("polizei have taketh")
                    money = money - 500
                    wanted = 0
                else:
                    print("máš štěstí")
                    wanted = 0
