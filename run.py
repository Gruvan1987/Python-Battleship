import random

top_range = input("Hello, welcome to the guess Game! please typ in a number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print('Type a number that is larger than -1 next time.')
        quit()

else:
    print('You need to type a nuber the next time.')
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    player = input("Make your guess: ")
    if player.isdigit():
        player = int(player)
    else:
        print('You need to type a number the next time.')
        continue
        
    if player == random_number:
        print("Yeah =) You Got It Correct")
        break
    else:
        if player > random_number:
            print("You are above the number!")
        else:
            print("You are below the number!")

print("You got it corret in", guesses, "guesses")
