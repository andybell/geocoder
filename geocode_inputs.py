import os
import geocoder

# file name
file_2B_geocoded = 'dairies_2_geo.txt' # TODO make this a cmd line input?

#get folder location
wd = os.path.dirname(os.path.abspath(__file__))  # gets the path of *this file* and then gets the dir it's in
print(wd)

# txt file with address data
# address should be one line per address with no header
address = os.path.join(wd, file_2B_geocoded)

# base name of file
base, extension = os.path.splitext(address)

# output text file
output = os.path.join(wd, base + "_geocoder_results" + extension) # adds geocoded_results to input file name

print output
geocoder.parse_file(address, output)