username = "Rasmus"
print (username)
while True:
    name = input("vill du bli ihop?")
    print (name)
    print ("du svarade", name,)
    svar = input("är du säker")
    if svar == "ja" or "Ja":
        break
print ("tack för ditt svar")