# https://neetcode.io/problems/duplicate-integer
def hasDuplicate(nums):
    visited = []
    for x in nums:
        if(x in visited):
            return True
        else:
            visited.append(x)
    return False
print(hasDuplicate([1, 2, 3, 4]))
# Time complexity: O(n), Space complexity: O(n)
