import pandas
import smtplib
import datetime as dt
import random

MY_EMAIL = "YOUR_EMAIL"
PASSWORD = "YOUR_PASSWORD"

right_now = dt.datetime.now()
current_date = right_now.day
current_month = right_now.month
current_month_and_date = (current_month, current_date)

data = pandas.read_csv("birthdays.csv")

for _, row in data.iterrows():
    if row["day"] == current_date and row["month"] == current_month:
        celebrant_name = row["name"]
        celebrant_email = row["email"]
        n = random.randint(1, 3)
        wish_letter = f"./letter_templates/letter_{n}.txt"

        with open(wish_letter) as wishes:
            content = wishes.read()
            birthday_wish = content.replace("[NAME]", celebrant_name)
            msg = f"Subject: Happy Birthday!\n\n{birthday_wish}"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()

            connection.login(user=MY_EMAIL, password=PASSWORD)

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=celebrant_email,
                msg=msg
            )

        print(f"Sending letter_{n}.txt to {celebrant_email}")


