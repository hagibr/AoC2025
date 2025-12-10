# Reading the input as a set of ordered pairs. They are the coordinates of the tiles.
with open("09/input.txt") as file_input:
    red_tiles = [tuple([int(v) for v in line.split(",")]) for line in file_input.readlines()]
    
max_area = 0

for i in range(len(red_tiles)-1):
    for j in range(i+1,len(red_tiles)):
        x_i,y_i = red_tiles[i]
        x_j,y_j = red_tiles[j]
        area = (abs(x_i-x_j)+1)*(abs(y_i-y_j)+1)
        if area > max_area:
            max_area = area

print(f"Part 1: {max_area}")

# OK, the red tiles are the vertices from a polygon
# Let's use this algorithm:
# We have 2 pairs of dots, (x_i, y_i) and (x_j, y_j) as diagonals of a rectangle
# The other 2 dots are (x_i, y_j) and (x_j, y_i)
# We just need to know if the rectangle is inside the polygon
# So we need to know if the sides of the rectangle are all inside the polygon
# Anyway, if we find one rectangle and it fits inside the polygon, we don't have to check any smaller rectangle

# Finding the borders from our polygon
borders = set()
for i in range(len(red_tiles)):
    x_i,y_i = red_tiles[i]
    x_j,y_j = red_tiles[(i+1) % len(red_tiles)]
    if x_i == x_j:
        if y_j < y_i:
          y_i, y_j = y_j, y_i
        for y in range(y_i,y_j+1):
            borders.add((x_i,y))
    elif y_i == y_j:
        if x_j < x_i:
            x_i, x_j = x_j, x_i
        for x in range(x_i,x_j+1):
            borders.add((x,y_i))
    else:
        print("Error")
# print(borders)

# Finding an tile that is internal 
min_x, min_y = red_tiles[0]
max_x, max_y = red_tiles[0]
for tile in red_tiles[1:]:
    x,y = tile
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

inside = borders.copy()
outside = set()
def is_inside(x,y):
    if (x,y) in inside:
        return True
    elif (x,y) in outside:
        return False

    count_cross = 0
    crossing = False
    for x_c in range(x, max_x):
        if (x_c, y) in borders:
            if not crossing:
                crossing = True
                count_cross += 1
        elif crossing:
          crossing = False
    if count_cross % 2 == 1:
        inside.add((x,y))
        return True
    outside.add((x,y))
    return False


# Now let's find the biggest rectangle that is inside the polygon

# I cheated a little. As I saw that my input polygon is something like a circle
# with 2 deviant red tiles (94876,50058) and (94876,48734) creating a gap in the circle,
# intuitively I know that the biggest rectangle have one of them in the diagonal,
# so we just have to evaluate rectangles above (94876,50058) and below (94876,48734)
# because the gap makes every rectangle with (94876,50058) as top to have tiles outside
# the polygon, and is does with every rectangle with (94876,48734)
# PS: I've tried other algorithms before, but all of them were too slow
max_area = 0
x_i, y_i = (94876,50058)
for i in range(len(red_tiles)):
    x_j,y_j = red_tiles[i]
    if( y_j > y_i ):
        if not is_inside(x_i,y_j) or not is_inside(x_j, y_i):
            continue
        area = (abs(x_i-x_j)+1)*(abs(y_i-y_j)+1)
        # Evaluating only bigger areas
        if area > max_area:
            max_area = area
            #print(max_area)

x_i, y_i = (94876,48734)
for i in range(len(red_tiles)):
    x_j,y_j = red_tiles[i]
    if( y_j < y_i ):
        if not is_inside(x_i,y_j) or not is_inside(x_j, y_i):
            continue
        area = (abs(x_i-x_j)+1)*(abs(y_i-y_j)+1)
        # Evaluating only bigger areas
        if area > max_area:
            max_area = area
            #print(max_area)   
            
print(f"Part 2: {max_area}")