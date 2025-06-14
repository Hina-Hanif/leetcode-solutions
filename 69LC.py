def mysqrt(x):
    if x < 2:
        return x
    left, right = 0, x
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right

# Test:

print(mysqrt(16))

