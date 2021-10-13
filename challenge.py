answer = 5
print("please guessa number between 1 and 10 : ")
guess  = int(input())
if guess == answer:
    print("You got it at first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done you got it")
    else:
        print("Sorry, you have not guessed it")

