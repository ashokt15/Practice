# https://neetcode.io/problems/duplicate-integer
def hasDuplicate(nums):
    seen=[]
    for x in (nums):
      if x == x+1:
        print("given set has duplicate numbers")
      for x in range(len(nums)):
         seen=nums(x)
         for y in range(x+1,len(nums))
         if (seen==num(y))
         break
          return true
         else False
print(hasDuplicate([1, 2, 3, 4]))
# Time complexity: O(n), Space complexity: O(n)
