import random
num = random.randint(1000,9999)
HITS = 0
MISSES = 0
def intro():


    print("Welcome to \"MAGSHIMIM CODE-BREAKER\"!!!\n\n")
    print("A secret password was chosen to protect the credit card of Pancratius,")
    print("the descendant of Antiochus.")
    print("Your mission is to stop Pancratius by revealing his secret password.\n\n")

    print("The rules are as follows:\n")
    print("1. In each round you try to guess the secret password (4 distinct digits)\n")
    print("2. After every guess you'll receive two hints about the password\n\n")
    print("   HITS:   The number of digits in your guess which were exactly right.\n")
    print("   MISSES: The number of digits in your guess which belongs to\n ")
    print("		   the password but were miss-placed.\n")
    print("3. If you'll fail to guess the password after a certain number of rounds\n")
    print("   Pancratius will buy all the gifts for Hanukkah!!!\n\n")

    print("Please choose the game level:\n")
    print("1 - Easy (20 rounds)\n")
    print("2 - Moderate (15 rounds)\n")
    print("3 - Hard (10 rounds)\n")
    level =  input("4 - Crazy (random number of rounds 5-25)\n")
    #I think theres a way to write this with less code
    while 1:
        if level == "1":
            return 20
        elif level == "2":
            return 15
        elif level == "3":
            return 10
        elif level == "4":
            pass
        else:
            level = input("Please enter a number 1-4")

        

def guess():

    HITS = 0
    MISSES = 0
    global a
    guess = input("Enter your guess here: \n")
    while len(guess) != 4:
        guess = input("Please enter a guess with 4 numbers: \n")
    if guess == num:
        print("YOU WIN!!!!!!!!!")
        a = True
        return HITS, MISSES
        

    for i in range(4):
        if guess[i] == num[i]:
            HITS += 1
        if guess[i] in num:
            MISSES += 1
    MISSES -= HITS
    a = False
    return HITS, MISSES

def play():
    global tries 
    tries = intro()
    while tries:
        HITS, MISSES = guess()
        if a == False:
            print("HITS: " + str(HITS))
            print("MISSES: " + str(MISSES))  
            tries -= 1  
        else:
            break
play()



