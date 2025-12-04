# Reading the input
with open("input.txt") as file_input:
  input = [line.replace('\n', '') for line in file_input.readlines()]

total_jolts = 0
for line in input:
  # Step 1: find the highest value from right to left
  max_tens = 0
  pos_max_tens = len(line)-2
  for a in range(len(line)-2,-1,-1):
    v = int(line[a])
    if v >= max_tens:
      max_tens = v
      pos_max_tens = a
  #    print(f"Tens: {v}")
  # Step 2: Starting at the highest tens, find the hightest digit going to right
  max_units = 0
  for b in range(pos_max_tens+1,len(line)):
    v = int(line[b])
    if v >= max_units:
      max_units = v
  #    print(f"Units: {v}")
  max_jolts = 10*max_tens + max_units
  #print(max_jolts)
  total_jolts += max_jolts

print(f"Part 1: {total_jolts}")

# Part 2:
# Algorithm:
# There are 100 digits, so we can first find the highest from index 0 until index 88.
# Then we select the 12 highest from left to right, within the limit of 12

total_jolts = 0
for line in input:
  last_msd_pos = -1 # position of last MSD (most significant digit)
  max_jolts = 0     # max jolts for this battery
  for remaining_digits in range(12,0,-1):
    highest_value = 0
    highest_position = len(line)-remaining_digits
    # Finding the highest value within the allowed range
    for a in range(len(line)-remaining_digits,last_msd_pos,-1):
      value = int(line[a])
      if( value >= highest_value ):
        highest_value = value
        highest_position = a
    # Updating the jolts for this battery with this value
    max_jolts = max_jolts*10+highest_value
    #print(max_jolts)
    last_msd_pos = highest_position
  total_jolts += max_jolts

print(f"Part 2: {total_jolts}")
