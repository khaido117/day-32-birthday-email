from datetime import datetime
import pandas 
import smtplib
import random

#1 Get the today month date
today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("/Users/khaido/Library/CloudStorage/GoogleDrive-khaitroyy@gmail.com/My Drive/Code/day-32-birthday-email/email_birthday/birthdays.csv")
 
birthday_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}

MY_EMAIL = "khaitroyy@gmail.com"
PASSWORD = "wzhwcympfdytnkdf"

TO_EMAIL = "khaido12365@gmail.com"

#2 Send email function.

def send_email():
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=TO_EMAIL,
                                msg=f"Subject: Happy Birthday \n\n {letter}")
            print("Email sent successfully!")
    except Exception as error_message:
        print(f"An error occured: {error_message}. ")

#3 Select random letter and send email.

if today in birthday_dict:
    file_path = f"/Users/khaido/Library/CloudStorage/GoogleDrive-khaitroyy@gmail.com/My Drive/Code/day-32-birthday-email/birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        content = file.read()
        letter = content.replace("[NAME]", birthday_dict[today]["name"])
        send_email()
else:
    print("Nobody has birthday today.")


