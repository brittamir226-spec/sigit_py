import string
# def E_StopIteration():
#     f = filter(lambda x: x > 5, [1, 10])
#     print(next(f))
#     print(next(f))
#
#
# def E_ZeroDivisionError():
#     return 9 / 0
#
#
# def E_AssertionError():
#     assert 2 > 5
#
#
# def E_ImportError():
#     from math import d
#
#
# def E_KeyError():
#     d = {"a": 1}
#     d["b"]
#
#
# def E_SyntaxError():
#     exec("while True\n    print('Hi')")
#
#
# def E_IndentationError():
#     exec("d = 1\n    e = 2")
#
#
# def E_TypeError():
#     return 'h' + 4.3
#
# E_StopIteration()
# E_ZeroDivisionError()
# E_AssertionError()
# E_ImportError()
# E_KeyError()
# E_SyntaxError()
# E_IndentationError()
# E_TypeError()

def read_file(file_name):
    cont = ""
    try:
        file = open(file_name, "r")
        cont += "__CONTENT_START__\n"
    except FileNotFoundError:
        return "__CONTENT_START__\n__NO_SUCH_FILE__\n__CONTENT_END__"
    else:
        cont += f"{str(file.read())}\n"
        file.close()
    finally:
        cont += "__CONTENT_END__"
    return cont

class Underage(Exception):
    def __init__(self, age):
        self._age = int(age)
    def __str__(self):
        return f"Younger than 18, current age: {self._age}, {18 - self._age} years left "

def send_invitation(name, age):
    if int(age) < 18:
        raise Underage(age)
    else:
        print("You should send an invite to " + name)

def main_underage():
    ages = [17, 20]
    for age in ages:
        try:
            send_invitation("banana", age)
        except Underage as e:
            print(e)

def check_input(username, password):
    cnt = 0

    if len(username) < 3:
        raise UsernameTooShort
    elif len(username) > 16:
        raise UsernameTooLong
    elif not all(c.isalnum() or c == "_" for c in username):
        raise UsernameContainsIllegalCharacter(username)
    else:
        cnt += 1

    if len(password) < 8:
        raise PasswordTooShort
    elif len(password) > 40:
        raise PasswordTooLong
    elif not any(c.isupper() for c in password):
        raise Upper
    elif not any(c.islower() for c in password):
        raise Lower
    elif not any(c.isdigit() for c in password):
        raise Digit
    elif not any(c in string.punctuation for c in password):
        raise Special
    else:
        cnt += 1
    if cnt == 2:
        return "OK"




class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, user):
        self._user = user
    def __str__(self):
        index = 0
        punc = ""
        for i in range (len(self._user)):
            if not self._user[i].isalnum() or self._user[i] == "_":
                punc = self._user[i]
                index = i

        return f"The username contains an illegal character \"{punc}\" at index {index}"

class UsernameTooShort(Exception):
    def __str__(self):
        return "User has under 3 keys"

class UsernameTooLong(Exception):
    def __str__(self):
        return "User has more than 16 keys"

class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"

class PasswordTooShort(Exception):
    def __str__(self):
        return "password has under 8 keys"

class Upper(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"

class Lower(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"

class Digit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"

class Special(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


class PasswordTooLong(Exception):
    def __str__(self):
        return "password has more than 40 keys"

def main_check_input():
    tests = [("1", "2"),
             ("0123456789ABCDEFG", "2"),
             ("A_a1.", "12345678"),
             ("A_1", "2"),
             ("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary"),
             ("A_1", "abcdefghijklmnop"),
             ("A_1", "ABCDEFGHIJLKMNOP"),
             ("A_1", "ABCDEFGhijklmnop"),
             ("A_1", "4BCD3F6h1jk1mn0p"),
             ("A_1", "4BCD3F6.1jk1mn0p")]

    for username, password in tests:
        try:
            print(check_input(username, password))
        except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong,
                PasswordMissingCharacter, PasswordTooShort, PasswordTooLong) as e:
            print(e)



print(read_file("names.txt"))
print(read_file("smth.txt"))
main_underage()
main_check_input()