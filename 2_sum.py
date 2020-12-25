"""
Given an array of integers, return indices of the two numbers such that they 
add up to a specific target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.
"""


def two_sum(nums, target: int):
    seen = dict()

    for i, num in enumerate(nums):
        partner = target - num

        if partner in seen:
            return [seen[partner], i]

        seen[num] = i

# TIME COMPLEXITY   O(n) #
# SPACE COMPLEXITY  O(n) #