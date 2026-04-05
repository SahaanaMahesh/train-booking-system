#routes.py to store the data about source,destination and distance
#distance is in kms and the distance func returns the distance between the source and destination
routes = {
    ("NEW DELHI", "MUMBAI") : 1460,
    ("NEW DELHI", "KOLKATA") : 1525,
    ("NEW DELHI", "CHENNAI") : 2200,
    ("NEW DELHI", "HYDERABAD") : 1670,
    ("MUMBAI", "KOLKATA") : 1970,
    ("MUMBAI", "CHENNAI") : 1300,
    ("MUMBAI","HYDERABAD"): 711,
    ("KOLKATA", "CHENNAI") : 1200,
    ("KOLKATA", "HYDERABAD") : 1600,
    ("CHENNAI", "HYDERABAD") : 633 
           }
def get_distance(source,destination): 
    source = source.upper()
    destination = destination.upper()
    if (source,destination) in routes:
        return routes[(source,destination)] 
    elif (destination,source) in routes:
        return routes[(destination,source)]
    else:
        return None