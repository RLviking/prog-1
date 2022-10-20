# Övning 3 går ut på att implementera så många av nedanstående funktioner som möjligt
# Ta bort pass och implementera funktionerna


def best(name):
    print(name, "är bäst")
    # TODO Skriv ut att namnet är bäst
    # Ex: "Katherine" in - skriver ut "Katherine är bäst"
name= input("skriv ett namn ")
best(name)    


def square(number):
    return number ** 2
    # TODO Returnera talet kvadrerat
    # Ex: 5 in - 25 ut
square(9)


def sums(a, b):
   return a + b
    # TODO Returnera summan av a och b
    # Ex: 2, 6 in - 8 ut
sums(3,6)

# Nu blir det lite svårare


def maximum(a, b, c):
    if a>b and a>c:
         return a
    elif b>c:
         return b
    else:
         return c
    # TODO Returnera det största av a,b,c
    # Ex: 3, 6, 12 in - 12 ut
    
maximum(4, 9, 2)


def palindrom(ord):
    # TODO Returnera True om ord är ett palindrom
    # Ex: abba in - True ut
    # Palindrom är ett ord som stavas likadant baklänges och framlänges.
    pass


def prime(nr):
    # TODO Returnera True om nr är ett primtal, annars returnera false
    # Ex: 5 in - True ut
    pass