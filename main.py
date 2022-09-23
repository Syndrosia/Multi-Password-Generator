import random as r
amount, length, sym, tmp = int(input("Enter amount of passwords to be generated: ")), int(input("Enter the length of the password to be generated: ")), ["!","@","£","$","%","^","&","*","(",")","-", "_", "+","=", "`", "¬", "¦", "'", "[", "]", ";", ":", "{", "}", "~", "#", ",", "<", ".",">", "/","?","|", " ", "", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], ""
for o in range(amount):
   for i in range(length):
      s = r.randint(0,68)
      tmp = tmp + sym[s]
   print(tmp); tmp = ""
