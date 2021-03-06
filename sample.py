def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            # We check whether the adjecent number is greater or not
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
bubble_sort(nums=[89,45,68,90,29,17])