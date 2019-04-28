from functools import reduce

nums = [3, 2, 5, 6, 7, 1, 9, 8]

evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)

doubles = list(map(lambda n: n * 2, evens))
print(doubles)

sum = reduce(lambda a, b: a + b, doubles)
print(sum)