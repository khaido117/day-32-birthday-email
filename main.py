# import smtplib
# from email.mime.text import MIMEText

# my_email = "khaitroyy@gmail.com"
# password = "wzhwcympfdytnkdf"

# to_email = "khaido12365@gmail.com"

# # Create a MIMEText object with the email content

# try:
#     connection = smtplib.SMTP("smtp.gmail.com", 587)
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=to_email, msg= "Subject: Hello \n \n This is my message.")
#     connection.close()
#     print("Email sent successfully!")
# except Exception as e:
#     print(f"An error occurred: {e}")

import datetime as dt

now = dt.datetime.now()
date = now.date
print(date)
