import sys
import os
import geocoder

print len(sys.argv)

# get folder location
wd = os.path.dirname(os.path.abspath(__file__))  # gets the path of *this file* and then gets the dir it's in
print(wd)

if len(sys.argv) == 2: # checks if a single argument was given

	# file name from system argument
	file_2B_geocoded = sys.argv[1]  # get's file name from argument provided from user

	# txt file with address data
	# address should be one line per address with no header
	address = os.path.join(wd, file_2B_geocoded)

	# base name of file
	base, extension = os.path.splitext(address)

	# output text file
	output = os.path.join(wd, base + "_geocoder_results" + extension) # adds geocoded_results to input file name

	print output
	geocoder.parse_file(address, output)

else:
	print("ERROR: please use text file name as a cmd line argument")