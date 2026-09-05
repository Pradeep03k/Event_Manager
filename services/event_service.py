from Database.db import get_connection

class EventService:
    def __init__(self):
        self.conn = get_connection()

    def _ensure_connection(self):
        if not self.conn or not self.conn.is_connected():
            self.conn = get_connection()

    # CREATE
    def add_event(self, title, venue, price, seats):
        self._ensure_connection()
        if not self.conn: return False
        
        cursor = self.conn.cursor()
        query = "INSERT INTO events (title, venue, price, seats) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (title, venue, price, seats))
        self.conn.commit()
        cursor.close()
        return True

    # READ
    def get_all_events(self):
        self._ensure_connection()
        if not self.conn: return []
        
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM events")
        records = cursor.fetchall()
        cursor.close()
        return records

    # UPDATE
    def update_event(self, event_id, title, venue, price, seats):
        self._ensure_connection()
        if not self.conn: return False
        
        cursor = self.conn.cursor()
        query = "UPDATE events SET title = %s, venue = %s, price = %s, seats = %s WHERE id = %s"
        cursor.execute(query, (title, venue, price, seats, event_id))
        self.conn.commit()
        affected = cursor.rowcount
        cursor.close()
        return affected > 0

    # DELETE
    def delete_event(self, event_id):
        self._ensure_connection()
        if not self.conn: return False
        
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM events WHERE id = %s", (event_id,))
        self.conn.commit()
        affected = cursor.rowcount
        cursor.close()
        return affected > 0