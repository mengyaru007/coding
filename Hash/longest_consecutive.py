"""最长连续序列"""

def longest_consecutive(nums):
    if len(nums) == 0: return 0
    nums_set = set(nums)
    longest = 0
    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_streak = 1
            while current_num + 1 in nums_set:
                current_streak += 1
                current_num += 1
            longest = max(longest, current_streak)
    return longest

print(longest_consecutive([100,4,200,1,3,2]))