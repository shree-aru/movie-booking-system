
import mysql.connector

def verify_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="", # No password for root in sandbox
            database="movie_booking_db"
        )
        cursor = conn.cursor()

        print("\n--- Verifying Database Structure ---")
        tables = ["Theatres", "Shows", "Seats", "Customers", "Bookings"]
        for table in tables:
            cursor.execute(f"DESCRIBE {table};")
            print(f"\nTable: {table}")
            for column in cursor:
                print(f"  {column[0]} ({column[1]}) {'NULL' if column[2]=='YES' else 'NOT NULL'}")

        print("\n--- Verifying Data ---")

        # Verify Theatres data
        cursor.execute("SELECT * FROM Theatres;")
        print("\nTheatres Data:")
        for row in cursor:
            print(row)

        # Verify Shows data
        cursor.execute("SELECT s.movie_title, t.name as theatre_name, s.show_time, s.ticket_price FROM Shows s JOIN Theatres t ON s.theatre_id = t.theatre_id;")
        print("\nShows Data:")
        for row in cursor:
            print(row)

        # Verify Customers data
        cursor.execute("SELECT * FROM Customers;")
        print("\nCustomers Data:")
        for row in cursor:
            print(row)

        # Verify Bookings data
        cursor.execute("SELECT b.booking_id, c.first_name, c.last_name, s.movie_title, se.seat_number, b.booking_time FROM Bookings b JOIN Customers c ON b.customer_id = c.customer_id JOIN Shows s ON b.show_id = s.show_id JOIN Seats se ON b.seat_id = se.seat_id;")
        print("\nBookings Data:")
        for row in cursor:
            print(row)

        # Verify Seat availability
        cursor.execute("SELECT theatre_id, seat_number, is_available FROM Seats WHERE is_available = FALSE;")
        print("\nBooked Seats:")
        for row in cursor:
            print(f"  Theatre ID: {row[0]}, Seat: {row[1]}, Available: {row[2]}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("\nMySQL connection closed.")

if __name__ == "__main__":
    verify_database()


