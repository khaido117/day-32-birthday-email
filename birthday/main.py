import smtplib
from email.mime.text import MIMEText
import random
import datetime as dt

MY_EMAIL = "khaitroyy@gmail.com"
PASSWORD = "wzhwcympfdytnkdf"

TO_EMAIL = "khaido12365@gmail.com"

#----------

with open("quotes.txt", mode = "r") as file:
    list_quotes = file.readlines()
    random_quote = random.choice(list_quotes)

def send_email():
    try:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls() #Secure the connection.
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                             to_addrs=TO_EMAIL,
                             msg= f"Subject: Everyday quote \n\n {random_quote}")
        connection.close()
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

#------------------------------

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    send_email()
#------------------------------


