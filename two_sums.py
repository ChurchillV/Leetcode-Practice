"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def two_sums(target, nums):
    index1 = 0
    index2 = 0
    for i in range(0, len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target and i != j:
                index1 = i
                index2 = j
                print( f"Elements summing up to {target} can be found at indexes: {index1}, {index2}")
                return
            elif i >= len(nums)-1 and index2 == 0:
                print("No values available")


test_array = [2, 4, 5, 7]
target_value = 11
two_sums(target_value, test_array)