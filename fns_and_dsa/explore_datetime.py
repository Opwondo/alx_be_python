from datetime import datetime, timedelta

# Display current date and time
def display_current_datetime():
    current_date = datetime.now()  # current date and time
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")
    return current_date

# Calculate future date
def calculate_future_date(days_to_add):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)  # future date
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date

if __name__ == "__main__":
    
    display_current_datetime()

    number_of_days = int(input("Enter the number of days to add to the current date: "))

    calculate_future_date(number_of_days)
