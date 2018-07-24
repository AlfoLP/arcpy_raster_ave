#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Alfonsina
#
# Created:     19/07/2018
# Copyright:   (c) Alfonsina 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
arcpy.CheckOutExtension("spatial")

#set input, output and workspace folders
InputFolder_alfo = "C:/Users/Alfonsina/Desktop/Distance"
arcpy.env.workspace = InputFolder_alfo
OutputFolder_alfo = "C:\Users\Alfonsina\Desktop\Distance\output_prueba_alfo"

# Set the extent environment using a keyword. MAXOF=La extensi?n combinada
#de todos los datos de entrada. Se procesar?n todas las entidades o las celdas.
arcpy.env.extent = "MAXOF"

#Create a raster list of all raster files in input folder
raslist = arcpy.ListRasters("*", "All")
print raslist

# Run cell statistics
calc = arcpy.sa.CellStatistics(raslist, statistics_type = "MEAN", ignore_nodata = "DATA")
calc.save(r'C:\Users\Alfonsina\Desktop\Distance\output_prueba_alfo\raster-04.img')