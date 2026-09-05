from rich.console import Console
from services.booking_service import BookingService
from menus.event_menu import EventMenu

console = Console()

class BookingMenu:
    @staticmethod
    def handle_booking():
        EventMenu.display_events()
        customer = input("Enter your name: ")
        try:
            event_id = int(input("Enter Event ID: "))
            count = int(input("Enter ticket quantity: "))
        except ValueError:
            console.print("[red]Invalid numerical entry.[/red]")
            return

        success, msg = BookingService.book_ticket(customer, event_id, count)
        if success:
            console.print(f"[bold green]✓ {msg}[/bold green]")
        else:
            console.print(f"[bold red]❌ {msg}[/bold red]")