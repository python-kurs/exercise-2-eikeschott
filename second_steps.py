# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500
               }

# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500,
                "GEOS":2000,
                "worldview":0.31
               }

print("I have the following satellites in my database:", sat_database)

# 2) print out all satellite names contained in the dictionary [2P]

for sat in sat_database:
    print(sat)

# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]

print("Enter a satellite to get it's resolution:")
inp = input()


# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]

print("Enter a satellite to get it's resolution:")
inp = input()

if inp in sat_database:
    print("The requested satellite is in the database")
else:
    print("The requested satellite is not in the database")
    
    
# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P] 

print("Enter a satellite to get it's resolution:")
inp = input()

if inp in sat_database:
    print("The requested satellite is in the database\n", "\nName:", inp, "\nResolution:", sat_database[inp])
else:
    print("The requested satellite is not in the database")

