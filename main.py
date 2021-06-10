##################### Extra Hard Starting Project ######################


import random
import pandas
import datetime as dt
import smtplib


#----------------------------SEND MAILS------------------------------#
def send_email(letter):
    my_email="*******@gmail.com" #USE YOUR OWN ID AND PASSWORD
    password="*****"
    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()

        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="nilabja.sanyal@gmail.com",
                            msg=f"subject: HAPPY BIRTHDAY!!\n\n{letter}")



info = pandas.read_csv("birthdays.csv")
info_list = info.to_dict(orient="records")

for dictionarie in info_list:

    name=dictionarie["name"]

    bday_day=dictionarie["day"]
    bday_month=dictionarie["month"]

    current_time=dt.datetime.now()
    current_day=current_time.day
    current_month=current_time.month

    #UPDATING THE LETTER

    updated_letter = ""
    list_of_letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt",
                       "letter_templates/letter_2.txt"]
    letter_address = random.choice(list_of_letters)
    with open(letter_address) as letter:
        line_list = letter.readlines()

    new_letter_line = line_list[0].replace("[NAME]", name)  # HAVE TO CHANGE MOM
    line_list[0] = new_letter_line
    for lines in line_list:
        updated_letter += f"{lines}"


    if current_day==bday_day and current_month==bday_month:
        print(updated_letter)
        send_email(updated_letter)



