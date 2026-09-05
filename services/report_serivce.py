from rich.console import Console
from services.export_service import ExportService

console = Console()

class ReportMenu:
    def __init__(self):
        self.export_service = ExportService()

    def handle_export(self):
        console.print("[cyan]Enter target export path (Press Enter for default: exports/Booking_Report.xlsx):[/cyan]")
        user_input = input("Path: ").strip()
        target_path = user_input if user_input else "exports/Booking_Report.xlsx"

        success, msg = self.export_service.export_to_excel(target_path)
        if success:
            console.print(f"[bold green]🚀 Data exported successfully to '{msg}'![/bold green]")
        else:
            console.print(f"[bold red]❌ {msg}[/bold red]")