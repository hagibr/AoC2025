# Reading the input
with open("input.txt") as file_input:
  input = file_input.readlines()[0]

# For part 1, it's a simple split of 2 halves and comparing them
ranges = input.split(',')
sum_invalid = 0
for r in ranges:
  r1, r2 = [int(v) for v in r.split('-')]
  for v in range(r1,r2+1):
    s = str(v)
    sl = len(s)
    # Only when the stringfyed form has even size
    if( sl % 2 == 0 ):
      if( s[:sl//2] == s[sl//2:] ):
        sum_invalid += v

print(f"Part 1: {sum_invalid}")

# For Part 2, let's analyze every case
sum_invalid = 0
for r in ranges:
  r1, r2 = [int(v) for v in r.split('-')]
  for v in range(r1,r2+1):
    # With 2 digits, both must be the same
    if 11 <= v and v <= 99:
      # Or in other words, it must be multiple of 11
      if v % 11 == 0:
        sum_invalid += v
    # With 3 digits, all of them must be the same
    elif 111 <= v and v <= 999:
      if v % 111 == 0:
        sum_invalid += v
    # With 4 digits, they can 2 pairs of 2 digits (which includes the all-the-same)
    elif 1010 <= v and v <= 9999:
      if v % 101 == 0:
        sum_invalid += v
    # With 5 digits, must be all the same
    elif 11111 <= v and v <= 99999:
      if v % 11111 == 0:
        sum_invalid += v
    # With 6 digits, can be 3 pairs or 2 three-of-a-kind (which includes the all-the-same)
    elif 100100 <= v and v <= 999999:
      if v % 10101 == 0 or v % 1001 == 0:
        sum_invalid += v
    # With 7 digits, must be all the same
    elif 1111111 <= v and v <= 9999999:
      if v % 1111111 == 0:
        sum_invalid += v
    # With 8 digits, can be 4 pairs or 2 four-of-a-kind (which includes the all-the-same)
    elif 10001000 <= v and v <= 99999999:
      if v % 1010101 == 0 or v % 10001 == 0:
        sum_invalid += v
    # With 9 digits, can be 3 three-of-a-kind (which includes the all-the-same)
    elif 100100100 <= v and v <= 999999999:
      if v % 1001001 == 0:
        sum_invalid += v
    # With 10 digits, can be 5 pairs or 2 five-of-a-kind (which includes the all-the-same)
    elif 1000010000 <= v and v <= 9999999999:
      if v % 101010101 == 0 or v % 100001 == 0:
        sum_invalid += v
    
print(f"Part 2: {sum_invalid}")

