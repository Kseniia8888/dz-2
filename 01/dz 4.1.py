def move_zeros_to_end(numbers):
    result = []
    zeros = 0

    for x in numbers:
        if x == 0:
            zeros += 1
        else:
            result.append(x)

    result.extend([0] * zeros)
    return result


nums = [0, 1, 0, 12, 3]
answer = move_zeros_to_end(nums)
print(answer)
