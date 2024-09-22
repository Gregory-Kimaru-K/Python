import random
def guessGame():
    num = random.randint(1, 100)
    guess = None
    closerange = 10
    while guess != num:
        try:
            user_guess = input('Guess the number\n(Hint it is between 1 and 100): ')
            
            guess = int(user_guess)

            if guess < 1 or guess > 100:
                print("Invalid guess number between 1 and 100")
                continue

            else:
                if guess == num:
                    print('Congratulations! Your answer is correct.')
                elif guess < num:
                    if num - guess <= closerange:
                        print("Almost there just a bit higher")

                    else:
                        print("Too low!")
                
                elif guess > num:
                    if guess - num <= closerange:
                        print("Almost there a bit lower")

                    else:
                        print("Too high")
        
        except ValueError:
            print("Please enter a valid number.")

guessGame()