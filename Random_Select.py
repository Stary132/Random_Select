import random

count = 2
random_range_max = 1e9


def Random_Select(start: int, end: int) -> None:
    actual = int(input("Please input an integer:"))
    random_value_int = random.randint(start, end)
    print("Random_value:", random_value_int)
    print("Result:", (random_value_int % actual) + 1)


for _ in range(0, count):
    Random_Select(1, random_range_max)
