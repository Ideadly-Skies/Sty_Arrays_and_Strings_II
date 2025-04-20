def has_subarray_sum(numbers, target_sum):
    # init pointers 
    i = 0
    j = i + 1

    while i < len(numbers):
        # sum adds up to target_sum
        if sum(numbers[i:j]) == target_sum:
            return True

        # reset counters
        if j >= len(numbers):
            i = i + 1
            j = i + 1

        # increment j
        j += 1

    # target_sum not found
    return False

if __name__ == "__main__":
    print(has_subarray_sum([1, 3, 1, 4, 3], 8)) # -> True
    print(has_subarray_sum([1, 3, 1, 4, 3], 2)) # -> False
    print(has_subarray_sum([1, 3, 1, 1, 3], 2)) # -> True