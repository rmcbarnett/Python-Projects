
# This project reads through a list of my friends and creates a pandas dataframe.
# If any birthdays fall on that date, a random letter is selected and sent to that friend.


import pandas as pd
import datetime as dt
import smtplib
import random
# read the birthdays.csv into a dataframe

letter_choice = ['letter_1.txt','letter_2.txt','letter_3.txt']

def send_mail(message,to_email):
    my_email = "XXXXXtttest@gmail.com"
    my_password = "XXXXX!"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password= my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg='Subject:Happy birthday\n\n' + message)


# Create a pandas dataframe with the birthdy data
birthday_df = pd.read_csv('./birthdays.csv')
birthday_df =birthday_df.to_dict('records')
print(birthday_df)


# Find any birthdays that fall on today's date
now = dt.datetime.now()
month = now.month
day = now.day



today_birthday = [x for x in birthday_df if x['month'] == month and x['day'] == day]
print(today_birthday)

# Send birthday greetings automatically but still with lots of love :) A letter is selected randomly and the name is inserted.

for birthday in today_birthday:
    letter = random.choice(letter_choice)
    with open(f'./letter_templates/{letter}') as open_letter:
        message = open_letter.read()
        message = message.replace('[NAME]', birthday['name'])
        email = birthday['email']
        print('email sent')
        send_mail(message,email)
