from datetime import datetime
def date(date_str):
    input = "%m/%d/%Y"
    output = "%B %d, %Y"
    try:
        date_obj = datetime.strptime(date_str, input)
        return date_obj.strftime(output)
    except ValueError:
        return "Invalid date format. Please use mm/dd/yyyy."

if __name__ == "__main__":
    print("_________________________________________________")
    date = input("Enter the date (mm/dd/yyyy): ")
    hdate = date(date)
    print("Date Output:", hdate)
    print("_________________________________________________")