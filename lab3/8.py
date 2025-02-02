def spy_game(nums):
    sequence = [0, 0, 7]
    index = 0

    for num in nums:
        if num == sequence[index]:
            index += 1
            if index == len(sequence):
                return True
    return False