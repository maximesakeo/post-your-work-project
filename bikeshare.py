
bike = "Road Bike"
exists = any(bike.lower() in line.lower() for line in open("bikes.txt"))
print(exists)
