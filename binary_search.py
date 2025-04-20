def binary_search(numbers, target):
    # dict to store number and its index
    dict = {}

    for i, num in enumerate(numbers):
      dict[num] = i 

    # recursive case
    return _binary_search(numbers, target, dict)

def _binary_search(numbers, target, dict):
    # target not found 
    if numbers == []:
       return -1

    # base case and recursive cases 
    mid = len(numbers) // 2
    if numbers[mid] == target:
       return dict[target] 
    if numbers[mid] < target:
       return _binary_search(numbers[mid+1:], target, dict)
    if numbers[mid] > target:
       return _binary_search(numbers[:mid], target, dict)


if __name__ == "__main__":
   print(binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8], 6))        # -> 6
   print(binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 27)) # -> -1
   print(binary_search([0, 6, 8, 12, 16, 19, 20, 28], 8))      # -> 2