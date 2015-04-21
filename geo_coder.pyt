__author__ = 'Andy Bell'
import arcpy
import geocoder


class Toolbox(object):
	def __init__(self):
		"""Define the toolbox (the name of the toolbox is the name of the
		.pyt file)."""
		self.label = "GeocodingTools"
		self.alias = "GeocodingTools"

		# List of tool classes associated with this toolbox
		self.tools = [GeocodeAddress]


class GeocodeAddress(object):
	def __init__(self):
		"""Define the tool (tool name is the name of the class)."""
		self.label = "GeocodeAddress"
		self.description = "Get's lat + long from an address supplied in attribute table"
		self.canRunInBackground = False

	def getParameterInfo(self):
		"""Define parameter definitions"""
		table = arcpy.Parameter(displayName="Address Table", name="table", datatype="DETable", parameterType="Required")

		st_no = arcpy.Parameter(displayName="Street Number", name="st_no", datatype="Field", parameterType="Optional")

		st_name = arcpy.Parameter(displayName="Street Name", name="st_name", datatype="Field", parameterType="Optional")

		city = arcpy.Parameter(displayName="City", name="city", datatype="Field", parameterType="Optional")

		state = arcpy.Parameter(displayName="State", name="state", datatype="Field", parameterType="Optional")

		zipcode = arcpy.Parameter(displayName="Zip Code", name="zipcode", datatype="Field", parameterType="Optional")

		st_no.parameterDependencies = [table.name]
		st_name.parameterDependencies = [table.name]
		city.parameterDependencies = [table.name]
		state.parameterDependencies = [table.name]
		zipcode.parameterDependencies = [table.name]

		params = [table, st_no, st_name, city, state, zipcode]
		return params


	def execute(self, parameters, messages):
		"""The source code of the tool."""

		# Get parameters and
		table = parameters[0].valueAsText
		number = parameters[1].valueAsText
		street = parameters[2].valueAsText
		city = parameters[3].valueAsText
		state = parameters[4].valueAsText
		zipcode = parameters[5].valueAsText

		# cursor to loop through attribute table

		cursor = arcpy.UpdateCursor(table)
		for row in cursor:
			# build address string in csv format
			full_address = number + " " + street + ", " + city + ", " + state + " " + zipcode
			arcpy.AddMessage(full_address)

			# geocoder.geocode(address)
		return