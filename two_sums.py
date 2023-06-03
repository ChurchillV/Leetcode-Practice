"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def two_sums(target, nums):
    index1 = 0
    index2 = 0
    for i in range(0, len(nums)-1):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target and i != j:
                index1 = i
                index2 = j
    answers = (index1, index2)
    return answers


test_array = [2, 4, 5, 7]
print(two_sums(9, test_array))