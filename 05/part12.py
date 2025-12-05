id_ranges = set()
id_ingredients = list()

# Reading the input
parsing_ranges = True
with open("05/input.txt") as file_input:
  line = file_input.readline()
  while len(line) > 0:
    if parsing_ranges:
      if line.find("-") > -1:
        r1,r2 = [int(v) for v in line.split('-')]
        id_ranges.add((r1,r2))
      else:
        parsing_ranges = False
    else:
      ingredient = int(line)
      id_ingredients.append(ingredient)
    line = file_input.readline()

#print(id_ranges)
#print(id_ingredients)

# Part 1: simple pass through every range, stopping when is already inside one of them
count_fresh = 0
for id in id_ingredients:
  for r1,r2 in id_ranges:
    if r1 <= id and id <= r2:
      count_fresh += 1
      break

print(f"Part 1: {count_fresh}")

# Part 2: let's merge the ranges to end only with disjunt ranges
#print(len(id_ranges))
merged_ranges = True
while merged_ranges:
  merged_ranges = False
  to_add = set()
  to_remove = set()
  for r1,r2 in id_ranges:
    for r3,r4 in id_ranges:
      if r1 != r3 or r2 != r4:
        if r1 <= r3 and r3 <= r2 and r2 <= r4:
          to_add.add((r1,r4))
          to_remove.add((r1,r2))
          to_remove.add((r3,r4))
          merged_ranges = True
        elif r3 <= r1 and r1 <= r4 and r4 <= r2:
          to_add.add((r3,r2))
          to_remove.add((r1,r2))
          to_remove.add((r3,r4))
          merged_ranges = True
        elif r1 <= r3 and r4 <= r2:
          to_remove.add((r3,r4))
          merged_ranges = True
        elif r3 <= r1 and r2 <= r4:
          to_remove.add((r1,r2))
          merged_ranges = True
  #print(len(id_ranges),len(to_remove),len(to_add))
  
  if merged_ranges:
    for r1,r2 in to_remove:
      id_ranges.remove((r1,r2))
    for r1,r2 in to_add:
      id_ranges.add((r1,r2))
  

#print(len(id_ranges))
# Now we count all the fresh ids with an easy operation
count_all_fresh = 0
for r1,r2 in id_ranges:
  count_all_fresh += (r2 - r1 + 1)

print(f"Part 2: {count_all_fresh}")