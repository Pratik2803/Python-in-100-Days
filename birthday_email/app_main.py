import utility

current_day = utility.current_day()
current_month = utility.current_month()

today_birthdays = utility.birthday_records(day=current_day, month=current_month)

if today_birthdays:
    birthday_template = utility.birthday_letter_template()
    email_body = utility.birthday_email_body(file=birthday_template)
    for birthday in today_birthdays:
        msg = email_body.replace('[NAME]', birthday['name'])
        email_to = birthday['email']
        utility.send_email(receiver_email=email_to, message_body=msg)








