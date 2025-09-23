from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:

    # sort array
    nums.sort()

    # set n to length of an array
    n = len(nums) - 1

    result = []

    for i in range(len(nums)):
        # break out of loop if first number is greater than 0
        if nums[i] > 0:
            break
        # continue loop if the previous value is the same as current value r > 0 and nums[r] == nums[r - 1]
        elif r > 0 and nums[i] == nums[i - 1]:
            continue

        # set l pointer to next index or i in for loop
        l = i + 1
        # set an r pointer to the end of array
        r = n

        # start while loop
        while l < r:
            # calculate current sum nums[i] + nums[l] + nums[r]
            sum = nums[i] + nums[l] + nums[r]

            # if sum is equal to 0 then append the values to the result array [nums[i], nums[l], nums[r]]
            if sum == 0:
                result.append([nums[i], nums[l], nums[r]])
                # move pointers
                l += 1
                r -= 1
                # move the left pointer by one if the previous is the same value so while l < r and nums[l] == nums[l - 1]
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                # check the same for the right pointer
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1








