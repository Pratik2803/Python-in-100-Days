import datetime as dt, pandas as pd, configuration, smtplib, ssl
from random import randint


# return current day of the month
def current_day():
    current_date_time = dt.datetime.now()
    today = current_date_time.day
    return today


# return current month of the year
def current_month():
    current_date_time = dt.datetime.now()
    month = current_date_time.month
    return month


# return birthday records on provided day and month
def birthday_records(day, month):
    all_birthdays = pd.read_csv(configuration.BIRTHDAY_FILE_LOC)
    birthday_provided_date = all_birthdays[(all_birthdays['month'] == month) & (all_birthdays['day'] == day)]
    birthday_provided_date = birthday_provided_date[['name', 'email']]
    return birthday_provided_date.to_dict(orient='records')


# decides birthday template
def birthday_letter_template():
    letter_no = str(randint(1, 3))
    return './letter_templates/letter_' + letter_no + '.txt'


# final birthday email body
def birthday_email_body(file):
    with open(file, 'r') as f:
        body = f.read()
        return body


# send email to particular email address
def send_email(receiver_email, message_body):
    default_context = ssl.create_default_context()
    with smtplib.SMTP(host=configuration.SENDER_SERVER, port=configuration.SENDER_PORT) as connection:
        connection.starttls(context=default_context)
        connection.login(user=configuration.EMAIL, password=configuration.PASSWORD)
        connection.sendmail(
            from_addr=configuration.EMAIL,
            to_addrs=receiver_email,
            msg=f'Subject:Hello\n\n {message_body}'
            )
