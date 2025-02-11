from datetime import datetime
import calendar

def calculate_devices_years():
    devices = {
        "MacBook": "25-Jan-2023",
        "iPad": "03-Oct-2021",
        "iPhone 14": "18-Oct-2023",
        "Mi 12 Pro": "25-Sep-2022",
        "R15M": "01-Jul-2022",
        "KTM 390 Adv": "14-Feb-2024",
        "ASUS TUF Laptop": "18-Oct-2023"
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

def calculate_age(dob_str):
    dob = datetime.strptime(dob_str, "%d-%b-%Y")
    today = datetime.today()
    
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day
    
    if days < 0:
        months -= 1
        last_month = today.month - 1 if today.month > 1 else 12
        last_month_year = today.year if today.month > 1 else today.year - 1
        days += calendar.monthrange(last_month_year, last_month)[1]

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

# Call functions correctly
calculate_devices_years()

# Provide a valid DOB input
dob_input = "03-Jan-1995"
years, months, days = calculate_age(dob_input)
print(f"Your age is: {years} years, {months} months, and {days} days")
