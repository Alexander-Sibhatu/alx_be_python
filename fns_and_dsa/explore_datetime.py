import datetime

# Get the current date and time
current_date = datetime.datetime.now()

formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

def display_current_datetime():
    print("Current date and time: ", formatted_date)


display_current_datetime()



current_date = datetime.date.today()

def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + datetime.timedelta(days=days_to_add)
    
    # Print the future date in "YYYY-MM-DD" format
    print("Future date: ", future_date.strftime("%Y-%m-%d"))

calculate_future_date()