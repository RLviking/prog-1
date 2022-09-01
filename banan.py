name = input("Välkomen till quizen om Sagan om Ringen, Vad heter du? ").capitalize()
print ("Användare", name)
points = 3
score = 0
#fråga 1
while True:
    print ("Fråga 1")
    print ("A, ringen övergav Gollum.")
    print ("B, Bilbo tog den från Gollum. ")
    print ("C, Gollum tappade bort den. ")
    svar1 = input ("Hur förlorade Gollum ringen? ").capitalize()
    if svar1 == "A": 
        print ("Rätt")
        score += points
        break

    else:
         print("Fel")
         points -= 1
#fråga 2
while True:
    print ("Fråga 2")
    print ("A, Tony, Don och Oin")
    print ("B, Gloin, Edward och Tom")
    print ("C, Bert, Tom och William")
    svar2 = input("I hobbit an unexpected journey fanns det tre troll som förvandlades till sten i sol ljus vad hete dem? ").capitalize()
    if svar2 == "C":
        print ("Rätt")
        score += points
        break

    else:
        print("Fel")
        points -= 1
#fråga 3
while True:
    print("fråga 3")
    print("A, 4")
    print("B, 1" )
    print("C, 3")
    print("D, 1/2")
    svar3 = input("Merry frågar pippin hur många lembas bröd han åt. Hur många Lembas bröd åt pippin? ").capitalize()
    if svar3 == "A":
        print ("Rätt")
        score += points
        break

    else:
        print("Fel")
        points -= 1
#fråga 4
while True:
    print ("Fråga 4")
    print("A, 5")
    print("B, 7")
    print("C, 8")
    svar4 = input ("Hur många ringar gavs till dvärg kungaran? ").capitalize()
    if svar4 == "B":
        print("Rätt")
        score += points
        break

    else:
        print("Fel")
        points -= 1
# avslut
print (name, "du fick", score, "poäng av 12 möjliga")