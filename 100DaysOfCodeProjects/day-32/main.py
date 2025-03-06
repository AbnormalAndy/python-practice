import datetime as dt
import mail_config
import random
import smtplib


with open('quotes.txt', mode='r') as quotes_file:
    quotes = [line.rstrip() for line in quotes_file]


app_email = mail_config.email
password = mail_config.password
smtp = mail_config.smtp
to_email = mail_config.to_email


now = dt.datetime.now()
day_of_week = dt.date(now.year, now.month, now.day).weekday()


if day_of_week != 5 or day_of_week != 6:
    random_quote = random.choice(quotes)

    with smtplib.SMTP(smtp, port=587) as connection:
        connection.set_debuglevel(1)
        connection.starttls()
        connection.login(user=app_email, password=password)
        connection.sendmail(from_addr=app_email,
            to_addrs=to_email,
            msg=f'Subject: Motivational Quote\n\n{random_quote}'
        )









