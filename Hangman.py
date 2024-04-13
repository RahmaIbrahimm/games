import random as rand
#print the rules of the game 
def rules():
    '''
    Prints the rules of the game
    '''
    game_rules = '''Welcome to Hangman!

Hangman is a word-guessing game where you'll try to uncover a hidden word by guessing one letter at a time. Here's how it works:

1. The computer will select a random word, and your goal is to guess that word.
2. The word is represented by a series of underscores, with each underscore representing a letter in the word.
3. You can guess one letter at a time. If the letter is in the word, all instances of that letter will be revealed.
4. You have a limited number of incorrect guesses. Once you reach the maximum number of incorrect guesses, the game is over.
5. Be careful not to guess the same letter more than once, and only guess letters (no numbers or symbols).

To make a guess, simply enter a letter when prompted. After each guess, the computer will provide feedback, showing you which letters are correct and revealing their positions in the word.

If you successfully guess all the letters and uncover the entire word before running out of incorrect guesses, you win! Otherwise, the game ends, and the correct word is revealed.

Are you ready to play Hangman? Let's see if you can uncover the mystery word!

'''
    return game_rules
#Choose a category 
def category():
    '''
    asks the player to choose a category
    
    '''
    while True:
        ctg = input('''Choose one of the following categories:
1 - animals
2 - countries
3 - programming languages
4 - Social Media Platforms
Your choice is number :
''')
        try :
            ctg=int(ctg.strip())
            if 1 <= ctg <= 4:
                return ctg
            else: 
                print("Invalid choice.Please enter a number between 1 and 4,")
        except ValueError:
                print("Invalid input. Please enter a number.")
                
#Have a list of the items in each category
animals = [
    "elephant", "giraffe", "kangaroo", "leopard", "rhinoceros",
    "chimpanzee", "cheetah", "penguin", "crocodile", "ostrich",
    "porcupine", "platypus", "panther", "koala",  
    "cat", "dog", "bird", "fish", "frog",
    "rabbit", "turtle", "mouse", "horse", "snake","fox"
]
programming_languages = [
    "python", "java", "javascript", "ruby",
    "php", "html", "css", "typescript", "swift",
    "go", "kotlin", "rust", "perl", "r",
    "dart", "haskell", "matlab"
]
social_media_platforms = [
    "facebook", "instagram", "twitter", "linkedin", "snapchat",
    "pinterest", "tiktok", "reddit", "whatsapp", "telegram",
    "youtube"
]
countries = [
    "afghanistan", "albania", "algeria", "andorra", "angola",
    "antigua", "argentina", "armenia", "australia", "austria",
    "azerbaijan", "bahamas", "bahrain", "bangladesh", "barbados",
    "belarus", "belgium", "belize", "benin", "bhutan",
    "bolivia", "bosnia", "botswana", "brazil", "brunei",
    "bulgaria", "burkina", "burundi", "cabo verde", "cambodia",
    "cameroon", "canada", "central african republic", "chad", "chile",
    "china", "colombia", "comoros", "congo", "costa rica",
    "usa", "russia", "india", "china", "brazil",
    "canada", "france", "germany", "japan", "uk"
]
#choose the secret words from the lists
def get_secret_word():
    '''
    Find the secret word according to the category
    
    '''
    #Ask for the category
    match(category()):
         #each choosen category get the secret word from 
        case 1:
            print("Your category of choice is Animals!\nGood Luck!")
            # Randomize a word from the choosen categroy's list
            return rand.choice(animals) 
        case 2:
            print("Your category of choice is Countries!\nGood Luck!")
            # Randomize a word from the choosen categroy's list
            return rand.choice(countries)  
        case 3:
            print("Your category of choice is Programming languages!\nGood Luck!")
            # Randomize a word from the choosen categroy's list
            return rand.choice(programming_languages) 
        case 4:
            print("Your category of choice is Social Media Platforms!\nGood Luck!")
            # Randomize a word from the choosen categroy's list
            return rand.choice(social_media_platforms)       
# use the functions to play the game
def play():
    rules()
    #turn the word into a list
    secret_word = list(get_secret_word())                  
    secret = secret_word.copy()
    
    #find the length to print the number of underscores
    number_of_underscores = len(secret_word)
    underscores = "_"*number_of_underscores
    print(' '.join(underscores))
    underscores = list(underscores)
    
    '''
    dog
      _ o _
    '''
    # pop the correctly guessed letters until there is none , then the game ends
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    number_guesses = 5
    while number_of_underscores > 0 and number_guesses > 0:
        #User guesses letters
        # let the player take a guess
        guess = input("Guess a letter from a to z : ").strip().lower()
        #checks if the guess is a letter in the alphabet.
        if guess.isalpha() and len(guess)==1:
        #Check if the letter has been guessed before.
            if guess not in letters:
                print("This letter has already been guessed.")
                continue
            #the number of guesses
            #remove the guessed letter from the letters list
            letters.pop(letters.index(guess))
            #check if the letter is present in the secret word
            if guess in secret_word:
                #if the letter is correct replace each underscore with the letters using a while loop
                while guess in secret_word:
                    ind = secret_word.index(guess)
                    secret_word[ind] = 1
                    #---------------
                    underscores[ind] = guess       
                    number_of_underscores-=1
                
                print("Good job!")
                print(*underscores)
                continue  
            else:
                number_guesses -= 1
                print(f"Incorrect guess! {number_guesses} {'guess' if number_guesses == 1 else 'guesses'} left.")
                continue   
        # the guess is not an alphabet
        else:
            print("Please only choose a letter from the English Alphabet.")
            continue
    # if the number of guesses are gone or the word is guesses correctly (no missing letters i.e. no underscores)    
    if number_guesses == 0:
        print(f"Good luck next time :( , the word was {''.join(secret)}" )
    else:    
        print(f"Good job the word was {''.join(secret)} and the number of wrong guesses is {5-number_guesses}")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes" or play_again == 'y':
        play()
    else:
        print("Thanks for playing!\n")

