"""
Bus Ticket Booking System
=========================
A console ticket booking system for a bus with 10 numbered seats (1 to 10).
Passengers can view seats, book a seat, view bookings and cancel a booking.

Rules
-----
* Fare is Rs.500 per seat.
* Cancelling a booking refunds 80% of the fare (Rs.400).
* A seat that is already booked cannot be booked again.
* The seat number and the passenger name are validated.
* The number of seats left is shown after every change (booking / cancellation).

Data structures
---------------
* seats    : list  -> seats[0] is seat 1 ... seats[9] is seat 10.
                      Each item is either "Available" or "Booked".
* bookings : dict  -> {seat_number: passenger_name}

Usage
-----
    python bus_ticket_booking.py           # run the program
    python bus_ticket_booking.py --test    # run the built-in test cases
"""

import io
import sys
from contextlib import redirect_stdout

# ----------------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------------
TOTAL_SEATS = 10
FARE_PER_SEAT = 500
REFUND_PERCENT = 80
MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 30

AVAILABLE = "Available"
BOOKED = "Booked"

INVALID_SEAT_MESSAGE = f"Invalid seat. Choose a seat from 1 to {TOTAL_SEATS}."
INVALID_NAME_MESSAGE = (
    f"Invalid name. Use {MIN_NAME_LENGTH} to {MAX_NAME_LENGTH} letters "
    "(spaces, . - ' allowed)."
)


# ----------------------------------------------------------------------------
# Helper functions
# ----------------------------------------------------------------------------
def create_bus():
    """Return a new bus: every seat is free and there are no bookings."""
    seats = [AVAILABLE] * TOTAL_SEATS
    bookings = {}
    return seats, bookings


def seats_left(seats):
    """Return how many seats are still available."""
    return seats.count(AVAILABLE)


def parse_seat(text):
    """
    Convert the text typed by the user into a seat number.
    Returns the seat number (1 to TOTAL_SEATS) or None if the input is invalid.
    """
    text = text.strip()
    # Only plain digits are accepted: rejects "abc", "3.5", "-2", "", "1_0".
    if not (text.isascii() and text.isdigit()):
        return None
    number = int(text)
    if 1 <= number <= TOTAL_SEATS:
        return number
    return None


def clean_name(text):
    """
    Validate a passenger name.
    Returns the cleaned name (extra spaces removed) or None if it is invalid.
    A valid name starts with a letter and contains only letters, spaces and
    the characters . - ' with a length of 2 to 30 characters.
    """
    name = " ".join(text.split())
    if not (MIN_NAME_LENGTH <= len(name) <= MAX_NAME_LENGTH):
        return None
    if not name[0].isalpha():
        return None
    for character in name:
        if not (character.isalpha() or character in " .-'"):
            return None
    return name


def show_seats_left(seats):
    """Print the number of seats that are still available."""
    print(f"Seats left: {seats_left(seats)}")


# ----------------------------------------------------------------------------
# Menu operations (all take the same two arguments so they can be called alike)
# ----------------------------------------------------------------------------
def view_seats(seats, bookings):
    """Menu option 1: show booked seats (with passenger) and free seats."""
    booked = [f"{seat} ({bookings[seat]})" for seat in sorted(bookings)]
    available = [
        str(number)
        for number, status in enumerate(seats, start=1)
        if status == AVAILABLE
    ]
    print("Booked: " + (", ".join(booked) if booked else "None"))
    print("Available: " + (", ".join(available) if available else "None"))


def book_seat(seats, bookings):
    """Menu option 2: book a free seat for a passenger."""
    if seats_left(seats) == 0:
        print("Bus is full. No seats available.")
        return

    seat = parse_seat(input(f"Enter seat number (1-{TOTAL_SEATS}): "))
    if seat is None:
        print(INVALID_SEAT_MESSAGE)
        return

    if seats[seat - 1] == BOOKED:
        print(f"Seat {seat} is already booked.")
        return

    name = clean_name(input("Enter passenger name: "))
    if name is None:
        print(INVALID_NAME_MESSAGE)
        return

    seats[seat - 1] = BOOKED
    bookings[seat] = name
    print(f"Seat {seat} booked for {name}. Fare: {FARE_PER_SEAT}")
    show_seats_left(seats)
    if seats_left(seats) == 0:
        print("Bus is now full.")


