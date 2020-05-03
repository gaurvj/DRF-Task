# DRF-Task
A Django Get REST api  task.which is using Python(3.5),Django(2.2) and Sqllite(DB.This project also contain a django custom command to insert dummy data into the db.

Technologies Used Python(3.5) Django(2.2) Sqllite3

Install

- pip install -r requirements.txt

Migrations

- python manage.py makemigrations
- python manage.py migrate

Commands

- python python manage.py create_dummy_data_into_userinfo_and_activity_table

Api Endpoint

- /user_activity_log/

Steps To Follow by using some of above commands:-
  - First download the Python(3.5) along with pip in your system.
  - Install all requirement using this command "pip install –r requirement.txt".
  - Go into mytask folder where we have manage.py file.
  - Run command "python manage.py makemigrations" and "python manage.py migrate".
  - To insert dummy data in db run command "python python manage.py create_dummy_data_into_userinfo_and_activity_table".
  - Now run python local server using "python manage.py runserver".
  - Hit this url in browser http://localhost:8000/user_activity_log/ to get the data.
