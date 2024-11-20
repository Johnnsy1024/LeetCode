def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]  # 把基准数放到中间
    return i + 1


def quick_sort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)
        quick_sort(nums, low, pi - 1)
        quick_sort(nums, pi + 1, high)


if __name__ == "__main__":
    nums = [10, 7, 8, 9, 1, 5]
    quick_sort(nums, 0, len(nums) - 1)
    print("Sorted array is:", nums)
