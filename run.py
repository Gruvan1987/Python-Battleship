import random

print("Hello, welcome to The Guessing Game!")
print("This is the classic guessing game that most people have probably played. You choose the highest number, then you have to guess the random number in between. You will get help if you are over or under! ")

top_range = input("Please typ in a number: \n")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print('Type a number that is larger than -1 next time.')
        quit()

else:
    print('You need to type a number the next time.')
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    player = input("Make your guess: \n")
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

print("You got it corret in", guesses, "guesses", "Great work!")
