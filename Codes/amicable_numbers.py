# The problem
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#Evaluate the sum of all the amicable numbers under 10000.

def proper_divisors_sum(x):
    # this part of the code do all the calculation, looking for the divisors and summing them up
    sum = 0
    for number in range(1,x+1):
        if (x%(number) == 0 and number < x):
            sum = sum + number
    return sum

def amicable(x):
    
    # this validates if the number is amicable or not, based on the sums returned
    sum = proper_divisors_sum(x)
    second_sum = proper_divisors_sum(sum)
    third_sum = proper_divisors_sum(second_sum)

    if (x == second_sum and sum == third_sum and x != sum):
        return x
    return 0

sum = 0
for number in range(1,10000):
    sum = sum + amicable(number)
print(sum)

