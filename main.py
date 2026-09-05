from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from Database.db import init_db
from services.admin_service import AdminService
from menus.admin_menu import AdminMenu
from menus.user_menu import UserMenu

console = Console()

def main():
    init_db()

    # Instantiating controller services and menus
    admin_service = AdminService()
    admin_menu = AdminMenu()
    user_menu = UserMenu()

    while True:
        # Full-width panel scaled to match terminal width
        console.print(
            Panel(
                Align.center("[bold magenta]🎪 ENTERPRISE EVENT TICKET MANAGEMENT SYSTEM[/bold magenta]"),
                title="[bold yellow]Welcome[/bold yellow]",
                subtitle="[dim]Role-Based Portal[/dim]",
                style="bold blue",
                expand=True,
                padding=(1, 2)
            )
        )

        console.print("[bold cyan]  1. Admin Portal[/bold cyan]")
        console.print("[bold yellow]  2. User / Customer Portal[/bold yellow]")
        console.print("[bold red]  3. Exit Application[/bold red]")
        console.print("─" * console.width)

        choice = input("\nSelect Module (1-3): ").strip()

        match choice:
            case "1":
                username = input("Enter Admin Username: ").strip()
                password = input("Enter Admin Password: ").strip()
                if admin_service.verify_admin(username, password):
                    console.print("[bold green]✓ Admin Authenticated![/bold green]")
                    admin_menu.show_menu()
                else:
                    console.print("[bold red]❌ Incorrect admin credentials![/bold red]")
            case "2":
                user_menu.show_menu()
            case "3":
                console.print("[bold blue]Exiting Application. Goodbye![/bold blue]")
                break
            case _:
                console.print("[bold red]Invalid choice! Please select 1, 2, or 3.[/bold red]")

if __name__ == "__main__":
    main()