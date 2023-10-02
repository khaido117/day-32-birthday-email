##################### Extra Hard Starting Project ######################

import datetime as dt 
import pandas 
from smtplib

# 1. Update the birthdays.csv

birthday = pandas.read_csv("/Users/khaido/Library/CloudStorage/GoogleDrive-khaitroyy@gmail.com/My Drive/Code/day-32-birthday-email/birthday-wisher-extrahard-start/birthdays.csv")
birthday_list = birthday[birthday.columns[3]].tolist()
#print(birthday_list)


# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
today_date = now.date()


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv


# 4. Send the letter generated in step 3 to that person's email address.



print(birthday)

