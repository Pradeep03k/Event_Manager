class Event:
    def __init__(self, title, venue, price, seats, event_id=None):
        self.id = event_id
        self.title = title
        self.venue = venue
        self.price = price
        self.seats = seats