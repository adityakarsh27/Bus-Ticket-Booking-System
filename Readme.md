<div align="center">

# 🚌 Bus Ticket Booking System

**A sleek, console-based ticket booking system for a bus with numbered seats, built in Python 3.**  
*Seamlessly view seats, book tickets, manage bookings, and process instant refunds.*


</div>

---

## 📋 Project & Student Metadata

| Attribute | Details |
| :--- | :--- |
| **📌 Project (PS No.)** | `40` – Bus/Train Ticket Booking System |
| **👨‍💻 Student** | **Aditya Kumar Karsh** |
| **🆔 ERP No.** | `RU-26-00063` |
| **🏫 Section** | `BE-CSE-C-1-26-1-K` |
| **📚 Course** | Programming Fundamentals and Logic Building Using Python |
| **🏛️ University** | Rungta International Skills University – School of Computer Science and Engineering |
| **⚙️ Language** | Python 3 *(single file, zero external libraries)* |

---

## 🎯 Problem Statement

Develop a console ticket booking system for a bus with numbered seats where passengers can **view seats**, **book a seat**, **view bookings**, and **cancel a booking with a refund**.

### 📜 Core System Rules
* 💺 **Capacity:** The bus has **10 seats** numbered `1` to `10`.
* 💵 **Ticket Fare:** Fixed at **Rs. 500** per seat.
* 💸 **Cancellation Refund:** Automatically refunds **80%** of the fare (**Rs. 400**).
* 🧭 **Menu Controls:** `1` View seats, `2` Book, `3` Bookings, `4` Cancel.
* 🔄 **Initial State:** Every test case starts with all seats free unless stated otherwise.

---

## ✨ Key Features

- **🔁 Continuous Menu-Driven Loop:** Runs smoothly until the user explicitly chooses **Exit**.
- **🗂️ Clean Data Structures:** Seats are tracked in a `list`; passenger details are mapped in a `dictionary`.
- **🚫 Double-Booking Prevention:** A seat that is already booked **cannot be booked again**.
- **🔢 Strict Seat Validation:** Ensures seat inputs are whole numbers strictly between `1` and `10`.
- **✍️ Smart Name Validation:** Accepts letters only (`2–30` characters) and automatically cleans extra whitespace.
- **🧮 Instant Refund Engine:** Automatically calculates the 80% cancellation refund (`Rs. 400`).
- **📊 Real-Time Seat Counter:** Displays **Seats left** immediately after every booking and cancellation.
- **🔔 Full-Capacity Alerts:** Notifies the user with `"Bus is now full."` as soon as the final seat is claimed.
- **🛡️ Crash-Proof Execution:** Gracefully handles invalid menu inputs as well as `Ctrl+C` / `Ctrl+D` interrupts.
- **🧪 Built-in Automated Test Suite:** Run with `--test` to verify all 4 core test cases plus 11 edge cases.

---

## 🚀 How to Run

> **Prerequisite:** Python **3.7** or newer. No third-party packages need to be installed.

```bash
# 1. Run the interactive booking system
python bus_ticket_booking.py

# 2. Run the automated test runner (no manual input required)
python bus_ticket_booking.py --test
```

> 💡 **Tip:** Depending on your operating system configuration, you may need to use `python3` instead of `python`.

---

## 🧭 Menu Overview

```text
1. View seats
2. Book a seat
3. View bookings
4. Cancel a booking
5. Exit
```

| Option | Action | Description |
| :---: | :--- | :--- |
| **`1`** | **View seats** | Displays booked seats alongside passenger names and lists all available seats. |
| **`2`** | **Book a seat** | Prompts for a seat number and passenger name, then confirms booking (`Fare: 500`). |
| **`3`** | **View bookings** | Lists every active booking, total fare collected, and remaining seats. |
| **`4`** | **Cancel a booking** | Prompts for a seat number, frees the seat, and issues the refund (`Refund: 400`). |
| **`5`** | **Exit** | Safely terminates the program. |

---

## 💻 Sample Console Run

```text
==================================================
          BUS TICKET BOOKING SYSTEM
==================================================
Seats: 10 | Fare: Rs.500 per seat | Refund on cancellation: 80%

1. View seats
2. Book a seat
3. View bookings
4. Cancel a booking
5. Exit
Enter your choice (1-5): 2

Enter seat number (1-10): 3
Enter passenger name: Aman
Seat 3 booked for Aman. Fare: 500
Seats left: 9

Enter your choice (1-5): 2

Enter seat number (1-10): 5
Enter passenger name: Riya
Seat 5 booked for Riya. Fare: 500
Seats left: 8

Enter your choice (1-5): 2

Enter seat number (1-10): 3
Seat 3 is already booked.

Enter your choice (1-5): 4

Enter seat number to cancel (1-10): 3
Booking for seat 3 cancelled. Refund: 400
Seats left: 9

Enter your choice (1-5): 1

Booked: 5 (Riya)
Available: 1, 2, 3, 4, 6, 7, 8, 9, 10
```

> *Note: In live execution, the menu reprints before each `"Enter your choice"` prompt; it is omitted above for brevity.*

---

## 🧪 Verification & Test Cases

All four standard test cases from the project specification pass automatically via `python bus_ticket_booking.py --test`:

