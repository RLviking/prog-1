import random


#En funktion som lägger till värden på alla kort i kortleken
def värden(hand):
    summa = 0
    värde_färg = {"♥" : 0, "♦" : 0, "♠" : 0, "♣" : 0} #lägg till andra färgerna
    for kort in hand:
        color, value = kort.split()
        if value.isdigit():
            värde_färg[color] += int(value) #inden color för färg 
        elif value == "ess":
            värde_färg[color] += 11
        elif value == "knekt" or value == "drottning" or value =="kung":
            värde_färg[color] += 10

    return max(värde_färg.values())
        


#Poäng räknare och liv skapas för att man ska kunna vinna spelet
poäng = 0
spelare1_liv = 3
spelare2_liv = 3
active_player = "spelare som kör"

#Kortlek läggs till 
kort = ["♥", "♦", "♠", "♣"]
värde = ["ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "knekt", "drottning", "kung"]
kortlek = []

for siffra in värde:
    for färger in kort:
        kortlek.append (färger + " " + siffra)

#2 spelare skapas med en varis tom lista(hand) i listan hammnar det kort spelaren har
spelare = {"spelare1": [], "spelare2": []}

#Random kort väljs ut och tas bort ur kortleken
#len(kortlek)-1 räknar index i listan och minskar med 1 så inte ett tomt värde slumpas fram
def dela_ut_kort(spelare): 
    global kortlek
    spelare ["spelare1"], spelare ["spelare2"] = [], []
    for i in range(3):
        start_kort = kortlek.pop(random.randint(0, len(kortlek)-1))
        spelare ["spelare1"].append(start_kort)
        start_kort2 = kortlek.pop(random.randint(0, len(kortlek)-1))
        spelare ["spelare2"].append(start_kort2)

#En hög för kastade kort läggs till
kastade_kort = [] 

dela_ut_kort(spelare)

# Loopar igenom själva spelfunktionen tills nån vinner 
while True:
    # active_player byter så spelare1 och spelare2 kör varanan gång
    active_player = "spelare1" if active_player == "spelare2" else "spelare2"# funkar inte än 
    input("Visa active_player's kort. Trycke enter\n")
    print(*spelare[active_player])
    print("Kastade kort:")
    print(*kastade_kort)
    print(" ")
    menyval = input("Tryck\n 1. Ta upp kort\n 2. Ta upp kort ur kastad hög\n 3. Lägg ut dina kort\n ")


    #Tar upp ett nytt kort
    if menyval == "1":
       start_kort = kortlek.pop(random.randint(0, len(kortlek)-1))
       spelare [active_player].append(start_kort)
       print(*spelare[active_player])
       #Kastar ett av dinna kort och lägger i kastat högen
       #int används för att kunna använda variabeln för pop kuktionen och -1 för att index startar på 0 
       while True: # loopar ifall man skulle skriva fel index så får man ny chans att skriva in rätt
        try:
            kasta = int(input("Välj ett kort att kasta: "))
            kastade_kort.append(spelare[active_player].pop(kasta-1))
            break
        except IndexError:
                print("Ange ett kort från i din hand 1-4 ") #gör så programmet inte krachar vid ogiligt index
       print(" ")
       print(*spelare[active_player])
       print("\n"*18)
    
    # Ta upp ett kort ur kastade kort högen(enbart kortet som senast vart kastat) 
    # istället för att dra nytt kort ur leken
    elif menyval == "2":
        spelare [active_player].append(kastade_kort.pop(-1))
        print(*spelare[active_player])
        while True: # loopar ifall man skulle skriva fel index så får man ny chans att skriva in rätt
            try:
                kasta = int(input("Välj ett kort att kasta\n "))
                kastade_kort.append(spelare[active_player].pop(kasta-1))
                break
            except IndexError:
                print("Ange ett kort från i din hand 1-4 ") #gör så programmet inte krachar vid ogiligt index
        print(*spelare[active_player])
        print("\n"*18)


    #handens värde räknas ut och jämförs med motståndaren och avgör vem som är vinnaren
    elif menyval == "3":
        summa1 = värden(spelare["spelare1"])
        print(summa1)
        summa2 = värden(spelare["spelare2"])
        print(summa2)
        if summa1 > summa2:
            print("Spelare 1 vann rundan")
            spelare2_liv -= 1
            print(spelare1_liv, spelare2_liv)
            dela_ut_kort(spelare)
        elif summa1 == summa2:
            print("Lika")
            print(spelare1_liv, spelare2_liv)
            dela_ut_kort(spelare)
        else:
            print("Spelar 2 vann rundan")
            spelare1_liv -= 1
            print(spelare1_liv, spelare2_liv)
            dela_ut_kort(spelare)
        if spelare1_liv ==0 or spelare2_liv ==0:
            break

#kollar om någon av spelarnas liv når 0 av isåfall avslutas spelet och vinnaren skrivs ut 
if spelare1_liv == 0:
    print("Spelare 2 vann spelet\n spelet är över")
elif spelare2_liv ==0:
    print("Spelare 1 vann spelet\n spelet är över")
