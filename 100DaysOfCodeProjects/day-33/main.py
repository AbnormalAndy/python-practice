from datetime import datetime
import mail_config
import requests
import smtplib


# response_iss.json()
#{'message': 'success',
#   'timestamp': 1741472289,
#   'iss_position':
#{'latitude': '20.1806',
#   'longitude': '-40.8743'}}


# response_sunrise_sunset.json()
#{'results': {
#   'sunrise': '5:00:11 AM',
#   'sunset': '3:55:25 PM',
#   'solar_noon': '10:27:48 AM',
#   'day_length': '10:55:14',
#   'civil_twilight_begin': '4:10:53 AM',
#   'civil_twilight_end': '4:44:44 PM',
#   'nautical_twilight_begin': '3:09:47 AM',
#   'nautical_twilight_end': '5:45:50 PM',
#   'astronomical_twilight_begin': '2:03:40 AM',
#   'astronomical_twilight_end': '6:51:57 PM'},
#'status': 'OK', 'tzid': 'UTC'}


# 60 - 70 : Latitude Range for Observing
MY_LAT = 66.497231
# 15 - 40 : Longitude Range for Observing
MY_LNG = 25.724880


# Email Information
app_email = mail_config.email
password = mail_config.password
smtp = mail_config.smtp
to_email = mail_config.to_email


# Current Time
time_now = datetime.now()


response_iss = requests.get(url='http://api.open-notify.org/iss-now.json')
response_iss.raise_for_status()


data_iss = response_iss.json()
data_latitude = float(response_iss.json()['iss_position']['latitude'])
data_longitude = float(response_iss.json()['iss_position']['longitude'])


if data_latitude <= 70 and data_latitude >= 60 and data_longitude <= 40 and data_longitude >= 15:
# Used to DEBUG
#if MY_LAT <= 70 and MY_LAT >= 60 and MY_LNG <= 40 and MY_LNG >= 15:
    print('ISS is nearby!')
    response_sunrise_sunset = requests.get(url=f'https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LNG}&formatted=0')
    response_sunrise_sunset.raise_for_status()


    data_sunrise_sunset = response_sunrise_sunset.json()
    data_sunrise = response_sunrise_sunset.json()['results']['sunrise']
    data_sunset = response_sunrise_sunset.json()['results']['sunset']


    data_sunrise_hour = int(data_sunrise.split('T')[1].split(':')[0])
    data_sunset_hour = int(data_sunset.split('T')[1].split(':')[0])


    # Used to DEBUG
    #test_time = 13


    # Determines if it is currently night time so the ISS can be seen.
    if time_now.hour < data_sunrise_hour or time_now.hour > data_sunset_hour:
        # Used to DEBUG
        print("Night time!")
        with smtplib.SMTP(smtp, port=587) as connection:
            # Used to DEBUG
            #connection.set_debuglevel(1)
            connection.starttls()
            connection.login(user=app_email, password=password)
            connection.sendmail(from_addr=app_email,
                to_addrs=to_email,
                msg=f'Subject: ISS ABOVE!\n\nLook UP for the ISS is ABOVE!'
            )
    else:
        print("Day time!")
else:
    print('ISS is NOT nearby!')


