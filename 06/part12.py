# Reading the input as a list of strings
with open("input.txt") as file_input:
    lines = [line.replace('\n','') for line in file_input.readlines()]

# Processing the list of operations at the last line
operations = lines[-1].split()
#print(operations)
number_of_columns = len(operations)
# Accuulating the values at the first line
accumulators = [int(v) for v in lines[0].split()]
#print(accumulators)
# Now reading next lines
for line in lines[1:-1]:
    values = [int(v) for v in line.split()]
    #print(values)
    # Just multiply/add and accumulate
    for i in range(number_of_columns):
        if operations[i] == '*':
            accumulators[i] *= values[i]
        elif operations[i] == '+':
            accumulators[i] += values[i]

print(f"Part 1: {sum(accumulators)}")

# Part 1 was easy. For part 2, we must group the values read as columns and apply the operation
total_acc = 0
number_of_rows = len(lines)-1
pos = 0
# For every group...
for c in range(number_of_columns):
    # This is the group accumulator
    col_acc = 0
    # Reading the digits for current column
    while pos < len(lines[0]):
        col_str = ''
        for r in range(number_of_rows):
            col_str += lines[r][pos]
        pos += 1
        # Is it at least one digit?
        if len(col_str.strip()) > 0:
            # Parse the digit
            col_val = int(col_str)
            #print(col_val)
            # If the first value for this group, just stores it.
            if( col_acc == 0 ):
                col_acc = col_val
            # If not first value, apply the operation
            elif operations[c] == '*':
                col_acc *= col_val
            elif operations[c] == '+':
                col_acc += col_val
        else:
            break
    # End of group. Accumulates the total results
    #print(col_acc)
    total_acc += col_acc

print(f"Part 2: {total_acc}")