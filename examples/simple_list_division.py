from random import randint

from divisiblelist import DivisibleList

MIN, MAX = 0, 9999
DIVISOR = 100
NUMBER_OF_ITEMS = DIVISOR * 10

if __name__ == "__main__":

    huge_list = DivisibleList(
        [randint(MIN, MAX) for __ in range(NUMBER_OF_ITEMS)]
    )

    small_list = [sum(i) / DIVISOR for i in huge_list / DIVISOR]

    print(small_list)
