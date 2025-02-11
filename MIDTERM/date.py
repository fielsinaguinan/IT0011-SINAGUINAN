import datetime
def format_date(date_str):
    """Converts a date string from mm/dd/yyyy to a more readable format."""
    try:
        date_obj = datetime.datetime.strptime(date_str, '%m/%d/%Y')
        return date_obj.strftime('%B %d, %Y')
    except ValueError:
        return "Invalid date format. Please use mm/dd/yyyy."

date_input = input("Enter the date (mm/dd/yyyy): ")
formatted_date = format_date(date_input)
print("Date Output:", formatted_date)
