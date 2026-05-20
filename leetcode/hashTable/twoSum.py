def twoSum(nums, target) -> None:
    # OUTPUT: [0 , 1]

    seen = set()

    for i in range(len(nums)):
        x = target - nums[i]
        if nums[i] not in seen:
            seen.add(nums[i])
        else:
            return i, seen[x] # TO FIX

twoSum(nums = [2, 7, 11, 15], target = 9)