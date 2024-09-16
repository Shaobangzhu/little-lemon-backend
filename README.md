# little_lemon_backend
Meta Back End Developer Capstone Project

## Commands that Usually Used (On Windows OS)
### Powershell Commands
python -m venv capstone <br />
capstone\Scripts\activate <br />
pip install django <br />
**create a django project:** django-admin startproject littlelemon <br />
**run development server:** cd littlelemon | python manage.py runserver <br />
**create a django app:** python manage.py startapp restaurant <br />
**install client:** pip3 install mysqlclient <br />

### Database Commands
create database littlelemon; <br />
use littlelemon; <br />
CREATE USER 'django'@'localhost' IDENTIFIED BY 'password'; <br />
GRANT ALL PRIVILEGES ON littlelemon.* TO 'django'@'localhost'; <br />

### Powershell Commands related to Database
python3 manage.py migrate <br />
python3 manage.py makemigrations <br />
python manage.py createsuperuser <br />
#user:super <br />
#email: super@gmail.com <br />
#password: 123 <br />
pip3 install djangorestframework <br />

### API Samples
GET in http://localhost:8000/api/menu/1 <br />
{
    "id": 1, 
    "title": "Menu 1",
    "price": "123.00", 
    "inventory": 4 
} <br />

GET in http://localhost:8000/api/menu <br />
Get all menus <br />

POST http://localhost:8000/api/menu/ <br />
BODY <br />
{
    "title": "Menu 2",
    "price": "123.00",
    "inventory": 3
} <br />
RESULT <br />
{
    "id": 2,
    "title": "Menu 2",
    "price": "123.00",
    "inventory": 3
} <br />

GET in http://localhost:8000/api/booking/tables <br />
[
    {
        "id": 1,
        "name": "Booking 1",
        "number_of_guests": 6,
        "booking_date": "2023-06-06T17:41:53Z"
    }
]<br />

POST http://localhost:8000/api/api-token-auth/ <br />
{
    "token": "YOUR_API_TOKEN"
}<br />

Add authorization to the endpoints, so you have to send a header in the request with the Authorization title: Token [VALUE] <br />
pip install djoser <br />

navigate to http://127.0.0.1:8000/auth/token/login/ to get the token <br />
user: "YOUR_SUPERUSER_NAME" 
password: "YOUR_PASSWORD"

use http://127.0.0.1:8000/auth/token/logout/ to logout with the token in the header <br />

### Testing
python manage.py test <br />
GRANT ALL PRIVILEGES ON `test_littlelemon`.* TO 'django'@'localhost'; <br />
FLUSH PRIVILEGES; <br />

To execute the available unittests, please open the Visual Studio terminal and enter the following command: python manage.py test tests/. Please ensure that you have activated the virtual environment and navigated into the 'littlelemon' directory prior to running the unit-tests command.<br />

Utilize this path to verify that the web application is serving static HTML content, inclusive of images and styling. /restaurant <br />

For testing, you can make use of the following API endpoints with Insomnia or Postman clients. Alternatively, feel free to explore them through your browser of choice. <br />

DJOSER endpoint, for instance, to perform a POST request and register a new user. /auth/users/ <br />

To log in and obtain an authentication token. /api-token-auth/ <br />

To log in using the DJOSER endpoint. /auth/token/login <br />

Menu items /api/menu/ /api/menu/{menuItemId} <br />

Table reservations /api/booking/tables/ /api/booking/tables/{bookingId} <br />

## Notes
### Virtual Enviroment
**Install the Virtual Environment:** pip3 install virtualenv <br />
**Init Vritual Environment:** python -m venv **your_project_name** <br />
**Activate Virtual Environment:** .\your_project_name\Scripts\Activate.ps1 <br />
**Deactivate Virtual Environment:** deactivate <br />

### Django Related
**Install Django:** pip3 install django <br />
**Create a Django Project:** django-admin startproject PROJECT_NAME <br />
**Create an App:** python manage.py startapp app_name <br />
**Run Django Server:** python manage.py runserver <br />
**Open Django Shell in Cmdline:** python manage.py shell <br />

### Database Related
**Add a New Model or Effect Changes:** python manage.py makemigrations <br />
**Migrating Models of Installed Apps(Apply the Tasks in the Migration File):** python manage.py migrate <br />
**Revert Back to a Specific Version:** python manage.py migrate app_name migration_file_name <br />
**There are Two Unmigrated Changes in the Model, Run:** python manage.py showmigrations <br />
**Shows the SQL Query or Queries Executed:** python manage.py sqlmigrate app_name migration_file_name

### ORM Commands
**Import a Model:** from app_name import model_name <br />
**Show all the Element in the ORM:** model_name.objects.all() <br />
**Add an Element in the Model:** model_name.objects.create(attribute1 = 'xxx', attribute2 = 'xxx' ...) <br />
**Get an Element by ID:** model_name.objects.get(id=id_number) <br />
**Get an Element by Filter:** model_name.objects.filter(filter_content) <br />

### Admin
**Create a Super User:** python manage.py createsuperuser

### MySQL
**Start the MySQL command line client:** mysql -u root -p

## Learn API in Python

### PIPENV related

**Install pipenv:** pip install pipenv <br />
**Install Django in pipenv:** pipenv install django <br />
**Set the PIPENV_IGNORE_VIRTUALENVS environment variable:** set PIPENV_IGNORE_VIRTUALENVS=1 <br />
**Activate Virtual Environment:** pipenv shell <br />
**Shut Down Virtual Environment:** exit <br />
