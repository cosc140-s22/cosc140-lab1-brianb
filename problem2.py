#
# Name:
# Collaborator(s):
#
import math

lat1 = input("Location 1 latitude? ")
lon1 = input("Location 1 longitude? ")
lat2 = input("Location 2 latitude? ")
lon2 = input("Location 2 longitude? ")

lat1 = float(lat1)
lon1 = float(lon1)
lat2 = float(lat2)
lon2 = float(lon2)

lat1 = math.radians(lat1)
lon1 = math.radians(lon1)
lat2 = math.radians(lat2)
lon2 = math.radians(lon2)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = math.pow((math.sin(dlat/2)),2)+math.cos(lat1)*math.cos(lat2)*math.pow(math.sin(dlon/2),2)
c = 2 * math.atan2(math.sqrt(a),math.sqrt(1-a))
d = 3956 * c

print("Distance is: ",d)