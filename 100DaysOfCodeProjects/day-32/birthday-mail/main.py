import datetime as dt
import mail_config
import pandas
import random
import smtplib


app_email = mail_config.email
password = mail_config.password
smtp = mail_config.smtp


now = dt.datetime.now()
# Used to DEBUG
#print(now.year, now.month, now.day)


birthdays = pandas.read_csv('birthdays.csv')
# Used to DEBUG
#print(birthdays)


today_birthdays = birthdays[(birthdays['day'] == now.day) & (birthdays['month'] == now.month)]
# Used to DEBUG
#print(today_birthdays)


if len(today_birthdays) == 0:
    print('There are NO birthdays today!')


elif len(today_birthdays) > 1:
    print(f'There are {len(today_birthdays)} birthdays today!')


    for count in range(len(today_birthdays)):
        with open(f'letter_templates/letter_{random.randint(1,3)}.txt') as letter_file:
            birthday_letter = letter_file.readlines()


        new_birthday_letter = ''.join([name.replace('[NAME]', today_birthdays['names'][count].title()) for name in birthday_letter])
        # Used to DEBUG
        #print(new_birthday_letter) 


        with smtplib.SMTP(smtp, port=587) as connection:
            # Used to DEBUG
            #connection.set_debuglevel(1)
            connection.starttls()
            connection.login(user=app_email, password=password)
            connection.sendmail(from_addr=app_email,
                to_addrs=today_birthdays['email'][count],
                msg=f'Subject: Happy Birthday!\n\n{new_birthday_letter}'
            )


        print(f'Sent email to {today_birthdays['names'][count].title()}!')


else:
    print('There is a birthday today!')


    with open(f'letter_templates/letter_{random.randint(1,3)}.txt') as letter_file:
        birthday_letter = letter_file.readlines()


    new_birthday_letter = ''.join([name.replace('[NAME]', today_birthdays['names'][0].title()) for name in birthday_letter])
    # Used to DEBUG
    #print(new_birthday_letter)

    
    with smtplib.SMTP(smtp, port=587) as connection:
        # Used to DEBUG
        #connection.set_debuglevel(1)
        connection.starttls()
        connection.login(user=app_email, password=password)
        connection.sendmail(from_addr=app_email,
            to_addrs=today_birthdays['email'][0],
            msg=f'Subject: Happy Birthday!\n\n{new_birthday_letter}'
        )


    print(f'Sent email to {today_birthdays['names'][0].title()}!')


