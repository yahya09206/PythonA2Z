from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:

    # sort array
    nums.sort()

    # set n to length of an array
    n = len(nums) - 1

    result = []

    for i in range(len(nums)):
        # break out of loop if the first number is greater than zero which will mean the rest are higher since the array is sorted
        # so none of the indexes will equal to zero
        if nums[i] > 0:
            break
        # continue aka skip loop if the previous value is the same as current value r > 0 and nums[r] == nums[r - 1]
        # this prevents duplicate triplets
        elif i > 0 and nums[i] == nums[i - 1]:
            continue

        # set l pointer to start after current number located in nums[i]
        l = i + 1
        # set an r pointer to the end of array
        r = n

        # start while loop and keep going as long as the left pointer is to the left of the right pointer
        while l < r:
            # calculate current sum nums[i] + nums[l] + nums[r]
            sum = nums[i] + nums[l] + nums[r]

            # if sum is equal to 0 then append the values to the result array [[nums[i], nums[l], nums[r]]
            # we found our triplets
            if sum == 0:
                result.append([nums[i], nums[l], nums[r]])
                # move pointers inward to look for more triplets
                l += 1
                r -= 1
                # move the left pointer by one if the previous is the same value so while l < r and nums[l] == nums[l - 1]
                # essentially skipping duplicate numbers on the left side
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                # check the same for the right pointer and skip duplicates on the right side
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            # if the sum is less than zero, move the left pointer to get a bigger sum
            elif sum < 0:
                l += 1
            # if the sum is greater than zero, move the right pointer to get a smaller sum
            else:
                r -= 1
    # return result array and give back all the triplets that were found
    return result


print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([0,1,1]))
print(three_sum([0,0,0]))




