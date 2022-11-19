import math
def sum_array(a):
    total = (sum(a))
    return total


def opposite(number):
    return -number


def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= (mpg * fuel_left):
        return True
    else: return False


def century(years):
    return ((years-1) // 100) + 1


def find_needle(haystack):
    index = haystack.index("needle")
    print(index)
    return (f'found the needle at position {index}')


def basic_op(operator, value1, value2):
    if operator == '+':
        return (value1 + value2)
    elif operator == '-':
        return (value1 - value2)
    elif operator == '*':
        return (value1 * value2)
    else:
        return (value1 / value2)


def sum_mix(arr):
    nums_list = []
    for x in arr:
        nums = (int(x))
        nums_list.append(nums)
    print(nums_list)
    return (sum(nums_list))


def maps(a):
    doubled = []
    for i in a:
        twice = i * 2
        doubled.append(twice)
    return (doubled)


def number(bus_stops):
    entry = []
    exit = []
    for i in bus_stops:
        entered = (i[0])
        entry.append(entered)
        exited = i[1]
        exit.append(exited)
    sums = sum(entry)
    loss = sum(exit)
    return (sums-loss)


def lovefunc(flower1, flower2):
    sum = flower1 + flower2
    print(sum % 2)
    if sum % 2 != 0:
        return True
    else:
        return False
print(lovefunc(2, 2))


def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    else:
        return False


def make_upper_case(s):
    return s.upper()


def check(arr, x):
    if x in arr:
        return True
    else: return False


def invert(lst):
    inverse = []
    for i in lst:
        inverse.append(-i)
    return (inverse)


def filter_list(l):
    filtered = []
    for i in l:
        if isinstance(i, int):
            filtered.append(i)
    return (filtered)


def row_sum_odd_numbers(n):
    return (n * n * n)


def remove_char(s):
    return s[1:-1]


def grow(arr):
    return (math.prod(arr))
