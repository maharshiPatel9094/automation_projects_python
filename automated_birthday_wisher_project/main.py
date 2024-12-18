import smtplib
from datetime import datetime
import pandas
import random

MY_EMAIL = "test@1234.gmail.con"
MY_PASSWORD = "1234546"

# created a tuple for the birthday day and month as they need to be fixed 
today = datetime.now()
today_tuple = (today.month,today.day)

# pandas to read CSV
data = pandas.read_csv("./birthdays.csv")
# print(data)

# birthday dictionary
birthday_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
# print(birthday_dict)

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=birthday_person["email"],msg=f"Subject: Happy Birthday\n\n{contents}") 