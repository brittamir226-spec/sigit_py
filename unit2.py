class FirstAnimal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

class Upgradedanimal:
    count_animals = 0
    def __init__(self, age, name = "Octavio"):
        self._name = name
        self._age = age
        Upgradedanimal.count_animals += 1

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

class Pixel:
    def __init__(self, x = 0, y = 0, red = 0, green = 0, blue = 0):
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        avg = (self._red + self._green + self._blue)//3
        self._red = avg
        self._green = avg
        self._blue = avg

    def print_pixel_info(self):
        color = ""
        if self._red == 0 and self._blue == 0 and self._green > 50:
            color = "Green"
        elif self._red == 0 and self._green == 0 and self._blue > 50:
            color = "Blue"
        elif self._green == 0 and self._blue == 0 and self._red > 50:
            color = "Red"

        print(f"X: {self._x}, Y: {self._y}, Color: ({self._red}, {self._green}, {self._blue}) {color}")

class BigThing:
    def __init__(self, thing):
        self._thing = thing

    def size(self):
        if isinstance(self._thing, int):
            return self._thing
        return len(self._thing)

class BigCat(BigThing):
    def __init__(self, thing, weight):
        BigThing.__init__(self, thing)
        self._weight = weight

    def size(self):

        if self._weight > 20:
            return "Very Fat"

        elif self._weight > 15:
            return "Fat"

        else:
            return "ok"


class Animal:
    """Represents an animal in the Hayaton zoo.
    :cvar zoo_name: the name of the zoo, shared by all animals
    """
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        """Initializes the animal's name and hunger level.
        :param name: the animal's name
        :param hunger: the animal's hunger level (default 0)
        :type name: str
        :type hunger: int
        :return: no return
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """Returns the animal's name.
        :return: the animal's name
        :rtype: str
        """
        return self._name

    def is_hungry(self):
        """Checks whether the animal is hungry (hunger level above 0).
        :return: True if the animal is hungry, otherwise False
        :rtype: bool
        """
        return self._hunger > 0

    def feed(self):
        """Lowers the animal's hunger level by 1.
        :return: no return
        """
        self._hunger -= 1

    def talk(self):
        """Makes the animal talk. Each subclass overrides this method.
        :return: no return
        """
        pass


class Dog(Animal):
    """Represents a dog."""

    def talk(self):
        """Prints what a dog says.
        :return: no return
        """
        print("woof woof")

    def fetch_stick(self):
        """Prints the dog's special line when it fetches a stick.
        :return: no return
        """
        print("There you go, sir!")


class Cat(Animal):
    """Represents a cat."""

    def talk(self):
        """Prints what a cat says.
        :return: no return
        """
        print("meow")

    def chase_laser(self):
        """Prints the cat's special line when it chases a laser.
        :return: no return
        """
        print("Meeeeow")


class Skunk(Animal):
    """Represents a skunk, which also has a stink count."""

    def __init__(self, name, hunger=0, stink_count=6):
        """Initializes the skunk using the Animal initializer, and adds a stink count.
        :param name: the skunk's name
        :param hunger: the skunk's hunger level (default 0)
        :param stink_count: how many times the skunk can stink (default 6)
        :type name: str
        :type hunger: int
        :type stink_count: int
        :return: no return
        """
        Animal.__init__(self, name, hunger)
        self._stink_count = stink_count

    def talk(self):
        """Prints what a skunk says.
        :return: no return
        """
        print("tsssss")

    def stink(self):
        """Prints the skunk's special line when it stinks.
        :return: no return
        """
        print("Dear lord!")


class Unicorn(Animal):
    """Represents a unicorn."""

    def talk(self):
        """Prints what a unicorn says.
        :return: no return
        """
        print("Good day, darling")

    def sing(self):
        """Prints the unicorn's special line when it sings.
        :return: no return
        """
        print("I'm not your toy...")


class Dragon(Animal):
    """Represents a dragon, which also has a color."""

    def __init__(self, name, hunger=0, color="Green"):
        """Initializes the dragon using the Animal initializer, and adds a color.
        :param name: the dragon's name
        :param hunger: the dragon's hunger level (default 0)
        :param color: the dragon's color (default "Green")
        :type name: str
        :type hunger: int
        :type color: str
        :return: no return
        """
        Animal.__init__(self, name, hunger)
        self._color = color

    def talk(self):
        """Prints what a dragon says.
        :return: no return
        """
        print("Raaaawr")

    def breath_fire(self):
        """Prints the dragon's special line when it breathes fire.
        :return: no return
        """
        print("$@#$#@$")


def main_animal():
    cat1 = FirstAnimal("snow", 10)
    cat2 = FirstAnimal("Lutzi", 3)
    cat2.birthday()
    print(cat1.get_age())
    print(cat2.get_age())

def main_upgraded_animal():
    animal1 = Upgradedanimal(3)
    animal2 = Upgradedanimal(10, "Snow")
    print(animal1.get_name())
    print(animal2.get_name())
    animal1.set_name("Lutzi")
    print(animal1.get_name())
    print(Upgradedanimal.count_animals)

def main_pixel():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()

def main_bigthingORcat():
    my_thing = BigThing("balloon")
    print(my_thing.size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size())

def main_Animal():
    """Creates the zoo animals, feeds the hungry ones, and makes every animal
       talk and use its special method.
       :return: no return
       """
    zoo_lst = []
    ob1 = Dog("Brownie", 10)
    ob2 = Cat("Zelda", 3)
    ob3 = Skunk("Stinky")
    ob4 = Unicorn("Keith", 7)
    ob5 = Dragon("Lizzy", 1450)
    zoo_lst.extend([ob1, ob2, ob3, ob4, ob5])

    ob6 = Dog("Doggo", 80)
    ob7 = Cat("Kitty", 80)
    ob8 = Skunk("Stinky Jr.", 80)
    ob9 = Unicorn("Clair", 80)
    ob10 = Dragon("McFly", 80)
    zoo_lst.extend([ob6, ob7, ob8, ob9, ob10])

    for animal in zoo_lst:
        if animal.is_hungry():
            print(f"{str(type(animal)).split('.')[1][:-2]} {animal.get_name()}")
            # also possible: type(animal).__name__ for clean type
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(Animal.zoo_name)






main_animal()
main_upgraded_animal()
main_pixel()
main_bigthingORcat()
main_Animal()