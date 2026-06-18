import mysql.connector

def book_ticket(customer_id, show_id, seat_number):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="movie_booking_db"
        )
        cursor = conn.cursor()

        # Step 1: Find the theatre_id for the show
        cursor.execute("SELECT theatre_id FROM Shows WHERE show_id = %s", (show_id,))
        show = cursor.fetchone()
        if not show:
            print("Error: Show not found.")
            return
        theatre_id = show[0]

        # Step 2: Check if seat exists and is available
        cursor.execute(
            "SELECT seat_id, is_available FROM Seats WHERE theatre_id = %s AND seat_number = %s", 
            (theatre_id, seat_number)
        )
        seat = cursor.fetchone()
        if not seat:
            print("Error: Seat not found in this theatre.")
            return
        if not seat[1]:
            print(f"Error: Seat {seat_number} is already booked!")
            return
        seat_id = seat[0]

        # Step 3: Insert booking
        cursor.execute(
            "INSERT INTO Bookings (customer_id, show_id, seat_id) VALUES (%s, %s, %s)",
            (customer_id, show_id, seat_id)
        )

        # Step 4: Mark seat as unavailable
        cursor.execute(
            "UPDATE Seats SET is_available = FALSE WHERE seat_id = %s",
            (seat_id,)
        )

        # Commit transaction
        conn.commit()
        print(f"Success! Ticket booked for Customer {customer_id}, Show {show_id}, Seat {seat_number}.")

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        if 'conn' in locals() and conn.is_connected():
            conn.rollback()
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    print("--- Interactive Ticket Booking System ---")
    try:
        c_id = int(input("Enter Customer ID: "))
        s_id = int(input("Enter Show ID: "))
        seat_no = input("Enter Seat Number (e.g., A1): ")
        book_ticket(c_id, s_id, seat_no)
    except ValueError:
        print("Invalid input. IDs must be integers.")
