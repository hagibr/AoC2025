# Reading the input as a list of strings
with open("input.txt") as file_input:
    lines = [list(line.replace('\n','')) for line in file_input.readlines()]
    
number_of_splits = 0
for r in range(1,len(lines)):
    for c in range(len(lines[r])):
        if lines[r-1][c] == 'S' or lines[r-1][c] == '|':
            if lines[r][c] == '.':
                lines[r][c] = '|'
            elif lines[r][c] == '^':
                lines[r][c-1] = '|'
                lines[r][c+1] = '|'
                number_of_splits += 1

print(f"Part 1: {number_of_splits}")

# This is our cache of timelines
timelines = dict()
# Analyzing a timeline for a tachyon
def analyze(r,c):
    # If not analyzed yet...
    if (r,c) not in timelines:
        # End of manifold
        if r >= len(lines)-1:
            timelines[(r,c)] = 1
        # Next is a free way...
        elif lines[r+1][c] == '|':
            timelines[(r,c)] = analyze(r+1,c)
        # Splitting...
        elif lines[r+1][c] == '^':
            timelines[(r,c)] = analyze(r+1,c-1) + analyze(r+1,c+1)
    
    return timelines[(r,c)]
    
# Now we just start analyzing the startig point
total_timelines = 0
for c in range(len(lines[0])):
    if lines[0][c] == 'S':
        total_timelines = analyze(0,c)

print(f"Part 2: {total_timelines}")