def view_bookings(seats, bookings):
    """Menu option 3: list every booking with the total fare collected."""
    if not bookings:
        print("No bookings yet.")
        return

    print("Current bookings:")
    for seat in sorted(bookings):
        print(f"Seat {seat} | {bookings[seat]} | Fare: {FARE_PER_SEAT}")
    total_fare = len(bookings) * FARE_PER_SEAT
    print(f"Total bookings: {len(bookings)} | Total fare collected: {total_fare}")
    show_seats_left(seats)


def cancel_booking(seats, bookings):
    """Menu option 4: cancel a booking and refund 80% of the fare."""
    if not bookings:
        print("No bookings to cancel.")
        return

    seat = parse_seat(input(f"Enter seat number to cancel (1-{TOTAL_SEATS}): "))
    if seat is None:
        print(INVALID_SEAT_MESSAGE)
        return

    if seat not in bookings:
        print(f"Seat {seat} is not booked. Nothing to cancel.")
        return

    del bookings[seat]
    seats[seat - 1] = AVAILABLE
    refund = FARE_PER_SEAT * REFUND_PERCENT // 100
    print(f"Booking for seat {seat} cancelled. Refund: {refund}")
    show_seats_left(seats)


# ----------------------------------------------------------------------------
# Main program
# ----------------------------------------------------------------------------
MENU_ACTIONS = {
    "1": view_seats,
    "2": book_seat,
    "3": view_bookings,
    "4": cancel_booking,
}


def print_menu():
    """Display the main menu."""
    print("1. View seats")
    print("2. Book a seat")
    print("3. View bookings")
    print("4. Cancel a booking")
    print("5. Exit")


def main():
    """Run the menu-driven program until the user chooses Exit."""
    seats, bookings = create_bus()

    print("=" * 50)
    print("          BUS TICKET BOOKING SYSTEM")
    print("=" * 50)
    print(
        f"Seats: {TOTAL_SEATS} | Fare: Rs.{FARE_PER_SEAT} per seat | "
        f"Refund on cancellation: {REFUND_PERCENT}%"
    )

    try:
        while True:
            print()
            print_menu()
            choice = input("Enter your choice (1-5): ").strip()

            if choice == "5":
                print("Thank you for using the Bus Ticket Booking System. Goodbye!")
                break

            action = MENU_ACTIONS.get(choice)
            if action is None:
                print("Invalid choice. Please enter a number from 1 to 5.")
                continue

            print()
            action(seats, bookings)
    except (EOFError, KeyboardInterrupt):
        print("\nProgram ended. Goodbye!")


