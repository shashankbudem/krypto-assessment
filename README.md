# krypto-assessment
Created a price alert application that triggers an email when the user’s target price is achieved using flask and REST API.
Login page is created to authenticate the users.
The email is considered to be the primary key
Create page is made available to set alerts , where user enters the limit price of cryptocurrency and the name(id) of cryptocurrency.
The current value of the cryptocurrencies is been fetched using requests library in python and is compared with the limit price set by 

1. Run app.py
2. Create module will create an alert and send email.
3. delete, status modules are incomplete.
4. We have used dictionaries to store the data (Haven't used any DBMS).
5. We have created a seperate server file which has an infinite loop that verifies all the created limit amount with the curent price of respective crytocurrency.   
