red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
italics = '\033[3m'
underline = '\033[4m'
end = '\033[0m'

from random import randint
from time import sleep
unimportant = input("want to zamble y/n" )
polish = 0
zeal = 3
odds = 4
spin_stripped = 1
moola = 50
rep = 0
slot1 = 1
slot2 = 2
slot3 = 3
zen = 3

print(" Lets go Zabli'n! ")
spin = input (" Spin y/n ")
while (zen == 3): 
    if( spin == "y" or spin_stripped == "y"):
        slot1 = randint (1, zeal + odds )
        slot2 = randint (1, zeal + odds )
        slot3 = randint (1, zeal + odds )
        moola = moola - 5
        print (" moola minus five spinning...")
        spin = 0
        sleep (3)
    if((slot1 == slot2) or (slot1 == slot3)):
        moola = moola + 3
        rep = rep + 20
        spin = input ("+3 moola +10 rep Spin again y/n")
        polish = input (" increase odds max 1/5 1/2 ")
    if((slot1 == slot2 == slot3)):
        moola = moola + 50
        rep = rep + 100
        spin = input ( bold+red+" !JACKPOT!" +end)
        print ("+50 moola +100 rep Spin again y/n")
        polish = input (" increase odds max 1/5 1/2 ")
    if ((slot1 != slot2 != slot3)):
        rep = rep - 40
        spin = input (" -40 rep Spin again y/n")
        polish = input (" Cost 25 moola increase odds max 1/5 1/2 ")
    while(polish == 1):
        zeal = zeal - 1
        polish = 9
    if (spin == "n"):
        zen = 2
    if ( moola <= 0):
        zen = 2
    if (rep >= 777 ):
        print (" you win!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    if (spin == "8"):
        moola = 9999
        rep = 7777
        zen = 2
print(str( rep ) + str( moola ) + " Thats your score this time think you can do better?")