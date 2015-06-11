import os
import csv
from geopy import geocoders
from osgeo import ogr, osr


def geocode(address):
	g = geocoders.GoogleV3()
	place, (lat, lng) = g.geocode(address)
	print '%s: %.5f, %.5f' % (place, lat, lng)
	return place, lat, lng


def parse_file2shp(filepath, output_shape):
	# create the shapefile
	drv = ogr.GetDriverByName("ESRI Shapefile")
	if os.path.exists(output_shape):
		drv.DeleteDataSource(output_shape)
	ds = drv.CreateDataSource(output_shape)
	# spatial reference
	sr = osr.SpatialReference()
	sr.ImportFromProj4('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
	lyr = ds.CreateLayer(output_shape, sr, ogr.wkbPoint)
	# fields
	featDefn = lyr.GetLayerDefn()
	fld_id = ogr.FieldDefn('id', ogr.OFTInteger)
	fld_address = ogr.FieldDefn('ADDRESS', ogr.OFTString)
	fld_address.SetWidth(255)
	lyr.CreateField(fld_id)
	lyr.CreateField(fld_address)
	print 'Shapefile %s created...' % ds.name
	# read text addresses file
	i = 0
	f = open(filepath, 'r')
	for address in f:
		try:
			print 'Geocoding %s' % address
			place, lat, lng = geocode(address)
			point = ogr.Geometry(ogr.wkbPoint)
			point.SetPoint(0, lng, lat)
			feat = ogr.Feature(lyr.GetLayerDefn())
			feat.SetGeometry(point)
			feat.SetField('id', i)
			feat.SetField('ADDRESS', address)
			lyr.CreateFeature(feat)
			feat.Destroy()
			i = i + 1
		except:
			print 'Error, skipping address...'


def parse_file(filepath, output_file):
	# read text addresses file
	matches = []
	f = open(filepath, 'r')
	for address in f:
		try:
			print 'Geocoding %s' % address
			row = geocode(address)
			print row
			matches.append(row)

		except:
			print 'Error, skipping address...'

	# write out lat/long to txt file
	with open(output_file, 'wb') as csvfile:
		writer = csv.writer(csvfile)
		for row in matches:
			writer.writerow(row)
			print row