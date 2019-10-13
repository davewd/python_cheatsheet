from pytz import timezone


def timezone_example():
    from datetime import datetime
    import pytz
    d = datetime.now()
    timezone = pytz.timezone("Australia/Sydney")
    date_timezone_aware = timezone.localize(d)
    print(f"The Time is {date_timezone_aware} where the TZ is {date_timezone_aware.tzinfo}")

    #pytz
    # https://www.journaldev.com/23370/python-pytz Thanks !
    # interesting info on the country / city combos : https://www.iso.org/iso-3166-country-codes.html
    print('all_timezones =', pytz.all_timezones, '\n')

    print('country_names =')
    for key, val in pytz.country_names.items():
        print(key, '=', val, end=',')
    print('\n')
    print('IN full name =', pytz.country_names['IN'])