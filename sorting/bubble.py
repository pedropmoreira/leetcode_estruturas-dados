def bubble(nums):
    size = len(nums)

    for _ in nums:
        is_sorted = True
        print(nums)

        for i in range(size-1):
            is_sorted = True
            nums[i+1], nums[i] = nums[i], nums[i+1]
        if is_sorted:
            return