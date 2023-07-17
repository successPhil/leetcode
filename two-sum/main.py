def twoSum(nums, target):
    numbers_seen = {}

    for idx, num in enumerate(nums):
        compliment = target - num
        if compliment in numbers_seen:
            return [numbers_seen[compliment], idx]
        numbers_seen[num] = idx

print(twoSum([2,7,11,15], 9))
print(twoSum([11,7,15,2], 9))
print(twoSum([11,7,15,2], 26))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))