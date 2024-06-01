def find_number(nums):
    expect_sum = (len(nums) + 1) * (len(nums) + 2) // 2
    real_sum = sum(nums)
    return expect_sum - real_sum


if __name__ == "__main__":
    nums = input().split()
    print(find_number(nums))