| Test Case | Scenario / Input | Expected Output | Status |
| :--- | :--- | :--- | :---: |
| **TC1 – Normal** | Book seat `3` for `Aman` | `Seat 3 booked for Aman. Fare: 500`<br>`Seats left: 9` | ✅ **PASS** |
| **TC2 – Boundary** | Seats `1–9` booked; book seat `10` for `Riya` | `Seat 10 booked for Riya. Fare: 500`<br>`Seats left: 0`<br>`Bus is now full.` | ✅ **PASS** |
| **TC3 – Invalid** | **(a)** Book seat `3` (already booked)<br>**(b)** Book seat `11` | **(a)** `Seat 3 is already booked.`<br>**(b)** `Invalid seat. Choose a seat from 1 to 10.` | ✅ **PASS** |
| **TC4 – Different Valid** | Seat `3` (`Aman`) & seat `5` (`Riya`) booked;<br>**(a)** cancel seat `3`, **(b)** view seats | **(a)** `Booking for seat 3 cancelled. Refund: 400`<br>**(b)** `Booked: 5 (Riya)` / `Available: 1, 2, 3, 4, 6, 7, 8, 9, 10` | ✅ **PASS** |

### 🔍 Extended Edge Cases (`E1–E11`)
All **11 additional edge cases** also pass without error:
* Non-numeric text or `0` entered as a seat number
* Invalid characters or empty strings for passenger names
* Extra leading, trailing, or internal spaces in passenger names
* Attempting to cancel an unbooked seat or an out-of-range seat number
* Attempting to book when the bus is completely full
* Cancelling and immediately rebooking the same seat
* Viewing bookings on an empty bus vs. a bus with two active bookings

> 🏆 **Final Test Result: `15 / 15` test cases passed.**

---

## 🧠 How the Program Works

### 🗄️ Data Structures

```python
seats    = ["Available", "Available", ..., "Available"]   # list: seats[0] is seat 1 ... seats[9] is seat 10
bookings = {3: "Aman", 5: "Riya"}                         # dictionary: {seat_number: passenger_name}
```

### ⚙️ Function Architecture

| Function | Responsibility |
| :--- | :--- |
| `create_bus()` | Initializes a fresh bus with all 10 seats free and an empty booking dictionary |
| `seats_left(seats)` | Calculates and returns the count of remaining available seats |
| `parse_seat(text)` | Validates seat input; returns an integer `1–10` or `None` |
| `clean_name(text)` | Sanitizes and validates passenger names; returns cleaned string or `None` |
| `show_seats_left(seats)` | Outputs `Seats left: N` to the console |
| `view_seats(seats, bookings)` | Handles **Menu Option 1** (displays booked and available seats) |
| `book_seat(seats, bookings)` | Handles **Menu Option 2** (validates input and processes new bookings) |
| `view_bookings(seats, bookings)` | Handles **Menu Option 3** (displays booking manifest and total revenue) |
| `cancel_booking(seats, bookings)` | Handles **Menu Option 4** (frees seat and calculates 80% refund) |
| `print_menu()` / `main()` | Renders the main menu and drives the interactive program loop |
| `run_tests()` | Executes the built-in automated test suite (`--test`) |

### 🔄 Core Workflows

<details open>
<summary><b>🎟️ Booking Workflow</b></summary>

1. Check seat availability → if `0` seats are free, print `Bus is full. No seats available.`
2. Read and validate seat number → if not a whole number from `1` to `10`, print `Invalid seat...`
3. Check seat status → if already occupied, print `Seat N is already booked.`
4. Read and validate passenger name → if invalid, print `Invalid name...`
5. Mark seat as booked, record passenger name in `bookings`, and display fare (`500`) + remaining seats.
6. If remaining seats reach `0`, announce `Bus is now full.`
</details>

<details open>
<summary><b>❌ Cancellation Workflow</b></summary>

1. Read and validate the target seat number.
2. Verify booking status → if seat is not booked, print `Seat N is not booked. Nothing to cancel.`
3. Remove entry from `bookings`, mark seat as `"Available"`, calculate refund (`500 × 80 / 100 = 400`), and display updated seat count.
</details>

---

## ✅ Project Requirements Checklist

| # | Bare Minimum Requirement | Status | Implementation |
| :---: | :--- | :---: | :--- |
| **1** | Solution in Python 3 (one `.py` file), run from the console | ✅ | `bus_ticket_booking.py` |
| **2** | Seats stored in a list, passenger details in a dictionary | ✅ | `seats` list & `bookings` dictionary |
| **3** | Functions to view seats, book a seat, view bookings, and cancel a booking | ✅ | Four dedicated modular functions |
| **4** | No double booking; refund calculated on cancellation | ✅ | Occupied-seat guard & `80%` refund logic |
| **5** | Validate seat number and passenger name; show seats left after every change | ✅ | `parse_seat()`, `clean_name()`, `Seats left: N` |

---

## 📂 Repository Structure

```text
📦 Bus-Ticket-Booking-System
 ┣ 📜 bus_ticket_booking.py   # Complete source code (interactive CLI + built-in test suite)
 ┣ 📝 README.md               # Project documentation (this file)
 ┗ 📄 SUMMARY.md              # Concise project summary
```

---

<div align="center">

### 👨‍💻 Developed By

**Aditya Kumar Karsh**  
ERP: `RU-26-00063` • Section: `BE-CSE-C-1-26-1-K`  
*Rungta International Skills University – School of Computer Science and Engineering*

</div>