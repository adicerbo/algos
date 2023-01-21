# Beginner - Reduce but Grow
import math
def sum_array(a):
    total = (sum(a))
    return total

# Opposite number
def opposite(number):
    return -number

# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= (mpg * fuel_left):
        return True
    else: return False

# Century From Year
def century(years):
    return ((years-1) // 100) + 1

# A Needle in the Haystack
def find_needle(haystack):
    index = haystack.index("needle")
    print(index)
    return (f'found the needle at position {index}')

# Basic Mathematical Operations
def basic_op(operator, value1, value2):
    if operator == '+':
        return (value1 + value2)
    elif operator == '-':
        return (value1 - value2)
    elif operator == '*':
        return (value1 * value2)
    else:
        return (value1 / value2)

# Sum Mixed Array
def sum_mix(arr):
    nums_list = []
    for x in arr:
        nums = (int(x))
        nums_list.append(nums)
    print(nums_list)
    return (sum(nums_list))


# Beginner - Lost Without a Map
def maps(a):
    doubled = []
    for i in a:
        twice = i * 2
        doubled.append(twice)
    return (doubled)

# Number of People in the Bus
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

# Opposites Attract
def lovefunc(flower1, flower2):
    sum = flower1 + flower2
    print(sum % 2)
    if sum % 2 != 0:
        return True
    else:
        return False
print(lovefunc(2, 2))

# L1: Set Alarm
def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    else:
        return False

# MakeUpperCase
def make_upper_case(s):
    return s.upper()

# You only need one - Beginner
def check(arr, x):
    if x in arr:
        return True
    else: return False

# Invert values
def invert(lst):
    inverse = []
    for i in lst:
        inverse.append(-i)
    return (inverse)

# List Filtering
def filter_list(l):
    filtered = []
    for i in l:
        if isinstance(i, int):
            filtered.append(i)
    return (filtered)


# Sum of odd numbers
def row_sum_odd_numbers(n):
    return (n * n * n)

# Remove First and Last Character
def remove_char(s):
    return s[1:-1]

# Beginner - Reduce but Grow
def grow(arr):
    return (math.prod(arr))

# Jaden Casing Strings
def to_jaden_case(string):
    split = (string.split(' '))
    fixed = []
    for i in split:
        caps = (i.replace(i, i.capitalize()))
        fixed.append(caps)
    return (" ".join(fixed))

# Square(n) Sum
def square_sum(numbers):
    products = []
    for i in numbers:
        squared = i*i
        products.append(squared)
    return (sum(products))

# Get the Middle Character
def get_middle(s):
    if len(s)%2 == 1:
        return(s[int(len(s)/2)])
    else: return(s[int(len(s)/2) - 1] + s[int(len(s)/2)])

# Who likes it?
def likes(names):
    if names == []:
        return 'no one likes this'
    elif len(names) == 1:
        return (f'{names[0]} likes this')
    elif len(names) == 2:
        return (f'{names[0]} and {names[1]} like this')
    elif len(names) == 3:
        return (f'{names[0]}, {names[1]} and {names[2]} like this')
    else:
        return (f'{names[0]}, {names[1]} and {len(names) - 2} others like this')

# Take a Ten Minutes Walk
def is_valid_walk(walk):
    addends = []
    if len(walk) != 10:
        return False
    else:
        for direction in walk:
            if direction == 'n':
                addends.append(1)
            elif direction == 's':
                addends.append(-1)
            elif direction == 'e':
                addends.append(2)
            elif direction == 'w':
                addends.append(-2)
    if sum(addends) == 0:
        return True
    else:
        return False
# after looking at others solutions, I can see that I overthought this
# solution and could have just checked if the count of 'n' = count of 's'
# and vice versa for 'w' and 'e'

# Which are in?
def in_array(array1, array2):
    r = []
    for word in array1:
        for words in array2:
            if word in words:
                if word not in r:
                    r.append(word)
    r.sort()
    return r
