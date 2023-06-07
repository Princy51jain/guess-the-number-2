# Practice problem 6------------------>>>>>>>> Guess the number
import random

mn = int(input("Enter the lower bound of range: "))
mx = int(input("Enter the upper bound of range: "))

ran_num1 = random.randint(mn, mx)
print("Player 1:")
print("You have 7 number of guesses")
k1 = 1
while k1 <= 7:
    fst_inp = int(input("Please guess a number: "))
    if fst_inp > ran_num1:
        print("Wrong, guess a smaller number again")
    elif fst_inp < ran_num1:
        print("Wrong, guess a greater number again")
    else:
        print("Correct guess")
        print(f"You took {k1} number of guesses to complete the challenge.\n")
        break
    print("number of guesses left are ", 7 - k1)
    k1 = k1 + 1

if k1 > 7:
    print("GAME OVER!!!\n")

ran_num2 = random.randint(mn, mx)
print("Player 2:")
print("You have 7 number of guesses")
k2 = 1
while k2 <= 7:
    fst_inp = int(input("Please guess a number: "))
    if fst_inp > ran_num2:
        print("Wrong, guess a smaller number again")
    elif fst_inp < ran_num2:
        print("Wrong, guess a greater number again")
    else:
        print("Correct guess")
        print(f"You took {k2} number of guesses to complete the challenge.\n")
        break
    print("number of guesses left are ", 7 - k2)
    k2 = k2 + 1

if k2 > 7:
    print("GAME OVER!!!\n")

if k1 > k2:
    print("Player 2 wins!")
elif k1 < k2:
    print("Player 1 wins!")
else:
    print("It's a tie!")
