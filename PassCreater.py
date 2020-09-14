import random as rnd

global passw
passw = []
for i in range(1,9):
    pw = rnd.randrange(0,10)
    passw.append(pw)
passw = str(passw)