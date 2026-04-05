# fare.py - to calculate the fare

from trains import train_types
from classes import travel_classes

def slab_fare(distance):
    fare = 100.0
    if distance <= 100:
        fare += distance * 1.0
    elif distance <= 300:
        fare += (100 * 1.0) + ((distance - 100) * 0.8)
    else:
        fare += (100 * 1.0) + (200 * 0.8) + ((distance - 300) * 0.6)
    return fare


def senior_discount(fare, age):
    if age > 60:
        return fare * 0.6
    return fare


def normalize_train(train_type):
    train_type = train_type.strip().upper()
    train_type = train_type.replace("-", " ")
    train_type = " ".join(train_type.split())
    if train_type == "SUPERFAST":
        return "SUPERFAST"
    elif train_type == "EXPRESS":
        return "EXPRESS"
    elif train_type == "FAST PASSENGER":
        return "FAST PASSENGER"
    else:
        return None
    

def normalize_class(travel_class):
    travel_class = travel_class.strip().upper()
    travel_class = travel_class.replace("-", " ")
    travel_class = " ".join(travel_class.split())
    if travel_class == "AC 2 TIER":
        return "AC 2-TIER"
    elif travel_class == "AC 3 TIER":
        return "AC 3-TIER"
    elif travel_class == "SLEEPER":
        return "SLEEPER"
    else:
        return None
    

def train_premium(fare, train_type):
    return fare * train_types[train_type]["premium"]


def class_premium(fare, travel_class):
    return fare * travel_classes[travel_class]["multiplier"]


def baggage_fee(weight, travel_class):
    allowed = travel_classes[travel_class]["baggage"]
    if weight > allowed:
        return (weight - allowed) * 15
    return 0


def surcharge(train_type):
    return train_types[train_type]["surcharge"]


def apply_promo(total, code):
    code = code.strip().upper()
    if code == "ADG20":
        total *= 0.8
    elif code == "WINTER500":
        total = max(0, total - 500)
    elif code == "":
        pass
    else:
        print("Invalid promo code. No discount applied.")
    return round(total, 2)


def calculate_time(distance, train_type):
    speed = train_types[train_type]["speed"]
    time_hours = distance / speed
    hours = int(time_hours)
    minutes = int((time_hours - hours) * 60)
    return hours, minutes


def calculate_fare(distance, age, train_type, travel_class, baggage_weight):
    train_type = normalize_train(train_type)
    travel_class = normalize_class(travel_class)
    if train_type is None:
        return None
    if travel_class is None:
        return None
    if distance <= 0 or age <= 0 or baggage_weight < 0:
        return None
    fare = slab_fare(distance)
    fare = senior_discount(fare, age)
    fare = train_premium(fare, train_type)
    fare = class_premium(fare, travel_class)
    fare += baggage_fee(baggage_weight, travel_class)
    fare += surcharge(train_type)
    return round(fare, 2)