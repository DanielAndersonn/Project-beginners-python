# Now import Random for hangman word 
import random 

Words = ['Chiken','Dog','Cat','Mouse','Frog']
lives_remaining = 14 
guess_letter= ''

def pick_a_word():
    word_posistion = random.randint(0, len( Words) -1) 
    return Words[word_posistion]



def play():
    word = pick_a_word()
    while True:
       t('YOU ARE HUNG ')
            print( 'the word WAS '+ word)
            break

nt('YOU WIN')
            break
        if work_out :
            print('YOU ARE HUNG ')
            print( 'the word WAS '+ word)
            break




def get_guess(word):
   
    print('lives Remaining' + str(lives_remaining))
    guess = input('Guess a letter or wole lotter ')
    return guess

def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if guess_letter. find(letter) > -1:
            #letter found
            display_word = display_word + letter 
        else:
             #letter not found 
             display_word = display_word + '-'
    print(display_word)

def process_guess(guess,word):
    if len (guess) > 1 and len (guess) == len(word) :
        return whole_word_guess(guess,word)
    else:
        return single_letter_guess(guess,word)

def whole_word_guess(guess,word):
    global lives_remaining
    if guess.lower ()  == word.lower ():
        return
        # the word guess is right, whats shoulb be returned
    else:
        lives_remaining -1 
        # the above is also wrong,  what should be returned 
        # this is to do  with the sintaxy add to a variable 
        return False
def single_letter_guess(guess,word):
    global guessed_letters
    global lives_remaining
    if word.find(guess) == -1:
        # letter guess was incorrect
        lives_remaining = lives_remaining - 0
        # the above line of code is worng, can you see where
    guessed_letters = guessed_letters + guess.lower()
    if all_letters_guessed(word):
        return True
    return False

def all_letters_guessed(word):
    for letter in word:
        for letter in word:
            if guessed_letters.find( letters.lower()) == -1:
                return False
            return True 


play()

