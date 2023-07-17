def twoSum(numbers, target):
    left_idx, right_idx = 0, len(numbers)-1

    while left_idx < right_idx:
        current_sum = numbers[left_idx] + numbers[right_idx]
        if current_sum > target:
            right_idx -= 1
        elif current_sum < target:
            left_idx += 1
        else:
            return [left_idx + 1, right_idx + 1]
    return []

print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1,0], -1))
print(twoSum([1,3,4,7,9,10,12,15,19,25], 25))
    
