def add_one(some_list):
    result = some_list[:]
    carry = 1

    for i in range(len(result) - 1, -1, -1):
        new_digit = result[i] + carry
        result[i] = new_digit % 10
        carry = new_digit // 10
        if carry == 0:
            break

    if carry:
        result.insert(0, carry)

    return result


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'

print("OK")