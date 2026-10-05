import winsound

freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }

notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

parts = notes.split("-")
print(type(parts))
print("__iter__" in dir(parts))

for part in parts:
    note, duration = part.split(",")
    winsound.Beep(freqs[note], int(duration))

class MusicNotes:
    def __init__(self):
        self._base = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self._octaves = 5
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._base) * self._octaves:
            raise StopIteration
        octave, note = divmod(self._index, len(self._base))
        self._index += 1
        return self._base[note] * 2 ** octave


notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)


def check_id_valid(id_number):
    """Checks whether an Israeli ID number is valid.
    Each digit is multiplied by 1 or 2 (alternating, starting with 1), digits of
    results above 9 are summed, and the total must be divisible by 10.
    :param id_number: the ID number to check
    :type id_number: int
    :return: True if the ID is valid, otherwise False
    :rtype: bool
    """
    return sum((lambda p: p // 10 + p % 10)(int(d) * (1 + i % 2))
               for i, d in enumerate(str(id_number).zfill(9))) % 10 == 0


class IDIterator:
    """An iterator that produces the valid ID numbers that come after a given ID."""

    def __init__(self, id_):
        """Initializes the iterator.
        :param id_: the ID number to start after (0 - 999999999)
        :type id_: int
        """
        self._id = id_

    def __iter__(self):
        """Returns the iterator itself."""
        return self

    def __next__(self):
        """Returns the next valid ID number, up to 999999999.
        :raises StopIteration: when there are no more valid IDs in the range
        :return: the next valid ID number
        :rtype: int
        """
        self._id += 1
        while self._id <= 999999999:
            if check_id_valid(self._id):
                return self._id
            self._id += 1
        raise StopIteration


def id_generator(id_number):
    """A generator function that produces the valid ID numbers that come after
    a given ID, up to 999999999.
    :param id_number: the ID number to start after
    :type id_number: int
    :return: a generator of valid ID numbers
    :rtype: generator
    """
    for number in range(id_number + 1, 1000000000):
        if check_id_valid(number):
            yield number


def main():
    id_number = int(input("Enter ID: "))
    choice = input("Generator or Iterator? (gen/it)? ")
    if choice == "it":
        source = IDIterator(id_number)
    else:
        source = id_generator(id_number)
    for _ in range(10):
        print(next(source))


if __name__ == "__main__":
    main()
