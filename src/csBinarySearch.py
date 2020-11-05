from typing import List

def csBinarySearch(nums: List[int], target: int) -> int:
    min = 0
    max = len(nums) - 1 
    while not max < min:

        guess = (max + min) // 2

        if nums[guess] == target:
            return guess

        elif nums[guess] < target:
            min = guess + 1

        else:
            max = guess - 1

    return -1
  
print(csBinarySearch([-1,0,3,5,9,12], 9))