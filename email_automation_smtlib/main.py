import smtplib

my_email = "your_gmail"
# normally gamil does not allow directly to access the gmail.
# account > manage > security > app_password > create_app > copy the password 
password = "password"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="receiver_email",msg="Subject:Hello\n\nThis is the body of my email.")
connection.close()