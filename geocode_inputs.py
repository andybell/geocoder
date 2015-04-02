import os
import geocoder

#get folder location
wd = os.path.dirname(os.path.abspath(__file__))  # gets the path of *this file* and then gets the dir it's in
print(wd)

# address path one line per address
address = os.path.join(wd, 'address_list.txt')

# output shapefile
output = os.path.join(wd, 'output_geocoder.txt')

geocoder.parse_file(address, output)