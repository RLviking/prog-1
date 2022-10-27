
accounts = {}
logged_in = False
tries=0

while True:
    menyval = input(
        "1. Skapa konto\n"
        "2. Logga in\n"
        "3. Läs en rolig historia\n"
        "4. Logga ut\n"
        "5. Avsluta program\n"
    )

    if menyval == "1":
        user = input("Välj konto namn\n ")
        password = input("Lösenord\n ")
        if user in accounts:
            print("kontot finns redan ")
        else:
            accounts[user] = password

        

    elif menyval == "2":
        if tries > 3:
            print("Du har slut på försök\n ")
        else:
            log_user = input("Användarnamn\n ")
            log_password = input("lösenord\n ")
        if log_user in accounts:
           if log_password == accounts[log_user]:
            print("Du är inloggad ")
            logged_in = True
        elif logged_in == False:
            print("Fel lösenord eller användarnamn")
            tries += 1

        

    elif menyval == "3":
        if logged_in == True:
            print("Hampus är den bästa läraren någonsin ")
        if logged_in == False:
            print("Det var en gång och den var sandad ")



    elif menyval == "4":
        utlog=input("Vill du logga ut?\n skriv Ja: ").capitalize
        Ja= logged_in = False
        print("du är utloggad ")
        pass

    elif menyval == "5":
        break
