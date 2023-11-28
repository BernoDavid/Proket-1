import random

max_attempts = 7
lowest_number = 1
highest_number = 100

secret_number = random.randint(lowest_number, highest_number)

def get_guess():
    while True:
        try:
            guess = int(input(f"Gissa ett nummer mellan {lowest_number} och {highest_number}: "))
            if lowest_number <= guess <= highest_number:
                return guess
            else:
                print("Fungerar inte, gissa ett nummer mellan 1 och 100.")
        except ValueError:
            print("Fungerar inte, skriv ett nummer")

def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Rätt"
    elif guess < secret_number:
        return "För lågt"
    else:
        return "För högt"

def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guessed_number = get_guess()
        result = check_guess(guessed_number, secret_number)

        if result == "Rätt":
            print(f"Grattis, du gissade rätt tal {secret_number} på {attempts} försök.")
            won = True
            break
        else:
            print(f"{result}, försök igen")

    if not won:
        print(f"Tyvärr, du har slut på gissningar. Numret var {secret_number}.")

if __name__ == "__main__":
    print("Välkommen till mitt spel!")
    play_game()