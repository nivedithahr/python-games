answer = 5
print("please guess the number between 1 and 10")
guess = int(input())
if guess < answer:
    print("please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you got it")
    else:
        print("Sorry, you have not guessed the correct answer")
elif guess > answer:
    print("please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you got it")
    else:
        print("Sorry, you have not guessed the correct answer")
else:
    print("Congragulations, you got it at first time")