# Reading the input
with open("input.txt") as file_input:
  input = [line.replace('\n', '') for line in file_input.readlines()]

# Just for conference
# print(input)

# Part 1: password is the counter of times it stopped at 0
position = 50
password = 0
for line in input:
  direction, amount = line[0], int(line[1:])
  if( direction == 'L' ):
    position = (position - amount) % 100
  else:
    position = (position + amount) % 100
  # Stopped at 0?
  if position == 0:
    password = password + 1

print(f"Part 1: {password}")

# Part 2: password is the counter of times it passed throuth 0. Brute force, not optimizing, it's already fast.
position = 50
password = 0
for line in input:
  direction, amount = line[0], int(line[1:])
  if( direction == 'L' ):
    for i in range(amount):
      position = (position - 1) % 100
      # Passing through 0?
      if position == 0:
        password = password + 1
  else:
    for i in range(amount):
      position = (position + 1) % 100
      # Passing through 0?
      if position == 0:
        password = password + 1

print(f"Part 2: {password}")