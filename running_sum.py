def running_sum(numbers):
    for i in range(len(numbers)):
        if i > 0:
            numbers[i] = numbers[i] + numbers[i-1]
    return numbers
       
if __name__ == "__main__":
    print(running_sum([4, 2, 1, 6, 3, 6])) # -> [ 4, 6, 7, 13, 16, 22 ]
    print(running_sum([10, 5, -2, 1, 1])) # -> [ 10, 15, 13, 14, 15 ] 