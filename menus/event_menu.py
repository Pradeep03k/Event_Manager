from rich.console import Console
from rich.table import Table, Table
from services.event_service import EventService

console = Console()

class EventMenu:
    def __init__(self):
        self.event_service = EventService()

    def display_events(self):
        events = self.event_service.get_all_events()
        if not events:
            console.print("[yellow]No upcoming events available.[/yellow]")
            return

        table = Table(
        title="🎪 Event Catalogue", 
        header_style="bold magenta", 
        width=120,             # Increased overall table width (from 80 to 120)
        padding=(2, 3)         # Increased height/spacing: 2 lines top/bottom, 3 spaces left/right
        )

        # Expand individual column dimensions
        table.add_column("ID", style="cyan", width=15, justify="center")
        table.add_column("Title", style="white", min_width=30)
        table.add_column("Venue", style="white", min_width=30)
        table.add_column("Price (₹)", style="green", width=20, justify="right")
        table.add_column("Seats Left", style="yellow", width=15, justify="center")

        for event in events:
            table.add_row(
                str(event["id"]),
                event["title"],
                event["venue"],
                f"₹{event['price']:.2f}",
                str(event["seats"])
            )

        console.print(table)