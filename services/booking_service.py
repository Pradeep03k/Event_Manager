from Database.db import get_connection

class BookingService:
    def __init__(self):
        self.conn = get_connection()

    def _ensure_connection(self):
        if not self.conn or not self.conn.is_connected():
            self.conn = get_connection()

    # CREATE
    def book_ticket(self, customer_name, event_id, count):
        self._ensure_connection()
        if not self.conn: return False, "Database connection error."

        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM events WHERE id = %s", (event_id,))
        event = cursor.fetchone()

        if not event:
            cursor.close()
            return False, "Event ID not found."

        if event["seats"] < count:
            cursor.close()
            return False, f"Insufficient seats. Only {event['seats']} remaining."

        total_price = float(event["price"]) * count

        cursor.execute("UPDATE events SET seats = seats - %s WHERE id = %s", (count, event_id))
        cursor.execute(
            "INSERT INTO bookings (customer_name, event_id, ticket_count, total_price) VALUES (%s, %s, %s, %s)",
            (customer_name, event_id, count, total_price)
        )
        self.conn.commit()
        cursor.close()
        return True, f"Successfully booked {count} tickets! Total: ₹{total_price:.2f}"

    # READ ALL (Admin)
    def get_all_bookings(self):
        self._ensure_connection()
        if not self.conn: return []

        cursor = self.conn.cursor(dictionary=True)
        query = """
        SELECT b.id, b.customer_name, e.title as event_title, b.ticket_count, b.total_price 
        FROM bookings b 
        JOIN events e ON b.event_id = e.id
        """
        cursor.execute(query)
        records = cursor.fetchall()
        cursor.close()
        return records

    # READ BY USER (User)
    def get_user_bookings(self, customer_name):
        self._ensure_connection()
        if not self.conn: return []

        cursor = self.conn.cursor(dictionary=True)
        query = """
        SELECT b.id, e.title as event_title, b.ticket_count, b.total_price 
        FROM bookings b 
        JOIN events e ON b.event_id = e.id
        WHERE b.customer_name = %s
        """
        cursor.execute(query, (customer_name,))
        records = cursor.fetchall()
        cursor.close()
        return records

    # DELETE / CANCEL
    def cancel_booking(self, booking_id, customer_name):
        self._ensure_connection()
        if not self.conn: return False, "Database connection error."

        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM bookings WHERE id = %s AND customer_name = %s", (booking_id, customer_name))
        booking = cursor.fetchone()

        if not booking:
            cursor.close()
            return False, "Booking ID not found for this user name."

        cursor.execute("UPDATE events SET seats = seats + %s WHERE id = %s", (booking["ticket_count"], booking["event_id"]))
        cursor.execute("DELETE FROM bookings WHERE id = %s", (booking_id,))
        self.conn.commit()
        cursor.close()
        return True, "Booking cancelled successfully and seats restored."