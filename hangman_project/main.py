# main body
import random
from words import hangman_words
from functions import showing_hangman, show_the_word, the_display

hang_man ={0:("      ",
              "      ",
              "      "),

         1:("  o   ",
            "      ",
            "      "),

         2:("  o   ",
            "  |   ",
            "      "),

         3:("  o   ",
            "/ |   ",
            "      "),

         4:("  o   ",
            "/ | \\",
            "      "),

         5:("  o   ",
            "/ | \\",
            " /    "),

         6:("  o   ",
            "/ | \\",
            " / \\ "),

           }

full_running = True

while full_running:

    inside_running = True
    wrong_attempts = 0
    hidden_word = random.choice(hangman_words)
    hidden_progress = ["_" for _ in hidden_word]

    print("~~~~~~~~~~~~~~~~")
    showing_hangman(hang_man, wrong_attempts)
    print(show_the_word(hidden_progress))
    print("\n~~~~~~~~~~~~~~~~\n")

    while inside_running :

        if "_" not in hidden_progress:
            print("--- YOU WON ---")
            print(f"Yes the answer is {hidden_word}")
            inside_running = False


        guess_letter = input("Enter a letter [type 'exit' to end the game]-- ").lower()

        if guess_letter == "exit" :
            print("------ BYE ------\n"
                  "SEE YOU NEXT TIME")
            inside_running = False
            full_running = False

        elif len(guess_letter) != 1 or not guess_letter.isalpha():
            print("invalid input")
            the_display(hang_man, wrong_attempts, guess_letter, hidden_word, hidden_progress)
            continue

        elif guess_letter in hidden_word:
            the_display(hang_man, wrong_attempts, guess_letter, hidden_word, hidden_progress)


        else:
            wrong_attempts += 1
            the_display(hang_man, wrong_attempts, guess_letter, hidden_word, hidden_progress)

            if wrong_attempts == 6:
                print("\n-- YOU LOST --")
                print(f"The correct answer is {hidden_word}\n")
                inside_running = False
