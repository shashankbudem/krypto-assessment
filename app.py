from flask import Flask, render_template, redirect, url_for, request
import requests
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)
users_pass = {}

current_user = ""
set_value = 0
crypto = ""
cur = 0

response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false").json()
currency = np.array(response)

for i in currency:
    if i['id'] == crypto:
        cur = i['current_price']
        break

sell = []
buy = []
if current_user not in list(users_pass.keys()):
    try:
        if cur == set_value:
            fromaddr = "shashank4305@gmail.com"
            toaddr = current_user
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Test Mail"
            body = "It has already reached the value"
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(fromaddr, "bringmethanos")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()
    except:
        print("Mail not sent")
    print("MAil sent")

    if cur < set_value:
        sell.append({current_user:[{crypto:[[cur, set_value]]}]})
        # users_pass[current_user] = "default"

    if cur > set_value:
        buy.append({current_user:[{crypto:[[cur, set_value]]}]})
        # users_pass[current_user] = "default"

else:
    if cur == set_value:
        print("Sending email")
    if cur < set_value:
        flag = 0
        for users in sell:
            for key_user in users:
                if key_user == current_user:
                    # print("found ",user)
                    # print(users[key_user])
                    for dict_of_cryptos in users[key_user]:
                        for key_crypto in dict_of_cryptos:
                            temp = []
                            if crypto in list(dict_of_cryptos.keys()):
                                dict_of_cryptos[crypto].append([cur, set_value])
                                # temp.append([cur, set])
                            else:
                                # dict_of_cryptos[crypto] = [cur, set]
                                users[key_user].append({crypto: [[cur, set_value]]})
                                flag = 1
                                break
                        if flag == 1:
                            break


    if cur > set:
        flag = 0
        for users in buy:
            for key_user in users:
                if key_user == current_user:
                    # print("found ",user)
                    # print(users[key_user])
                    for dict_of_cryptos in users[key_user]:
                        for key_crypto in dict_of_cryptos:
                            if crypto in list(dict_of_cryptos.keys()):
                                # dict_of_cryptos[crypto].append([cur, set])
                                break
                            else:
                                # dict_of_cryptos[crypto] = [cur, set]
                                users[key_user].append({crypto:[[cur, set_value]]})
                                flag=1
                                break
                        if flag == 1:
                            break


def add(username,password):
    if username not in list(users_pass.keys()):
        users_pass[username] = password
        print(users_pass)



@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        set_value = request.form["setvalue"]
        crypto = request.form["crypto"]
    return render_template('create.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        add(username,password)
        current_user = username
        return render_template('home.html')
    return render_template('index.html', error=error)

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    return render_template('delete.html')

@app.route('/status', methods=['GET', 'POST'])
def status():
    return render_template('status.html')


if __name__ == '__main__':
    app.run(debug = True,threaded = True)
