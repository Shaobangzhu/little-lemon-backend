# little-lemon-backend
Meta Back End Developer Capstone Project

## Commands that Usually Used (On Windows OS)
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