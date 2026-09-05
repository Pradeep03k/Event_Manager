import os
import pandas as pd
from services.booking_service import BookingService

class ExportService:
    def __init__(self):
        self.booking_service = BookingService()

    def export_to_excel(self, file_path="exports/Booking_Report.xlsx"):
        data = self.booking_service.get_all_bookings()
        if not data:
            return False, "No bookings found to export."

        # Extract directory and ensure it exists
        folder_path = os.path.dirname(file_path)
        if folder_path and not os.path.exists(folder_path):
            os.makedirs(folder_path)

        if not file_path.endswith(".xlsx"):
            file_path += ".xlsx"

        df = pd.DataFrame(data)
        df.rename(columns={
            "id": "Booking ID",
            "customer_name": "Customer Name",
            "event_title": "Event Name",
            "ticket_count": "Tickets",
            "total_price": "Total Price (INR)"
        }, inplace=True)

        df.to_excel(file_path, index=False, engine="openpyxl")
        return True, file_path