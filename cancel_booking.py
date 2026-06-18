import mysql.connector

def cancel_booking(booking_id):
    """Cancel a booking and free up the seat."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="movie_booking_db"
        )
        cursor = conn.cursor(dictionary=True)

        # Step 1: Find the booking
        cursor.execute("""
            SELECT b.booking_id, b.seat_id, c.first_name, c.last_name, s.movie_title, se.seat_number
            FROM Bookings b
            JOIN Customers c ON b.customer_id = c.customer_id
            JOIN Shows s ON b.show_id = s.show_id
            JOIN Seats se ON b.seat_id = se.seat_id
            WHERE b.booking_id = %s
        """, (booking_id,))
        
        booking = cursor.fetchone()
        
        if not booking:
            print(f"Error: Booking #{booking_id} not found.")
            return False

        # Step 2: Display booking details
        print(f"\n--- Booking Details ---")
        print(f"Booking ID  : #{booking['booking_id']}")
        print(f"Customer    : {booking['first_name']} {booking['last_name']}")
        print(f"Movie       : {booking['movie_title']}")
        print(f"Seat        : {booking['seat_number']}")

        # Step 3: Confirm cancellation
        confirm = input("\nAre you sure you want to cancel this booking? (yes/no): ")
        if confirm.lower() != 'yes':
            print("Cancellation aborted.")
            return False

        # Step 4: Free up the seat
        cursor.execute(
            "UPDATE Seats SET is_available = TRUE WHERE seat_id = %s",
            (booking['seat_id'],)
        )

        # Step 5: Delete the booking record
        cursor.execute(
            "DELETE FROM Bookings WHERE booking_id = %s",
            (booking_id,)
        )

        conn.commit()
        print(f"\nBooking #{booking_id} has been successfully cancelled.")
        print(f"Seat {booking['seat_number']} is now available again.")
        return True

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        if 'conn' in locals() and conn.is_connected():
            conn.rollback()
        return False
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    print("--- Booking Cancellation System ---")
    try:
        b_id = int(input("Enter Booking ID to cancel: "))
        cancel_booking(b_id)
    except ValueError:
        print("Invalid input. Booking ID must be an integer.")
