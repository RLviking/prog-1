import random

tal = random.randint(1, 100)

print("I detta spel ska du giss ett tal mella 1-100 och om du får rätt så vinner du =) ")

while True:
    gissning = int(input("Gissa på ett tal\n "))
    if gissning <tal:
        print("Gissa högre\n ")
    elif gissning >tal:
        print("Gissa lägre\n ")
    elif gissning == tal:
        print("Du gissade rätt\n ")
        break
