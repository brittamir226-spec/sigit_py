from functools import reduce
def double_letter(my_str):
    return ''.join(map(lambda x: x * 2, my_str))

def four_dividers(number):
    return list(filter(lambda a: a % 4 == 0, range(1, number + 1)))

def sum_of_digits(number):
    return reduce(lambda a, b: a + b, ezer(number), 0)

def ezer(num):
    lst = []
    while num > 0:
        lst.append(num % 10)
        num //= 10
    return lst


def intersection(list_1, list_2):
    return list(set(filter(lambda x: x in list_2, list_1)))

def is_prime(number):
    return number > 1 and len(list(filter(lambda x: number % x == 0, range(2, number)))) == 0

def is_funny(string):
    return not list(filter(lambda x: x != 'a' and x != 'h', string))

def find_pass(password):
    print(''.join(map(lambda x: chr(ord(x) + 2) if 65 <= ord(x) + 2 <= 90 or 97 <= ord(x) + 2 <= 122 else ' ', password)))

def find_longest():
    with open("names.txt", "r") as file:
        print(str(reduce(lambda x, y: x if len(x) > len(y) else y, file.read().split())))

def find_lengths():
    with open("names.txt", "r") as file:
        print(reduce(lambda a, b: a + len(b), file.read().split(), 0))

def find_short():
    with open("names.txt", "r") as file:
        cont = file.read()
        min_len = len(sorted(cont.split(), key = len)[0])
        print('\n'.join(list(filter(lambda x: len(x) == min_len, cont.split()))))

def write_lens():
    with open("name_length.txt", "w") as file:
        with open("names.txt", "r") as file1:
            file.write('\n'.join(map(lambda x: str(len(x)), file1.read().split())))

def get_lens():
    len1 =int(input("Enter name length:"))
    with open("names.txt", "r") as file1:
        print(('\n'.join(list(filter(lambda x: len(x) == len1, file1.read().split())))))


print(double_letter("python"))
print(double_letter("we are the champions!"))

print(four_dividers(9))
print(four_dividers(3))

print(sum_of_digits(104))

print(intersection([1, 2, 3, 4], [8, 3, 9]))
print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))

print(is_prime(42))
print(is_prime(43))

print(is_funny("hahahahahaha"))

password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
find_pass(password)

find_longest()
find_lengths()
find_short()
write_lens()
get_lens()