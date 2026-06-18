from datetime import datetime

def generate_receipt(booking_id, customer_name, movie_title, theatre_name, seat_number, show_time, ticket_price):
    """Generate a formatted booking receipt."""
    receipt_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    border = "=" * 50
    thin_border = "-" * 50
    
    receipt = f"""
{border}
          🎬  MOVIE BOOKING RECEIPT  🎬
{border}

  Booking ID    : #{booking_id}
  Date Issued   : {receipt_time}

{thin_border}
  BOOKING DETAILS
{thin_border}

  Movie         : {movie_title}
  Theatre       : {theatre_name}
  Show Time     : {show_time}
  Seat Number   : {seat_number}

{thin_border}
  CUSTOMER DETAILS
{thin_border}

  Name          : {customer_name}

{thin_border}
  PAYMENT SUMMARY
{thin_border}

  Ticket Price  : ${ticket_price:.2f}
  Service Fee   : ${ticket_price * 0.05:.2f}
  Total Amount  : ${ticket_price * 1.05:.2f}

{border}
  Thank you for choosing our theatre!
  Enjoy the movie! 🍿
{border}
"""
    return receipt

def save_receipt_to_file(receipt, booking_id):
    """Save receipt to a text file."""
    filename = f"receipt_{booking_id}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(receipt)
    print(f"Receipt saved to {filename}")
    return filename

if __name__ == "__main__":
    # Demo receipt
    sample_receipt = generate_receipt(
        booking_id=1001,
        customer_name="John Doe",
        movie_title="The Matrix Resurrections",
        theatre_name="PVR Cinemas",
        seat_number="A5",
        show_time="2026-06-19 18:30",
        ticket_price=12.99
    )
    print(sample_receipt)
    save_receipt_to_file(sample_receipt, 1001)
