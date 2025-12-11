with open("11/input.txt") as file_input:
  lines = file_input.readlines()

devices = dict()
for line in lines:
  dev, outs = line.split(":")
  devices[dev] = outs.split()
#print(devices)

# This is our cache for speeding the tree search
path_cache = dict()
def count_paths(current_path:set, current_device:str):
  if current_device == "out":
    return 1
  elif current_device in current_path:
    return 0
  elif current_device in path_cache:
    return path_cache[current_device]
  total_paths = 0
  new_path = current_path.union({current_device})
  for output in devices[current_device]:
    total_paths += count_paths(new_path, output)

  path_cache[current_device] = total_paths
  return total_paths

count = count_paths(set(), "you")

print(f"Part 1: {count}")

# Modifying the function for part 2. Now we have to specify the end device and the list of devices to avoid
def count_paths2(current_path:set, current_device:str, end_device:str, avoid_devices:list[str]):
  if current_device == end_device:
    #print(current_path)
    return 1
  elif current_device in avoid_devices:
    return 0
  elif current_device in current_path:
    return 0
  elif current_device in path_cache:
    return path_cache[current_device]

  total_paths = 0
  new_path = current_path.union({current_device})
  for output in devices[current_device]:
    total_paths += count_paths2(new_path, output, end_device, avoid_devices)
  
  path_cache[current_device] = total_paths
  return total_paths

# Calculating the size of 3 disjoint sets
path_cache = dict()
count_svr_fft = count_paths2(set(), "svr", "fft", ["dac", "out"]) # All the paths from svr to fft that doesn't pass through dac nor out
path_cache = dict()
count_fft_dac = count_paths2(set(), "fft", "dac", ["out"])        # All the paths from fft to dac that doesn't pass through out 
path_cache = dict()
count_dac_out = count_paths2(set(), "dac", "out", ["fft"])        # All the paths from dac to out that doesn't pass through fft

# By multiplying the size of these sets, we have the count of all the paths that goes from svr->fft->dac->out (bit set "A")
print(f"Part 2: svr->fft:{count_svr_fft}, fft->dac:{count_fft_dac}, dac->out:{count_dac_out}, svr->fft->dac->out: {count_svr_fft*count_fft_dac*count_dac_out}")

# Now we do the same for svr->dac->fft->out, creating another big set "B"
path_cache = dict()
count_svr_dac = count_paths2(set(), "svr", "dac", ["fft", "out"])
path_cache = dict()
count_dac_fft = count_paths2(set(), "dac", "fft", ["out"])
path_cache = dict()
count_fft_out = count_paths2(set(), "fft", "out", ["dac"])

print(f"Part 2: svr->dac:{count_svr_dac}, dac->fft:{count_dac_fft}, fft->out:{count_fft_out}, svr->dac->fft->out: {count_svr_dac*count_dac_fft*count_fft_out}")

# And we can sum these 2 big disjoint sets "A" and "B"
print(f"Part 2: {count_svr_fft*count_fft_dac*count_dac_out+count_svr_dac*count_dac_fft*count_fft_out}")
