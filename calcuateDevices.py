from datetime import datetime

def calculate_devices_years():
    devices = {
        "MacBook": "25-Jan-2023",
        "iPad": "03-Oct-2021",
        "iPhone 14": "18-Oct-2023",
        "Mi 12 Pro": "25-Sep-2022",
        "R15M": "01-Jul-2022",
        "KTM 390 Adv": "14-Feb-2023"
    }

    current_date = datetime.now()

    def calculate_lifespan(purchase_date):
        purchase_date = datetime.strptime(purchase_date, "%d-%b-%Y")
        delta = current_date - purchase_date
        years = delta.days // 365
        months = (delta.days % 365) // 30
        return years, months

    for device, date in devices.items():
        years, months = calculate_lifespan(date)
        print(f"{device} Age: {years} years, {months} months")

calculate_devices_years()
