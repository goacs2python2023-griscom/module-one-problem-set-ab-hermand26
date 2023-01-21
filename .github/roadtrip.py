def roadtripcost(distance, fuelefficiency, galloncost): 
    return int(distance/fuelefficiency) * galloncost 

print(roadtripcost(100, 20, 4))
