# save email template into variable
with open(file='Input/Letters/email_template.txt', mode='r', encoding='utf-8') as f:
    template_text = f.read()

# save all email invitees names in a list
with open(file='./Input/Names/invited_names.txt', mode='r', encoding='utf-8') as f:
    names = f.readlines()

# create ready to send email for each invitee
for name in names:
    name = name.strip('\n')
    new_letter = template_text.replace('[Name]', name)
    with open(file=f'./Output/send_letter_to_{name}.txt', mode='w') as f:
        f.write(new_letter)

