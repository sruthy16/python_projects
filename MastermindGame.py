import random


print("Welcome to the Mastermind game.")

num  =  random.randrange(1000, 10000)

guess = input("Guess a four digit number: ")

if num == guess:
    print("You are Mastermind")
else:
    ctr = 0
    while guess != num :
        ctr+=1
        count = 0
        num = str(num)
        correct = ["X"]*4

        for i in range(0,4):
            if guess[i] == num[i]:
                count+=1
                correct[i] = guess[i]
            else:
                continue

        if count < 4 and count!= 0 :
            print("Number is incorrect. But you did guess ", count, " digit(s) correctly.")
            print("These numbers in your guess were in the correct position.")
            for j in correct:
                print(j, end=" ")
            print("\n")
            print("\n")
            guess = input("Enter new guess: ")

        elif count == 0:
            print("None of the numbers entered match.")
            guess = input("Enter new guess: ")
    if guess == num:
        print("You are Mastermind.")
        print("It took you ", ctr,"tries.")


