import smtplib
import datetime as dt
import random

my_email = "myemail"
password = "1234"

# date and time
current_time = dt.datetime.now()
weekday = current_time.weekday()
if weekday == 4:
    with open("./quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)
        # object
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="receiver_add",msg=f"Subject: Motivation\n\n{random_quote}")
     

# import smtplib

# my_email = "your_gmail"
# # normally gamil does not allow directly to access the gmail.
# # account > manage > security > app_password > create_app > copy the password 
# password = "password"
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,to_addrs="receiver_email",msg="Subject:Hello\n\nThis is the body of my email.")
# connection.close()