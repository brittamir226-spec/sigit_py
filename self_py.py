def exe2_5_2(tav):
    #tav = input("please guess a letter:")
     print(tav)
exe2_5_2('a')
def exe3_4_2(txt):
     #txt = input("please enter a string:")
     txt1 = txt[0] + txt[1:].replace('d', 'e')
     print(txt1)
exe3_4_2("ddar astronaut. pldase, stop drasing md!")
def exe3_4_3(txt):
    #txt = input("please enter a string:")
    lentxt = len(txt) // 2
    print(txt[:lentxt].lower() + txt[lentxt:].upper())
exe3_4_3("astronaut")
def exe3_5_2(word):
    #word = input("please enter a word:")
    print("_ " * len(word))
exe3_5_2("hangman")
def exe4_2_3(temp):
    #temp = input("insert the temperature you would like to convert:")
    num = float(temp[:-1])
    c_or_f = temp[-1].lower()
    if c_or_f == "c":
        print(str((9 * num + (32 * 5)) / 5) + "F")
    else:
        print(str((5 * num - 160) / 9) + "C")
exe4_2_3("10F")
def exe4_3_1(guess):
    #guess = input("guess a letter:")
    if len(guess) > 1 and not guess.isalpha():
        print("E3")
    elif not guess.isalpha():
        print("E2")
    elif len(guess) > 1 :
        print("E1")
    else:
        print(guess.lower())
exe4_3_1('a')
exe4_3_1('A')
exe4_3_1('$')
exe4_3_1('ab')
exe4_3_1('app$')
def distance(num1, num2, num3):
    if abs(num2 - num1) == 1 and abs(num3 - num1) >= 2 or abs(num2 - num1) >= 2 and abs(num3 - num1) == 1:
        return True
    else:
        return False
print(distance(1, 2, 10))
print(distance(4, 5, 3))
def is_valid_input(letter_guessed):
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) > 1 or not letter_guessed.isalpha():
        return False
    else:
        return True
print(is_valid_input('a'))
print(is_valid_input('A'))
print(is_valid_input('$'))
print(is_valid_input('ab'))
print(is_valid_input('app$'))
def format_list(my_list):
    print(', '.join(my_list[:-1:2]) + " and " + my_list[-1])
my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
format_list(my_list)
def are_lists_equal(list1, list2):
    if sorted(list1) == sorted(list2):
        return True
    else:
        return False
list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]
print(are_lists_equal(list1, list2))
print(are_lists_equal(list1, list3))
def check_valid_input(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) > 1 or not letter_guessed.isalpha() or letter_guessed in old_letters_guessed:
        return False
    else:
        return True
old_letters = ['a', 'b', 'c']
print(check_valid_input('C', old_letters))
print(check_valid_input('ep', old_letters))
print(check_valid_input('$', old_letters))
print(check_valid_input('s', old_letters))
def numbers_letters_count(my_str):
    lst = [0,0]
    for i in my_str:
        if i.isdigit():
            lst[0] += 1
        else:
            lst[1] += 1
    return lst
print(numbers_letters_count("Python 3.6.3"))
def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=lambda tup: float(tup[1]), reverse = True)
products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
print(sort_prices(products))
def count_chars(my_str):
    dict = {}
    for i in my_str:
        dict[i] = my_str.count(i)
    return dict
magic_str = "abra cadabra"
print(count_chars(magic_str))
def copy_file_content(source, destination):
    with open(source, 'r') as file1:
        txt = file1.read()
    with open(destination, 'w') as file2:
        file2.write(txt)
with open('copy.txt', 'w') as file1:
    file1.write("Copy this text to another file.")
with open('paste.txt', 'w') as file2:
    file2.write("-- some random text --")
copy_file_content("copy.txt", "paste.txt")
with open('paste.txt', 'r') as file2:
    print(file2.read())
