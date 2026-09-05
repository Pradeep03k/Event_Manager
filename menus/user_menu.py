from rich.console import Console
from rich.table import Table
from services.booking_service import BookingService
from menus.event_menu import EventMenu

console = Console()

class UserMenu:
    def __init__(self):
        self.booking_service = BookingService()
        self.event_menu = EventMenu()

    def show_menu(self):
        while True:
            console.print("\n[bold yellow]--- Customer User Portal ---[/bold yellow]")
            console.print("\n[bold cyan]--- User Menu ---[/bold cyan]")
            console.print("[bold blue]1. Browse Events[/bold blue]")
            console.print("[bold blue]2. Book Tickets[/bold blue]")
            console.print("[bold blue]3. View My Bookings[/bold blue]")
            console.print("[bold blue]4. Cancel Booking[/bold blue]")
            console.print("[bold blue]5. Back to Main Menu[/bold blue]")


            choice = input("\nSelect Option (1-5): ")

            match choice:
                case "1":
                    self.event_menu.display_events()
                case "2":
                    self.book_ticket()
                case "3":
                    self.view_my_bookings()
                case "4":
                    self.cancel_booking()
                case "5":
                    break
                case _:
                    console.print("[red]Invalid option![/red]")

    def book_ticket(self):
        self.event_menu.display_events()
        customer = input("Enter your name: ").strip()
        try:
            event_id = int(input("Enter Event ID: "))
            count = int(input("Enter number of tickets: "))
        except ValueError:
            console.print("[red]Invalid numeric entry.[/red]")
            return

        success, msg = self.booking_service.book_ticket(customer, event_id, count)
        if success:
            console.print(f"[bold green]✓ {msg}[/bold green]")
        else:
            console.print(f"[bold red]❌ {msg}[/bold red]")

    def view_my_bookings(self):
        customer = input("Enter your registered name: ").strip()
        bookings = self.booking_service.get_user_bookings(customer)

        if not bookings:
            console.print(f"[yellow]No active bookings found for '{customer}'.[/yellow]")
            return

        table = Table(title=f"🎟️ Bookings for {customer}", header_style="bold yellow",min_width=80,padding=(1,2))
        table.add_column("Booking ID", style="cyan",width=12,justify="center")
        table.add_column("Event Title", style="white",width=30,min_width=20)
        table.add_column("Tickets", style="magenta",width=10,justify="center")
        table.add_column("Total Price", style="bold green",width=15,justify="right")

        for row in bookings:
            table.add_row(
                str(row["id"]),
                row["event_title"],
                str(row["ticket_count"]),
                f"₹{row['total_price']:.2f}"
            )

        console.print(table)

    def cancel_booking(self):
        customer = input("Enter your registered name: ").strip()
        try:
            booking_id = int(input("Enter Booking ID to cancel: "))
        except ValueError:
            console.print("[red]Invalid ID format.[/red]")
            return

        success, msg = self.booking_service.cancel_booking(booking_id, customer)
        if success:
            console.print(f"[bold green]✓ {msg}[/bold green]")
        else:
            console.print(f"[bold red]❌ {msg}[/bold red]")