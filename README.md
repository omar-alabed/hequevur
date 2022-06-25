## About Hequevur

Hequevur is a basic HR system


## Prerequisites

To Set Up the project properly without facing issues, please do the below using your favorite method (depending on your OS)

* [frontend Prerequisite]
* download and install node js

* [setup database]
* install mariadb-server 
* install libmariadbclient-dev
* login into mysql: `sudo mysql`
* create a new user : `create USER ‘someone’@‘localhost' IDENTIFIED BY 'SimplePass1';`
* grant privileges to our user: `GRANT ALL PRIVILEGES ON * . * to 'someone'@'localhost' WITH GRANT OPTION;`
* create a new database: `CREATE DATABASE hequavur_db;`

## Download and Installation

To begin using this app, choose one of the following options to get started:

* [Clone, or Download this repo]
* Install Python 3.6.8
* Create a new virtualenv called venv: `python3 -m venv venv`
    
If all went well then your command line prompt should now start with (venv).
If your command line prompt does not start with (venv) at this point, try running `source venv/bin/activate`
install required python packages by running `pip install -r requirements.txt`
migrate database migrations to your pre-set database: `python manage.py migrate`
run application using: `python manage.py runserver`
cd into frontend then `npm install` then `npm start dev`
create three departments by sending three POST requests to `/api/department` holding desired department name as department_name in the request body
or by going to `localhost:3000` then departments then add new departments using the GUI

## API Calls
After running the server, access the three API end points via the links below (following the default localhost and port `http://127.0.0.1:8000/`)
* List all candidates (Admin Only): `api/candidate/` -- GET
* Create a new candidate : `api/candidate/create/` -- POST
* Edit existing file (upload a new file/ Admin Only):`api/file/<int:pk>/` -- PATCH
* Get existing file :`api/file/<int:pk>/` -- GET

* Create a new department or List all departments: `api/department/` -- POST, GET
* Update, Delete or Get a department : `api/department/<int:pk>/` -- GET, DELETE, PUT, PATCH


