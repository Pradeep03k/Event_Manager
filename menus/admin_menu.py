from rich.console import Console
from rich.table import Table
from services.event_service import EventService
from services.booking_service import BookingService
from menus.event_menu import EventMenu
from menus.report_menu import ReportMenu

console = Console()

class AdminMenu:
    def __init__(self):
        self.event_service = EventService()
        self.booking_service = BookingService()
        self.event_menu = EventMenu()
        self.report_menu = ReportMenu()

    def show_menu(self):
        while True:
            console.print("\n[bold cyan]--- Admin Control Panel ---[/bold cyan]")
            console.print("[bold blue]1. Add New Event[/bold blue]")
            console.print("[bold blue]2. View All Events[/bold blue]")
            console.print("[bold blue]3. Update Event Details[/bold blue]")
            console.print("[bold blue]4. Delete Event[/bold blue]")
            console.print("[bold blue]5. View All User Bookings [/bold blue]")
            console.print("[bold blue]6. Export Bookings to Excel File[/bold blue]")
            console.print("[bold blue]7. Back to Main Menu[/bold blue]")


            choice = input("\nSelect Option (1-7): ")

            match choice:
                case "1":
                    self.add_event()
                case "2":
                    self.event_menu.display_events()
                case "3":
                    self.update_event()
                case "4":
                    self.delete_event()
                case "5":
                    self.view_all_bookings()
                case "6":
                    self.report_menu.handle_export()
                case "7":
                    break
                case _:
                    console.print("[red]Invalid selection![/red]")

    def add_event(self):
        title = input("Enter Event Title: ")
        venue = input("Enter Venue: ")
        try:
            price = float(input("Enter Price (₹): "))
            seats = int(input("Enter Total Seats: "))
        except ValueError:
            console.print("[red]Invalid numeric input.[/red]")
            return

        if self.event_service.add_event(title, venue, price, seats):
            console.print("[bold green]✓ Event created successfully![/bold green]")

    def update_event(self):
        self.event_menu.display_events()
        try:
            event_id = int(input("Enter Event ID to update: "))
            title = input("Enter New Title: ")
            venue = input("Enter New Venue: ")
            price = float(input("Enter New Price (₹): "))
            seats = int(input("Enter New Seat Count: "))
        except ValueError:
            console.print("[red]Invalid input format.[/red]")
            return

        if self.event_service.update_event(event_id, title, venue, price, seats):
            console.print("[bold green]✓ Event updated successfully![/bold green]")
        else:
            console.print("[bold red] Event ID not found [/bold red]")

    def delete_event(self):
        self.event_menu.display_events()
        try:
            event_id = int(input("Enter Event ID to delete: "))
        except ValueError:
            console.print("[red]Invalid ID.[/red]")
            return

        if self.event_service.delete_event(event_id):
            console.print("[bold green]✓ Event deleted successfully![/bold green]")
        else:
            console.print("[bold red] Event ID not found [/bold red]")

    def view_all_bookings(self):
        bookings = self.booking_service.get_all_bookings()
        if not bookings:
            console.print("[yellow]No customer bookings found.[/yellow]")
            return

        table = Table(title="📋 Master Booking List", header_style="bold green",width=80,padding=(1,2))
        table.add_column("Booking ID", style="yellow",width=12,justify="center")
        table.add_column("Customer Name", style="white",width=20,min_width=15)
        table.add_column("Event Title", style="cyan",width=30,min_width=20)
        table.add_column("Tickets", style="magenta",width=10,justify="center")
        table.add_column("Total Paid", style="bold yellow",width=15,justify="right")

        for row in bookings:
            table.add_row(
                str(row["id"]),
                row["customer_name"],
                row["event_title"],
                str(row["ticket_count"]),
                f"₹{row['total_price']:.2f}"
            )

        console.print(table)