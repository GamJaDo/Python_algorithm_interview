"""
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]
"""
"""
def twoSum(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]:
            print(nums.index(n), nums[i+1:].index(complement)+(i+1))
"""
"""
def twoSum(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target-num in nums_map and i!=nums_map[target-num]:
            return [i, nums_map[target-num]]
"""
def twoSum(nums, target):
    left, right = 0, len(nums)-1
    nums
    while left!=right:
        if nums[left]+nums[right] == target:
            return [left, right]
        elif nums[left]+nums[right] < target:
            left += 1
        elif nums[left]+nums[right] > target:
            right -= 1

    return None

nums = [2, 7, 11, 15]
target = 9        
print(twoSum(nums, target))
