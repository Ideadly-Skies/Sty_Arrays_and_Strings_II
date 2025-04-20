def subarray_sum_count(numbers, target_sum):
  # init counter
  i = 0
  j = i + 1
  count = 0

  while i < len(numbers):
    # check if sum to target_sum
    if sum(numbers[i:j]) == target_sum:
       print(numbers[i:j])
       count += 1

    # reset counter
    if j >= len(numbers):
        i = i + 1 
        j = i
    
    # increment j counter
    j += 1
  
  # return count
  return count 

if __name__ == "__main__":
   subarray_sum_count([1, 3, 1, 4, -2, 3], 5) # -> 3