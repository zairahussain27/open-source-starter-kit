# Problem: Binary Search
# Difficulty: Easy
# Approach: Iterative
# Time Complexity: O(log n)
# Space Complexity: O(1)

"""
Problem Statement:
Given a sorted array of integers and a target value,
return the index of the target if found, else return -1.
"""

def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ---- Test Cases ----
if __name__ == "__main__":
    print(binary_search([1,2,3,4,5], 3))  # 2
    print(binary_search([1,2,3,4,5], 6))  # -1