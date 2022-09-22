import random as r
amount = int(input("Enter amount of passwords to be generated: "))
length = int(input("Enter the length of the password to be generated: "))
sym = [["!","@","£","$","%","^","&","*","(",")","-", "_", "+","=", "`", "¬", "¦", "'", "[", "]", ";", ":", "{", "}", "~", "#", ",", "<", ".",">", "/","?","|", " ", ""], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"], ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]
print("Generating passwords...")
tmp = ""
for o in range(amount):
   for i in range(length):
      x = r.randint(0,2)
      s = r.randint(0,34)
      l = r.randint(0,25)
      n = r.randint(0,9)
      if x == 0:
         tmp = tmp + str(sym[x][s])
      elif x == 1:
         tmp = tmp + str(sym[x][l])
      elif x == 2:
         tmp = tmp + str(sym[x][n])
   print(tmp)
   tmp = ""
