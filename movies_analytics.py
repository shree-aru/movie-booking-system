import mysql.connector

def generate_analytics():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="movie_booking_db"
        )
        cursor = conn.cursor(dictionary=True)

        print("\n=== Movie Booking Analytics ===")

        # 1. Revenue per show
        print("\n1. Revenue Per Show:")
        cursor.execute("""
            SELECT s.movie_title, t.name as theatre_name, SUM(s.ticket_price) as total_revenue
            FROM Bookings b
            JOIN Shows s ON b.show_id = s.show_id
            JOIN Theatres t ON s.theatre_id = t.theatre_id
            GROUP BY s.show_id
            ORDER BY total_revenue DESC;
        """)
        for row in cursor:
            print(f"Movie: {row['movie_title']} | Theatre: {row['theatre_name']} | Revenue: ${row['total_revenue']}")

        # 2. Most active customers
        print("\n2. Top Customers (By Tickets Booked):")
        cursor.execute("""
            SELECT c.first_name, c.last_name, COUNT(b.booking_id) as total_tickets
            FROM Bookings b
            JOIN Customers c ON b.customer_id = c.customer_id
            GROUP BY c.customer_id
            ORDER BY total_tickets DESC
            LIMIT 5;
        """)
        for row in cursor:
            print(f"Customer: {row['first_name']} {row['last_name']} | Tickets: {row['total_tickets']}")

    except mysql.connector.Error as err:
        print(f"Error executing analytics: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    generate_analytics()
