from typing import List


def removeDuplicates( nums: List[int]) -> int:
    # First ask if there are duplicates by asking,
    # if set of nums is equally big like nums
    if len(nums) == len(set(nums)):
        return len(nums)
    else:
        test = []
        p = 0
        # Stop loop when the current char is "_"
        while  nums[p] != "_":
            # if the number was already picked, remove it, append
            # a "_" char
            if nums[p] in test:
                nums.pop(p)
                nums.append("_")
            else:
                # if it was seen the first time, append it to test
                test.append(nums[p])
                p += 1
        nums = test
        # Return the number of unique Elements
        return len(test)








#       j = 1
#       for i in range(1, len(nums)):
#           if nums[i] != nums[i-1]:
#               nums[j] = nums[i]
#               j +=1
#       print(f"after nums {nums}")
#       return j


print(removeDuplicates([1, 1, 2]))