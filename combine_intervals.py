def combine_intervals(intervals):
  # preprocessing step
  intervals.sort()
  
  # sorted intervals
  combined_intervals = []

  for interval in intervals:
    # append first interval
    if not combined_intervals:
      combined_intervals.append(interval) 
    else:
      # derive first and last elements
      first_incoming, last_incoming = interval
      first_last, last_last = combined_intervals[-1] 

      # overlap
      if first_last <= first_incoming <= last_last:
        # extend last_last interval
        if last_incoming > last_last:
          combined_intervals[-1] = (first_last, last_incoming)

      # do not overlap
      else:
        # add to the combined intervals
        combined_intervals.append(interval)

  # return combined_intervals
  return combined_intervals
    
if __name__ == "__main__":
  intervals = [
    (1, 4),
    (12, 15),
    (3, 7),
    (8, 13),
  ]
  print(combine_intervals(intervals)) # -> [ (1, 7), (8, 15) ]

  intervals = [
    (3, 7),
    (10, 13),
    (5, 8),
    (27, 31),
    (1, 5),
    (12, 16),
    (20, 32),
  ]
  print(combine_intervals(intervals)) # -> [ (1, 8), (10, 16), (20, 32) ]