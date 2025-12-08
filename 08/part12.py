# Reading the input as a set of ordered triplets
with open("08/input.txt") as file_input:
    junctions = [tuple([int(v) for v in line.split(",")]) for line in file_input.readlines()]


# Calculating the distances between all junctions
def calc_distance(j1,j2):
    return (j1[0]-j2[0])**2 + (j1[1]-j2[1])**2 + (j1[2]-j2[2])**2

# Let's store them as lists containing the two junctions and the distance between them
distances = list()
longest_distance = 0
for a in range(len(junctions)-1):
    for b in range(a+1,len(junctions)):
        j1,j2 = junctions[a], junctions[b]
        dist = calc_distance(j1,j2)
        distances.append([j1,j2,dist])
        if longest_distance < dist:
            longest_distance = dist
# Sorting by distance
distances.sort(key=lambda x: x[2])

# Initializes the circuits with only one junction
circuits = dict()
for j in junctions:
    circuits[j] = {j}
# Doing the 10/1000 merges:
for _ in range(1000): 
  # Get the first pair of junctions (shortest distance)
  j1,j2,dist = distances[0]
  # Merge the circuits
  c1:set = circuits[j1]
  c2:set = circuits[j2]
  if c1 != c2:
    new_circuit = c1.union(c2)
    for j in new_circuit:
        circuits[j] = new_circuit
  # Removing the used pair from distances list
  distances.remove([j1,j2,dist])

#print(circuits)

# Creating a list of unique circuits
unique_circuits = list()
for j in circuits.keys():
    if circuits[j] not in unique_circuits:
        unique_circuits.append(circuits[j])
# Sort them by number of junctions (highest to lowest)
unique_circuits.sort(key=len, reverse=True)
#print(unique_circuits, len(unique_circuits))

# Now the product of size of the 3 largest circuits
largest_product = 1
for c in unique_circuits[:3]:
    largest_product *= len(c)

print(f"Part 1: {largest_product}")

# Continuing the merges until we have a circuit with all the junctions
while True:
  # Get the first pair of junctions (shortest distance)
  j1,j2,dist = distances[0]
  # Merge the circuits
  c1:set = circuits[j1]
  c2:set = circuits[j2]
  if c1 != c2:
    new_circuit = c1.union(c2)
    # End of merges?
    if len(new_circuit) == len(junctions):
      print(f"Part 2: {j1[0]*j2[0]}")
      break
    for j in new_circuit:
        circuits[j] = new_circuit
  # Removing the used pair from distances list
  distances.remove([j1,j2,dist])