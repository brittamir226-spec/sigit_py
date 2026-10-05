def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    return " ".join(words[word] for word in sentence.split())

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primes_over(n):
    num = n + 1
    while True:
        if is_prime(num):
            yield num
        num += 1

def first_prime_over(n):
    return next(primes_over(n))
def parse_ranges(ranges_string):
    ranges = (r.split("-") for r in ranges_string.split(","))
    return (num for start, stop in ranges for num in range(int(start), int(stop) + 1))

def get_fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def gen_secs():
    """Generates all possible seconds (0-59)."""
    for sec in range(60):
        yield sec


def gen_minutes():
    """Generates all possible minutes (0-59)."""
    for minute in range(60):
        yield minute


def gen_hours():
    """Generates all possible hours (0-23)."""
    for hour in range(24):
        yield hour


def gen_time():
    """Generates every time of a day, starting from 00:00:00, as 'hh:mm:ss'."""
    for hour in gen_hours():
        for minute in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, minute, sec)


def gen_years(start=2019):
    """Generates the given year and every year after it."""
    while True:
        yield start
        start += 1


def gen_months():
    """Generates all the months of a year (1-12)."""
    for month in range(1, 13):
        yield month


def gen_days(month, leap_year=True):
    """Generates the days (1..N) of the given month.
    :param month: the month number (1-12)
    :param leap_year: True if the year is a leap year
    """
    if month == 2:
        days_in_month = 29 if leap_year else 28
    elif month in (4, 6, 9, 11):
        days_in_month = 30
    else:
        days_in_month = 31
    for day in range(1, days_in_month + 1):
        yield day


def is_leap_year(year):
    """Returns True if the year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def gen_date():
    """Generates full date and time signatures: dd/mm/yyyy hh:mm:ss."""
    for year in gen_years():
        for month in gen_months():
            for day in gen_days(month, is_leap_year(year)):
                for time in gen_time():
                    yield "%02d/%02d/%04d %s" % (day, month, year, time)


def main():
    # gen_time test (prints 86,400 lines):
    # for gt in gen_time():
    #     print(gt)

    # first three dates
    gen = gen_date()
    for _ in range(3):
        print(next(gen))

    # print the value after every 1,000,000 iterations
    gen = gen_date()
    count = 0
    printed = 0
    while printed < 3:
        date = next(gen)
        count += 1
        if (count - 1) % 1000000 == 0 and count > 1:
            print(date)
            printed += 1


print(translate("el gato esta en la casa"))
print(first_prime_over(1000000))
print(list(parse_ranges("1-2,4-4,8-10")))
print(list(parse_ranges("0-0,4-8,20-21,43-45")))
fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))

if __name__ == "__main__":
    main()

