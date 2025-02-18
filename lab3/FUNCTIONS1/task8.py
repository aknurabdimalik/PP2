def spy_game(nums):
    seq = [0, 0, 7]
    index = 0
    for num in nums:
        if num == seq[index]:
            index += 1
        if index == 3:  
            return True
    return False

print()  

