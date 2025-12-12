with open("12/input.txt") as file_input:
  data = file_input.readlines()
  presents_input = data[:30]
  regions_input = data[30:]

# Easy fits: the most area that a present uses is a 3x3 square, so if we analyze the total area
# and we can put all the presents without thinking on the geometry, just using 9 spaces, we have the
# easy fits total
total_easy_fit = 0
total_regions = 0
for regions in regions_input:
  width, length, q0, q1, q2, q3, q4, q5 = [int(v) for v in regions.replace('x', ' ').replace(':','').split()]
  if width*length >= (q0+q1+q2+q3+q4+q5)*9:
    total_easy_fit += 1
  total_regions += 1

print(total_easy_fit, total_regions)

#1000: too high
# 463: too low
# 487: OK
