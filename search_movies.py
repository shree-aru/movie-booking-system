import mysql.connector

def search_movies(search_term):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="movie_booking_db"
        )
        cursor = conn.cursor(dictionary=True)

        print(f"\n--- Searching for: '{search_term}' ---")

        # Search by Movie Title or Theatre Name
        query = """
            SELECT s.show_id, s.movie_title, t.name as theatre_name, s.show_time, s.ticket_price
            FROM Shows s
            JOIN Theatres t ON s.theatre_id = t.theatre_id
            WHERE s.movie_title LIKE %s OR t.name LIKE %s
            ORDER BY s.show_time ASC;
        """
        search_pattern = f"%{search_term}%"
        cursor.execute(query, (search_pattern, search_pattern))
        
        results = cursor.fetchall()
        
        if not results:
            print("No movies or theatres found matching your search.")
        else:
            print(f"Found {len(results)} match(es):")
            for row in results:
                print(f"[{row['show_id']}] {row['movie_title']} @ {row['theatre_name']} | Time: {row['show_time']} | Price: ${row['ticket_price']}")

    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    print("Welcome to the Movie Search Tool!")
    while True:
        term = input("\Enter a movie title or theatre name to search (or 'quit' to exit): ")
        if term.lower() in ['quit', 'q', 'exit']:
            break
        if term.strip():
            search_movies(term.strip())
