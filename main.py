#main.py cordinates the entire system 

from routes import get_distance
from fare import calculate_fare, apply_promo, calculate_time


def get_valid_int(user_input):
    while True:
        try:
            value = int(input(user_input))
            if value <= 0:
                print("Enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Enter a number.")


def get_valid_float(user_input):
    while True:
        try:
            value = float(input(user_input))
            if value < 0:
                print("Value cannot be negative.")
            else:
                return value
        except ValueError:
            print("Invalid input. Enter a number.")


def get_non_empty(user_input):
    while True:
        value = input(user_input).strip()
        if value == "":
            print("Input cannot be empty.")
        else:
            return value


def main():
    while True:
        print("###########################################")
        print("-🚥 TRAIN TICKET BOOKING SYSTEM 𓂃 ࣪˖ ִֶָ 𓈈")
        print("\tPresented by 25BDS0098 ｡°🚂༄｡° ")
        print("###########################################")

        print("1. 🌳 Book Ticket")
        print("2. 🚩 Exit")
        wish =input(" enter your choice 🚂 : ")
        if wish == "1":

            source = get_non_empty("🟢 enter source : ")
            destination = get_non_empty("🚩 enter destination :")
            distance = get_distance(source, destination)

            if distance is None:
                print("Route not available.")
                continue
            print("🚦   distance :", distance, "km")
            print("------------------------------------------")
            passengers = get_valid_int("Enter number of passengers 🚸 :") 
            total = 0

            for i in range(passengers):
                print(f"\n🌟 passenger {i+1}")

                age = get_valid_int("\n🤵 enter age : ")
                print("\n📍available types are :")
                print("--------------------------------------------")
                print("1. FAST PASSENGER")
                print("2. EXPRESS")
                print("3. SUPERFAST")
                print("--------------------------------------------")
                train_type = get_non_empty("🚆 enter train type: ")
                print("\n📍available classes are :")
                print("--------------------------------------------")
                print("1. SLEEPER")
                print("2. AC 3-TIER")
                print("3. AC 2-TIER")
                print("--------------------------------------------")
                travel_class = get_non_empty("📢 enter travel class: ")
                
                baggage = get_valid_float("\n🧳 enter baggage weight (kg): ")

                fare = calculate_fare(distance, age, train_type, travel_class, baggage)

                if fare is None:
                    print("Invalid train type or class.🚨")
                    continue
                print("------------------------------------------")
                print("\n🎟️ passenger fare:", fare)
                total += fare
                print("------------------------------------------")
            print("\n🎟️ total fare :", round(total, 2))
            print("------------------------------------------")
            print("𓂃 ࣪˖ ִֶָ 𓈈 if there's any promo code enter down below or just click ENTER key to proceed.")
            promo = input("enter promo code 💼 : ")
            total = apply_promo(total, promo)
            
            print("\n========== TICKET .𖥔 ݁ ˖🚋⋆｡°•☁︎⋆˚࿔ ==========")
            print("𖠵 Route:", source.title(), "→", destination.title())
            print("𖠵 Distance:", distance, "km")

            train_type_clean = train_type.strip().title()
            hours, minutes = calculate_time(distance, train_type.upper())

            print("🚆   Train Type:", train_type_clean)
            print("🕰️   Travel Time:", hours, "hrs", minutes, "min")

            print("\n⚜️   Passengers:", passengers)
            print("🎟️   Subtotal:", round(total, 2))
            print("🛎️   Final Amount:", total)
            print("================================================")

        elif wish == "2":
            print("Thank you for using the Train Ticket Booking System. Goodbye! 🚂💨")
            break

        else:
            print("Invalid choice. Please enter 1 or 2. 🚨")

if __name__ == "__main__":
    main()