import time
import random

#Initialize player scores
player_a_score = 0
player_b_score = 0
round = 0
state = True

print("Press 1 for best of 3")
print("Press 2 for best of 5")
print("Press 3 for best of 7")

choice = int(input("Make your choice: "))


print("Welcome to the Game: The Chance")
time.sleep(1)

#Player 1 input
player_a = input("Enter name for Player 1: ")
time.sleep(1)
print("Welcome " + player_a)
time.sleep(1)

#Player 2 input
player_b = input("Enter name for Player 2: ")
time.sleep(1)
print("Welcome " + player_b)
time.sleep(1)



while state:
    print("Roll the dice " + player_a + " and " + player_b)
    result1 = random.randint(1,7)
    result2 = random.randint(1,7)
    
    if result1 > result2:
        print(result1)
        print(result2)
        time.sleep(1)
        print(player_a + " wins!")
        player_a_score+=1

    elif result1 < result2:
        print(result1)
        print(result2)
        time.sleep(1)
        print(player_b + " wins!")
        
    else:
        print(result1)
        print(result2)
        time.sleep(1)
        print("It was a tie!")
        
    round+=1
    print("End of round" ,round)

if choice == 1:
    if player_a_score == 2 or player_b_score == 2:
        state = False
elif choice == 2:
    if player_a_score == 3 or player_b_score == 3:
        state = False
else:
    if player_a_score == 4 or player_b_score == 4:
        state = False

print("\nFinal score")

print(player_a_score)
print(player_b_score)
    