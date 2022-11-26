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

while True:
    print("")
    break