class Booking:
    def __init__(self, customer_name, event_id, ticket_count, total_price, booking_id=None):
        self.id = booking_id
        self.customer_name = customer_name
        self.event_id = event_id
        self.ticket_count = ticket_count
        self.total_price = total_price