import random as r; tmp, v, t = "", int(input("Enter amount of passwords to be generated: ")), int(input("Enter the length of the password to be generated: "))
for o in range(v):
   for i in range(t):
      tmp = tmp + str(r.choice(["!","@","£","$","%","^","&","*","(",")","-", "_", "+","=", "`", "¬", "¦", "'", "[", "]", ";", ":", "{", "}", "~", "#", ",", "<", ".",">", "/","?","|", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]))
   print(tmp); tmp = ""
