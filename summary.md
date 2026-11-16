# 📑 Project Summary – Bus Ticket Booking System (`PS No. 40`)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![PS No.](https://img.shields.io/badge/PS_No.-40-indigo?style=for-the-badge)
![Tests](https://img.shields.io/badge/Tests_Passed-15%2F15-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Submission_Ready-brightgreen?style=for-the-badge)

</div>

| Field | Details |
| :--- | :--- |
| **👨‍💻 Student** | **Aditya Kumar Karsh** |
| **🆔 ERP No.** | `RU-26-00063` |
| **🏫 Section** | `BE-CSE-C-1-26-1-K` |
| **📚 Course** | Programming Fundamentals and Logic Building Using Python (`RU-100-01-0021`) |
| **📅 Submission Date** | **16 November 2026** |

---

## 1. 🌟 Overview

This project is a **console ticket booking system** for a bus with **10 numbered seats**. A passenger can view free seats, book a seat, inspect all active bookings, and cancel a booking with an automatic refund. 

* 💵 **Ticket Fare:** `Rs. 500` per seat
* 💸 **Cancellation Refund:** `80%` of the fare (`Rs. 400`)
* 📦 **Architecture:** Contained entirely within a single Python 3 file (`bus_ticket_booking.py`) using only built-in Python features—zero external libraries required.

---

## 2. 🎯 Problem Definition

| Component | Specification |
| :--- | :--- |
| **📥 Input** | A menu choice (`1–5`), a seat number (`1–10`), and a passenger name |
| **⚙️ Process** | Validate user input, update the `seats` list and `bookings` dictionary, and compute the fare or refund |
| **📤 Output** | Clear confirmation messages, calculated fare/refund, updated `Seats left` count, or descriptive error alerts |
| **🚧 Constraints** | `10` seats · `Rs. 500` per seat · `80%` refund · No double booking · All seats start free |

---

## 3. 🧠 Approach and Logic

1. **🗂️ Store the Data Efficiently**
   * A `list` named `seats` tracks the status of each seat (`"Available"` or `"Booked"`).
   * A `dictionary` named `bookings` maps `{seat_number: passenger_name}`.
   * *In short:* The list answers *"Is this seat free?"* and the dictionary answers *"Who booked it?"*
2. **🧩 Modularize into Focused Functions**
   * `view_seats`, `book_seat`, `view_bookings`, and `cancel_booking` drive the four core menu actions.
   * `parse_seat` and `clean_name` isolate input validation.
   * `main` orchestrates the interactive menu loop.
3. **🛡️ Validate Before Mutating State**
   * First, verify the seat number is a whole number from `1` to `10`.
   * Second, confirm the seat is currently available.
   * Third, validate and sanitize the passenger name. Nothing changes unless every check passes.
4. **📢 Provide Immediate Feedback**
   * Every booking or cancellation outputs the exact fare/refund and `Seats left: N`.
   * Booking the final seat triggers the alert: `Bus is now full.`
5. **🔁 Resilient Execution Loop**
   * The menu repeats seamlessly until the user selects **Exit**, gracefully catching invalid choices and `EOF`/`KeyboardInterrupt` signals.

---

## 4. 💡 Key Design Decisions

* **🔢 Exact Integer Arithmetic for Refunds:** Calculated via `500 * 80 // 100 = 400` so currency values remain exact integers without floating-point rounding quirks.
* **⚡ Fail-Fast Seat Validation:** If a seat is out of range or already booked, the program skips prompting for a name. This directly aligns with **Test Case 3**, where the seat number alone triggers the error.
* **🔄 Safe Return to Menu on Errors:** Invalid inputs display a clear message and return straight to the main menu without crashing or corrupting state.
* **📊 Consistent `Seats left` Reporting:** Because the specification requires showing remaining seats after *every* state change, `cancel_booking` prints `Seats left: N` right after the refund confirmation.
* **🔗 Unified Function Signatures:** All four menu handlers accept `(seats, bookings)`, allowing identical invocation from both the interactive CLI and the automated test runner.
* **🧪 Self-Contained Test Suite:** Running `python bus_ticket_booking.py --test` executes automated verification with zero manual typing while preserving the single-file constraint.

---

## 5. 🛡️ Input Validation Matrix

| Input Type | ✅ Accepted | ❌ Rejected & Error Message |
| :--- | :--- | :--- |
| **Seat Number** | Whole numbers `1` to `10` (e.g., `3`, `03`) | `abc`, `3.5`, `-2`, `0`, `11`, empty $\rightarrow$ `Invalid seat. Choose a seat from 1 to 10.` |
| **Passenger Name** | `2–30` characters: letters, spaces, `.`, `-`, `'` *(extra spaces collapsed)* | Empty, digits/symbols (e.g., `Aman123`), 1 letter, $>30$ chars $\rightarrow$ `Invalid name...` |
| **Menu Choice** | `1` to `5` | Any other input $\rightarrow$ `Invalid choice. Please enter a number from 1 to 5.` |
| **Booked Seat** | — | Attempting to rebook $\rightarrow$ `Seat N is already booked.` |
| **Free Seat Cancel** | — | Attempting to cancel unbooked seat $\rightarrow$ `Seat N is not booked. Nothing to cancel.` |

---

## 6. 🧪 Testing Summary

All **4 standard test cases** from the project specification and **11 additional edge cases** pass automatically.

| Test ID | Scenario | Status |
| :--- | :--- | :---: |
| **TC1** | **Normal:** Book seat `3` for Aman $\rightarrow$ `Fare: 500`, `Seats left: 9` | ✅ **PASS** |
| **TC2** | **Boundary:** Book final seat `10` $\rightarrow$ `Seats left: 0`, `Bus is now full.` | ✅ **PASS** |
| **TC3** | **Invalid:** Seat `3` already booked; seat `11` out of range | ✅ **PASS** |
| **TC4** | **Different Valid:** Cancel seat `3` $\rightarrow$ `Refund: 400`; view seats shows `Booked: 5 (Riya)` | ✅ **PASS** |
| **E1–E11** | Text/zero seat, invalid/empty names, whitespace cleanup, cancel unbooked/invalid seat, full bus booking, cancel-and-rebook flow, view bookings (empty & populated) | ✅ **PASS** |

> 🏆 **Final Score: `15 / 15` Automated Tests Passed.**  
> *Also verified manually in an end-to-end live console session covering view, book, duplicate booking, invalid seat, view bookings, cancel, wrong menu input, and exit.*

---

## 7. ✅ Requirement Compliance

| Bare Minimum Requirement | Implementation | Status |
| :--- | :--- | :---: |
| Single `.py` file run from the console | `bus_ticket_booking.py` | ✅ |
| Seats stored in a `list`, passengers in a `dict` | `seats` (`list`) & `bookings` (`dictionary`) | ✅ |
| Separate functions for view / book / bookings / cancel | `view_seats`, `book_seat`, `view_bookings`, `cancel_booking` | ✅ |
| Prevent double booking; calculate refund on cancel | Status check before booking; `80%` of `Rs. 500` = `400` | ✅ |
| Validate seat & name; display seats left on every change | `parse_seat`, `clean_name`, `show_seats_left` | ✅ |

---

## 8. 🛠️ Python Concepts Applied

`Lists` · `Dictionaries` · `Functions & Parameters` · `Loops (while, for)` · `Conditionals (if / elif / else)` · `String Methods (strip, split, isdigit, isalpha)` · `Exception Handling (try / except)` · `Constants` · `f-Strings` · `Input Validation` · `Modular Programming`

---

## 9. 🎓 Possible Viva Questions & Answers

<details>
<summary><strong>1. Why did you use a list for seats and a dictionary for passengers?</strong></summary>
<br>
A <code>list</code> is naturally ordered by seat index and works great for a fixed block of 10 seats, while a <code>dictionary</code> maps each booked seat number directly to a passenger name for $O(1)$ lookup, insertion, and deletion.
</details>

<details>
<summary><strong>2. How do you stop the same seat from being booked twice?</strong></summary>
<br>
<code>book_seat</code> checks <code>seats[seat - 1] == "Booked"</code> before accepting a passenger name and immediately outputs <code>Seat N is already booked.</code>
</details>

<details>
<summary><strong>3. How is the cancellation refund calculated?</strong></summary>
<br>
Using integer floor division: <code>FARE_PER_SEAT * REFUND_PERCENT // 100</code>, which evaluates to <code>500 * 80 // 100 = 400</code>.
</details>

<details>
<summary><strong>4. Why is seat 1 stored at index 0?</strong></summary>
<br>
Python lists are zero-indexed, so human-readable seat number $n$ maps cleanly to list index $n - 1$.
</details>

<details>
<summary><strong>5. What happens if the user types text instead of a seat number?</strong></summary>
<br>
<code>parse_seat</code> rejects the non-numeric input, returns <code>None</code>, and the program prints <code>Invalid seat. Choose a seat from 1 to 10.</code> without crashing.
</details>

<details>
<summary><strong>6. How did you test the program?</strong></summary>
<br>
Using the built-in <code>--test</code> runner, which simulates user input across all 4 required test cases and 11 additional edge cases.
</details>

---

## 10. 🚀 Limitations & Future Improvements

* **💾 Persistent Storage:** Bookings currently reside in memory and reset on exit; saving data to a JSON/CSV file or SQLite database would preserve records across sessions.
* **🚌 Multi-Bus & Route Support:** Extend the system to manage multiple buses, routes, schedules, and travel dates.
* **🗺️ Visual Seat Layout & Ticket IDs:** Render an ASCII seat map in the terminal and generate unique ticket numbers for every booking.
* **🔐 Verified Cancellations:** Require passenger name or ticket ID confirmation before processing a cancellation.

---

## 11. 📦 GitHub Submission Checklist

* [ ] `bus_ticket_booking.py`, `README.md`, and `SUMMARY.md` are placed in the same repository
* [ ] `python bus_ticket_booking.py --test` outputs `15/15` passed locally
* [ ] Source code and documentation pushed before **16 November 2026**

```bash
git init
git add bus_ticket_booking.py README.md SUMMARY.md
git commit -m "PS 40 - Bus Ticket Booking System"
git branch -M main
git remote add origin https://github.com/<your-username>/<repository-name>.git
git push -u origin main
```