def hangmanstart():
  """Prints the starting captions of the game.
  :return: no return
  """
  HANGMAN_ASCII_ART = """   _    _                                         
  | |  | |                                        
  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
  |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
  | |  | | (_| | | | | (_| | | | | | | (_| | | | |
  |_|  |_|\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                      __/ |                      
                     |___/"""
  MAX_TRIES = 6
  print(" Welcome to the game \n" + HANGMAN_ASCII_ART + "\n" , MAX_TRIES)

def check_win(secret_word, old_letters_guessed):
    """Checks if the list old_letters_guessed contains one of the letters in the secret word.
    :param secret_word: the secret word that needs to be guessed throughout the game
    :param old_letters_guessed: the list of letters the player has guessed
    :type secret_word: string
    :type old_letters_guessed: list
    :return: whether the list contains letters from the secret word or not
    :rtype: bool
    """
    for i in secret_word:
        if not i in old_letters_guessed:
            return False
    return True
    
def show_hidden_word(secret_word, old_letters_guessed):
    """Shows the length of the secret word and the letters that were guessed correctly.
    :param secret_word: the secret word that needs to be guessed throughout the game
    :param old_letters_guessed: the list of letters the player has guessed
    :type secret_word: string
    :type old_letters_guessed: list
    :return: the secret word using only '_' and the letters that were guessed correctly
    :rtype: string
    """
    lines = ""
    for i in secret_word:
        if i in old_letters_guessed:
            lines += i + " "
        else:
            lines += "_ "
    print(lines)      
    
def check_valid_input(letter_guessed, old_letters_guessed):
    """Checks whether letter_guessed is valid or not according to the game's criteria (doesnt contain notes other then letters, doesnt previously appear in old_letters_guessed and only has 1 letter).
    :param letter_guessed: the user's guess
    :param old_letters_guessed: the list of letters the player has guessed
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: whether letter_guessed is valid or not
    :rtype: bool
    """
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) > 1 or not letter_guessed.isalpha() or letter_guessed in old_letters_guessed:
        return False
    else:
       return True
       
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """Checks if the guessed lettter is valid (using check_valid_input) and if it is the guess is added to the list of old_letters_guessed. if not the old letters will be shown .
    :param letter_guessed: the letter the player has guessed
    :param old_letters_guessed: the list of letters the player has guessed
    :type letter_guessed: string
    :type old_letters_guessed: list
    :return: whether the guess is valid or not
    :rtype: bool 
    """
    letter_guessed = letter_guessed.lower()
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("X")
        print("-> ".join(old_letters_guessed))
        return False
        
def choose_word(file_path, index):
  """chooses the secret word from the file the user has entered its path and the index of the secret word in that file.
  :param file_path: a path to the file that contains random words
  :param index: the index of the secret word in the file
  :type file_path: string
  :type index: int
  :return: a tuple with the number of words in the file (without double words) and the chosen word
  :rtype: tuple
  """
  with open(file_path, 'r') as file:
    wordlst = file.read().split(' ')
  lst = sorted(wordlst, key = lambda x: x[0]) #sorts the word list accoroing the fisrt letter of each word (abc)
  newwordlst = []
  for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
            newwordlst.append(lst[i]) 
  for word in newwordlst:
    if lst[-1] != word:
      newwordlst.append(lst[-1]) 
      break  
  index = index % len(wordlst)      
  tup = (len(newwordlst), wordlst[index - 1])      
  return(tup)
  
def print_hangman(num_of_tries):
    """Prints the hangman board according the number of the mistakes the player has made (not more then 6).
    :param num_of_tries: the number of failures the player has made (guessing incorrect letters)
    :type num_of_tries: int
    :return: no return
    """
    HANGMAN_PHOTOS = {
    "1": "x-------x",
    "2": """x-------x
|
|
|
|
|""",
    "3": """x-------x
|       |
|       0
|
|
|""",
    "4": """x-------x
|       |
|       0
|       |
|
|""",
    "5": """x-------x
|       |
|       0
|      /|\\
|
|""",
    "6": """x-------x
|       |
|       0
|      /|\\
|      /
|""",
    "7": """x-------x
|       |
|       0
|      /|\\
|      / \\
|"""
    }   

    print(HANGMAN_PHOTOS[str(num_of_tries)])
    
    
def main():    
 hangmanstart()
 with open("words.txt", 'w') as file:
   file.write("cat hangman song most broadly is a song hangman work music work broadly is typically")
 userfile = input("Please enter the files link:")
 userindex = int(input("please enter the wanted word's index:"))
 print_hangman(1)
 SECRET_WORD = choose_word(userfile, userindex)[1]
 number_of_failures = 1
 print("_ " * len(SECRET_WORD))
 old_letters_guessed = []  
 round_number = 1
 while number_of_failures <= 6 and check_win(SECRET_WORD, old_letters_guessed) == False:
    print("ROUND NUMBER: ", round_number)
    userguess = input("Please enter your guess:")
    while try_update_letter_guessed(userguess, old_letters_guessed) == False:
        userguess = input("Please enter an appropriate guess:")
    show_hidden_word(SECRET_WORD, old_letters_guessed)
    if not userguess.lower() in SECRET_WORD:
        number_of_failures += 1
        print(":(")
        print_hangman(number_of_failures)
    round_number += 1
 if check_win(SECRET_WORD, old_letters_guessed):
    print("WIN")
 else:
    print("LOSE")
    print("The secret word was: ", SECRET_WORD)
if __name__ == "__main__":
    main()
