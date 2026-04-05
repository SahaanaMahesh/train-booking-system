# 🚂 Train Ticket Booking System
**This project is a modular command-line based Train Ticket Booking System developed using Python.**
* NOTE : this isn't a real-world problem based task. It's a task worked on for TeamADG's selections !
---

## ✨ Features Involved - extra functionality added besides the task (travel time estimation)
* 📍 Route-based distance calculation
* 🎟️ Fare calculation using slab system
* 👴 Senior citizen discount
* 🚆 Multiple train types (Fast Passenger, Express, Superfast)
* 💺 Travel classes (Sleeper, AC 3-Tier, AC 2-Tier)
* 🧳 Baggage fee handling
* 🎁 Promo code support
* 🛡️ Error handling for invalid inputs
* 🧮 Travel time estimation

---

## 🗂️ Project Structure

```
main.py        → Coordinates the flow of the program and user interaction
fare.py        → Mathematical fare calculation logic
routes.py      → Distance data and Route between two cities data (implemented using dictionaries)
trains.py      → Train type details (dictionaries used)
classes.py     → Travel class details (dictionaries used)
```

---

## ⚙️ Working of the program
1. User enters source and destination
2. System calculates distance
3. User enters passenger details
4. Fare is calculated based on:
   * Distance slab
   * Age (senior discount available after a limit)
   * Train type
   * Travel class
   * Baggage weight
5. Promo code (optional) is applied
6. Final ticket is displayed

---

## 🧠 Concepts Used

* Functions and modular programming
* Dictionaries and data structures
* Error handling using try-except
* Loops and conditional statements
* String normalization

---

## 👩‍💻 Author
* **Reg No:** 25BDS0098
* **Name:** Sahaana Mahesh
---

