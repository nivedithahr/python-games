answer = 5
print("Please guess number between  1 and 10")
guess = int(input())
if guess != answer:
    if guess <  answer:
        print("Please guess higher")
    else: #guess must be greater than answer
        print("Please guesss lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you have got it")
    else:
        print("Sorry, you have not guessed it")
else:
    print("you got it at first time")