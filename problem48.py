import sys

sys.set_int_max_str_digits(50000)

sum = 0

for i in range(1, 1001):
    sum += i**i


print(str(sum)[-10:])