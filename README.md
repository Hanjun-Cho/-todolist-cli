# Calendar App
A Basic Responsive Calendar WebApp and CLI Program

## Project Description:
This is a personal project I decided to work on after starting to use
a Windows Subsystem for Linux (WSL). Used this program as a way to
configure, customize, and get accustomed to Nvim.

The program is built into 3 sections - Backend API, Frontend WebApp, and
Command Line Interface (CLI) Program - which uses **Python (Flask)**, 
**ReactJS** and **NodeJS** respectfully.

## Running the Calendar CLI Program:
Start by cloning - and updating - the directory
```
git clone https://github.com/Hanjun-Cho/Calendar-App
cd Calendar-App
git pull
```

If you're looking to make changes to the program itself to suite your
own needs, the first thing you'll need is a ***secret.py*** file within
the root of the flask directory

Within, you need to include 4 separate variables:
*MYSQL_HOST* which is the ip the mySQL server will be running on
*MYSQL_USER* and *MYSQL_PASSWORD* for the login details into the mySQL server
and *MYSQL_DB* for the specific database this calendar program will be using
```
MYSQL_HOST: localhost
MYSQL_USER: username
MYSQL_PASSWORD: password
MYSQL_DB: database_name
```

From the root of the flask directory, use the following commands
to activate the python virtual environment and to run the flask program
in debug mode:
```
. bin/activate
flask --app app run --debug
```

