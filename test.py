
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

    max(värde_färg)
    return 


#orginal kod
"""
    def värden(hand):
    summa = 0
    for kort in hand:
        value = kort.split()[1]
        if value.isdigit():
            summa += int(value)
        if value == "ess":
            summa += 11
        if value == "knekt" or value == "drottning" or value =="kung":
            summa += 10
    return summa
"""