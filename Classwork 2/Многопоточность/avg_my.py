import threading

numbers = tuple(range(50))
# tuple - кортеж(неизменяемый список)
result = 0

def avg(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    avg_number = sum / len(nums)
    return avg_number

a = avg(numbers)
print(a)

# 24.5
