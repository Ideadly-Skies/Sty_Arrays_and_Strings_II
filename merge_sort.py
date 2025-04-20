def merge_sort(nums):
  # base case
  if len(nums) <= 1:
    return nums
  
  # recursive case
  mid = len(nums) // 2
  left = merge_sort(nums[:mid])
  right = merge_sort(nums[mid:])
  
  # merging left and right subtrees
  return merge(left, right)

def merge(left, right):
  # init list and pointers
  merged = []
  i = j = 0
  
  # merging step
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1

  # add remaining elements
  merged.extend(left[i:])
  merged.extend(right[j:])
  
  # return merged list
  return merged

if __name__ == "__main__":
  numbers = [10, 4, 42, 5, 8, 100, 5, 6, 12, 40]
  print(merge_sort(numbers)) # -> [ 4, 5, 5, 6, 8, 10, 12, 40, 42, 100 ]