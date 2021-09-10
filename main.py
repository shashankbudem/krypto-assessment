import app
import requests
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
# from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.MIMEText import MIMEText

response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false").json()
currency = np.array(response)

def send_mail_sell(email):
    fromaddr = "shashank4305@gmail.com"
    toaddr = email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Test Mail"
    body = "The price has raised to your desired level!! check it"
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromaddr, "bringmethanos")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("MAil sent")

def send_mail_buy(email):
    fromaddr = "shashank4305@gmail.com"
    toaddr = email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Test Mail"
    body = "The price has fallen down!! Check it"
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromaddr, "bringmethanos")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    print("MAil sent")

while(True):
    for user_dictionary in app.sell:
        for key,value in user_dictionary:
            for alert in value:
                for x in currency:
                    if x['id'] == key:
                        if alert[0] >= x['current_price']:
                            send_mail_sell(user_dictionary)

    for user_dictionary in app.buy:
        for key,value in user_dictionary:
            for alert in value:
                for x in currency:
                    if x['id'] == key:
                        if alert[0] <= x['current_price']:
                            send_mail_buy(user_dictionary)






