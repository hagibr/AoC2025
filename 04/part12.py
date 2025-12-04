# Reading the input
with open("input.txt") as file_input:
  input = [list(line.replace('\n', '')) for line in file_input.readlines()]
  
# Part 1: just count the adjacent rolls
acessible = 0
for row in range(len(input)):
  for col in range(len(input[row])):
    if input[row][col] == '@':
      adjacent = 0
      for r in range(row-1,row+2):
        for c in range(col-1,col+2):
          if r >= 0 and r < len(input) and c >= 0 and c < len(input[row]) and not (r == row and c == col):
            if(input[r][c] == '@'):
              adjacent += 1
      if adjacent < 4:
        acessible += 1
        #print([row,col,adjacent])

print(f"Part 1: {acessible}")

# Part 2: remove acessible rolls and iterate
total_removed = 0
acessible = 1
while acessible > 0:
  acessible = 0
  to_remove = list()
  for row in range(len(input)):
    for col in range(len(input[row])):
      if input[row][col] == '@':
        adjacent = 0
        for r in range(row-1,row+2):
          for c in range(col-1,col+2):
            if r >= 0 and r < len(input) and c >= 0 and c < len(input[row]) and not (r == row and c == col):
              if(input[r][c] == '@'):
                adjacent += 1
        if adjacent < 4:
          acessible += 1
          to_remove.append([row,col])
          #print([row,col,adjacent])
  if acessible > 0:
    total_removed += acessible
    for r,c in to_remove:
      input[r][c] = 'X'
print(f"Part 2: {total_removed}")