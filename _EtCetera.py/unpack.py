#Unpacking

from time import sleep
last, first, middle = input("What's your name?: ").split(" ")
print(f"Hi, {first}.")

sleep(1)

def total(galleons, sickles, knuts):
    #calculate total number of money in sickles
    return round(((galleons * 17 ) + sickles) + (knuts/29),2)

coins = [50, 100, 2000]
print(total(*coins), 'Sickles')