# Problem: Maximum Subarray (Kadane’s Algorithm)
# Difficulty: Medium
# Time Complexity: O(n)
# Space Complexity: O(1)

"""
Problem Statement:
Given an integer array nums, find the subarray with the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6
"""

def max_subarray(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum


# ---- Test Cases ----
if __name__ == "__main__":
    print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
    print(max_subarray([1]))  # 1
    print(max_subarray([5,4,-1,7,8]))  # 23