# ----------------------------------------------------------------------------
# Built-in test cases  (python bus_ticket_booking.py --test)
# ----------------------------------------------------------------------------
def run_tests():
    """
    Run the 4 test cases given in the project description (PS 40) plus some
    extra edge cases. User input is simulated, so no typing is needed.
    Returns True if every test passes.
    """
    from unittest.mock import patch

    actions = {
        "view": view_seats,
        "book": book_seat,
        "bookings": view_bookings,
        "cancel": cancel_booking,
    }

    def make_bus(preset):
        """Create a bus where the seats in `preset` ({seat: name}) are booked."""
        seats, bookings = create_bus()
        for seat, name in preset.items():
            seats[seat - 1] = BOOKED
            bookings[seat] = name
        return seats, bookings

    def run_step(state, action, user_inputs):
        """Run one menu action with simulated input; return its output lines."""
        seats, bookings = state
        buffer = io.StringIO()
        try:
            with patch("builtins.input", side_effect=user_inputs), redirect_stdout(buffer):
                actions[action](seats, bookings)
        except Exception as error:  # a crash is a failed test, not a stop
            return [f"ERROR: {error!r}"]
        return buffer.getvalue().strip().splitlines()

    all_free = list(range(1, TOTAL_SEATS + 1))
    nine_booked = {seat: "Guest" for seat in range(1, 10)}
    full_bus = {seat: "Guest" for seat in range(1, 11)}

    # (id, title, seats booked at the start, [(action, inputs, expected output)])
    test_cases = [
        # ---- Test cases from the project description -----------------------
        ("TC1", "Normal Input - book seat 3 for Aman", {}, [
            ("book", ["3", "Aman"],
             ["Seat 3 booked for Aman. Fare: 500", "Seats left: 9"]),
        ]),
        ("TC2", "Boundary Input - book last seat 10 for Riya", nine_booked, [
            ("book", ["10", "Riya"],
             ["Seat 10 booked for Riya. Fare: 500", "Seats left: 0",
              "Bus is now full."]),
        ]),
        ("TC3", "Invalid Input - booked seat 3 / seat 11", {3: "Aman"}, [
            ("book", ["3"], ["Seat 3 is already booked."]),
            ("book", ["11"], ["Invalid seat. Choose a seat from 1 to 10."]),
        ]),
        ("TC4", "Different Valid Scenario - cancel seat 3, view seats",
         {3: "Aman", 5: "Riya"}, [
            ("cancel", ["3"],
             ["Booking for seat 3 cancelled. Refund: 400", "Seats left: 9"]),
            ("view", [],
             ["Booked: 5 (Riya)",
              "Available: " + ", ".join(str(s) for s in all_free if s != 5)]),
        ]),
        # ---- Extra edge cases ------------------------------------------------
        ("E1", "Seat number is text ('abc')", {}, [
            ("book", ["abc"], ["Invalid seat. Choose a seat from 1 to 10."]),
        ]),
        ("E2", "Seat number 0 is out of range", {}, [
            ("book", ["0"], ["Invalid seat. Choose a seat from 1 to 10."]),
        ]),
        ("E3", "Invalid name (digits) - seat stays free", {}, [
            ("book", ["4", "Aman123"],
             ["Invalid name. Use 2 to 30 letters (spaces, . - ' allowed)."]),
            ("view", [],
             ["Booked: None", "Available: " + ", ".join(str(s) for s in all_free)]),
        ]),
        ("E4", "Empty passenger name", {}, [
            ("book", ["4", "   "],
             ["Invalid name. Use 2 to 30 letters (spaces, . - ' allowed)."]),
        ]),
        ("E5", "Extra spaces in name are cleaned", {}, [
            ("book", ["7", "  Aditya   Kumar "],
             ["Seat 7 booked for Aditya Kumar. Fare: 500", "Seats left: 9"]),
        ]),
        ("E6", "Cancel a seat that is not booked", {3: "Aman"}, [
            ("cancel", ["7"], ["Seat 7 is not booked. Nothing to cancel."]),
        ]),
        ("E7", "Cancel with an invalid seat number", {3: "Aman"}, [
            ("cancel", ["11"], ["Invalid seat. Choose a seat from 1 to 10."]),
        ]),
        ("E8", "Booking when the bus is full", full_bus, [
            ("book", [], ["Bus is full. No seats available."]),
        ]),
        ("E9", "Cancel and re-book the same seat", {3: "Aman"}, [
            ("cancel", ["3"],
             ["Booking for seat 3 cancelled. Refund: 400", "Seats left: 10"]),
            ("book", ["3", "Riya"],
             ["Seat 3 booked for Riya. Fare: 500", "Seats left: 9"]),
        ]),
        ("E10", "View bookings (two bookings)", {3: "Aman", 5: "Riya"}, [
            ("bookings", [],
             ["Current bookings:",
              "Seat 3 | Aman | Fare: 500",
              "Seat 5 | Riya | Fare: 500",
              "Total bookings: 2 | Total fare collected: 1000",
              "Seats left: 8"]),
        ]),
        ("E11", "View bookings on an empty bus", {}, [
            ("bookings", [], ["No bookings yet."]),
        ]),
    ]

    print("Running test cases for PS 40 - Bus Ticket Booking System")
    print("-" * 60)

    passed = 0
    for case_id, title, preset, steps in test_cases:
        state = make_bus(preset)
        failures = []
        for action, user_inputs, expected in steps:
            actual = run_step(state, action, user_inputs)
            if actual != expected:
                failures.append((action, user_inputs, expected, actual))

        if failures:
            print(f"[FAIL] {case_id:<4} {title}")
            for action, user_inputs, expected, actual in failures:
                print(f"       action : {action}  inputs: {user_inputs}")
                print(f"       expected: {expected}")
                print(f"       actual  : {actual}")
        else:
            passed += 1
            print(f"[PASS] {case_id:<4} {title}")

    print("-" * 60)
    print(f"Result: {passed}/{len(test_cases)} test cases passed")
    return passed == len(test_cases)


if __name__ == "__main__":
    if "--test" in sys.argv[1:]:
        sys.exit(0 if run_tests() else 1)
    main()
