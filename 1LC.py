def twosum(nums, target):

    hash_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[num] = i


# Test: 
nums = [2, 7, 11, 15]
target = 9
print(twosum(nums, target))