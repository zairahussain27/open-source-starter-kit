# Problem: Two Sum
# Difficulty: Easy
# Approach: HashMap (single pass)
# Time Complexity: O(n)
# Space Complexity: O(n)

"""
Problem Statement:
Given an array of integers `nums` and an integer `target`,
return indices of the two numbers such that they add up to target.

Constraints:
- Each input has exactly one solution.
- You may not use the same element twice.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
"""

def two_sum(nums, target):
    """
    Finds two indices such that their values sum to target.

    Parameters:
    nums (list[int]): List of integers
    target (int): Target sum

    Returns:
    list[int]: Indices of the two numbers
    """
    seen = {}  # stores number -> index

    for i, num in enumerate(nums):
        complement = target - num

        # Check if complement already exists
        if complement in seen:
            return [seen[complement], i]

        # Store current number with index
        seen[num] = i

        # Example walkthrough:
        # nums = [2,7,11,15], target = 9
        # i=0 → num=2 → complement=7 → not found → store {2:0}
        # i=1 → num=7 → complement=2 → found → return [0,1]

    return []


# ---- Test Cases ----
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([3, 2, 4], 6))        # [1, 2]
    print(two_sum([3, 3], 6))           # [0, 1]
    print(two_sum([], 5))               # []