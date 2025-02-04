nums = input()
first_nums =list(map(int, nums.split()))
def is_prime(n):
    if n <=1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        else:
            return True
        
def filter_prime(first_nums):
    return [number for number in first_nums if is_prime(number)]

prime = filter_prime(first_nums)
print("Prime numbers:", prime)
