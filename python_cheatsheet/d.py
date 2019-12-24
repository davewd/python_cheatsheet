



# Thank-You https://medium.com/towards-artificial-intelligence/datetime-manipulations-with-python-de57aa7e3439
def datetime_examples():
    """
    docstring here
    """
    from datetime import date
    from datetime import time
    from datetime import datetime

    import calendar
    today = date.today();
    print(f"The Date today is {today}")
    print(f"The constituent parts of the date today are : Day {today.day} | Month {today.month} | Year {today.year}")
    print("Lets convert this to strings")

    weekday = today.weekday()
    weekdayName = calendar.day_name[weekday]
    monthName = calendar.month_name[today.month]
    print(f"It's a {weekdayName} in {monthName}")

    now = datetime.now();
    print(f"Ok to the millisecond its : {now}")
    print(f"If i were to only think interms of time : {now.time()}")
    
    #NB the timezone is 'None' see the timezone section for how to enable it.
    timeZone = now.tzname()
    print(f"Timezone is unset {timeZone}")

    #Adding relative amounts of time / dates see timedelta.


# https://powerfulpython.com/blog/checking-dict-keys/
def dictionary_manipulation() :
    return None;