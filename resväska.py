travelbag = ["tandborste", "kläder", "ananas", "spade"]

while True:
   menyval = input("\n1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "Avsluta program\n")

   if menyval == "1":
       for i, sak in enumerate(travelbag, start=1):
        print(i, sak)
   elif menyval == "2":
      travelbag.append (input("vad vill du lägga till? ")) 
       
   elif menyval == "3":
    remove = input("vad vill du ta bort? ")
    if remove.isdigit():

     travelbag.pop (int(remove)-1)

   elif menyval == "4":
       break


