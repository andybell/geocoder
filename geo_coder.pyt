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
        params = None
        return params


    def execute(self, parameters, messages):
        """The source code of the tool."""
        return