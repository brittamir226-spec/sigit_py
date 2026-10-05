from file1 import GreetingCard
from file2 import BirthdayCard

def main():
    card = GreetingCard()
    birthday_card = BirthdayCard(sender_age=30)
    card.greeting_msg()
    birthday_card.greeting_msg()

main()
