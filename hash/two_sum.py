"""两数之和"""

def two_sum(nums, target):
    hash_nums = {}
    for index, value in enumerate(nums):
        if value in hash_nums.keys():
            return [index, hash_nums[value]]
        hash_nums.update({target - value: index})
    return None
