def get_guess():
    while True:
        try:
            guess = int(input("Pick a number between 0 and 20: "))
            if 0 <= guess <= 20:
                return guess
            else:
                print("Please pick a number between 0 and 20.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    attempts = 3
    while attempts > 0:
        guess = get_guess()
        if guess == 6:
            print("Congratulations, you guessed the number!")
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Sorry, wrong guess. {attempts} attempts left.")
            else:
                print("Sorry, you've used all attempts.")

if __name__ == "__main__":
    play_game()
