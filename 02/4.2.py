nums = [0, 1, 7, 2, 4, 8]

if nums == []:
    print(0)
else:
    s = 0
    i = 0
    while i < len(nums):
        s = s + nums[i]
        i = i + 2

    result = s * nums[-1]
    print(result)