def max_circular_absolute_difference(nums):
    n = len(nums)
    max_diff = 0
    for i in range(n):
        next_i = (i + 1) % n  # circular index
        diff = abs(nums[i] - nums[next_i])
        max_diff = max(max_diff, diff)
    return max_diff

# Test: 

print(max_circular_absolute_difference([4, 8, 6, 1]))  # Output: 5