# function that want

def showing_hangman(hang_man,wrong_attempts):
    for x in hang_man[wrong_attempts]:
        print(x)

def show_the_word(hidden_progress):
    return " ".join(hidden_progress)



def hidden_letter_guessed(guess_letter, hidden_word,hidden_progress):
    for i in range(len(hidden_word)):
        if hidden_word[i] == guess_letter:
            hidden_progress[i] = guess_letter
    print(show_the_word(hidden_progress))
    return hidden_progress

def the_display(hang_man, wrong_attempts, guess_letter, hidden_word, hidden_progress):
    print("~~~~~~~~~~~~~~~~")
    showing_hangman(hang_man, wrong_attempts)
    hidden_letter_guessed(guess_letter, hidden_word, hidden_progress)
    print("\n~~~~~~~~~~~~~~~~\n")
