def minimizemax(nums, p):
    nums.sort()

    def can_form_pairs(max_diff):
        count = 0
        i = 1
        
        while i < len(nums):
            if nums[i] - nums[i - 1] <= max_diff: 
                count += 1
                i += 2  # skip the next index to avoid reusing
            else:
                i += 1
        return count >= p

    left, right = 0, nums[-1] - nums[0]
    while left < right:
        mid = (left + right) // 2
        if can_form_pairs(mid):
            right = mid
        else:
            left = mid + 1

    return left


nums = [1, 3, 6, 19, 20]
p = 2
print(minimizemax(nums, p)) 