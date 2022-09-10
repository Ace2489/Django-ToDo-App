
<h1 align="center">
  Django To-Do App
</h1>

<h4 align="center">A to-do app built using the Django framework in Python</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#installation-and-setup">Installation and Setup</a> •
  <a href="#roadmap">Roadmap</a> •
</p>

## Key Features

* CRUD - Create, Read, Update, and Delete tasks, their descriptions, and their completion status.
* Quick Summary - Instantly see the number of incomplete tasks at a glance.
* Task Search - Search for a particular task in the system.
* User Login - Login for a personalised list of tasks.
* User Isolation - Different users are not allowed to see each other's tasks.
* Database - Uses a remote postgres connection to allow for quick setup process.


## Roadmap

- [x] Implement User Login
- [x] Connect to Postgres database
- [ ] Deploy to production

## Installation and Setup
You need to have [Python](https://www.python.org/downloads/) installed on your machine to get the site running.

You also need to have a working internet connection for the database connection.
```bash
# Clone this repository into 
$ git clone https://github.com/Covenant224/Django-ToDo-App.git 

# Go into the repository
$ cd Django-ToDo-App

# Create virtual environment
$ python3 -m venv env

#Activate the environment(Linux and Mac)
$ source env/bin/activate

#Activate the environment(Windows)
$ env/scripts/activatesource env/bin/activate

#Install the requirements
$ pip install -r requirements.txt

#Run the migrations
$ python3 manage.py migrate

#Run the server
$ python3 manage.py runserver
```
That's it! All you have to do is open up your browser and go to "localhost:8000" to see the website ☻




