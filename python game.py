answer = "Head"
name = input("Welcome!, What is your Name : ")
age = int(input("How old are You {}?".format(name)))
if age < 16:
    print("Sorry come after {} years".format(16-age))
else:
    print("You are old enough..\tLet's Begin The guessing Game")
    print("*" * 80)
    output = input("Hello {}, I have tossed the coin...,Can you guess the output\nis it Head or Tail?".format(name))
    if output == answer:
        print("Yooh! you got it at first time")
    else:
        print("You didn't guess it correct, Try again {}\nYour answer : ".format(name))
        output = input()
        if output == answer:
            print("Well done, you got it right")
        else:
            print("Sorry you loose")
