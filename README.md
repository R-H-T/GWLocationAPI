# GWLocationAPI
An Awesome Python and Flask RESTful API Sample/Bootstrap Project with a Touch of OOP and MVC, Unit Testing, Persistence via SQLAlchemy, Security and Authentication, Mashups and some other cool topics in one single package.

---

## Work in Progress
_This is a work in progress..._

---


## Setup

**Quick steps to get started:**
* Clone this project from the terminal/command prompt: `git clone https://github.com/R-H-T/GWLocationAPI.git`
* Run `virtualenv venv` (Learn more about setting up your own _Virtual Environment_ - read my instructions below: _How to Setup a Virtual Environment?_)
* Activate the virtual environment `source venv/bin/activate`(Mac/Linux) or `./venv/Scripts/activate.bat`(_Windows_)
* Install the predefined requirements `pip install -r requirements.txt`
* Run the app `python app.py`
* Open up http://localhost:5000/ (Follow all the other instructions inside this document to see how to give it a test run).
* For a live preview see: https://gw-location-api.herokuapp.com and test making different calls.

### How to Setup a Virtual Environment?
#### Install `virtualenv`from your terminal/command prompt

Mac/Linux/Windows:
`pip install virtualenv`
or
`pip3.6 install virtualenv`

#### Initialize `virtualenv`

This will initialize `virtualenv` within your project's directory.

Mac/Linux/Windows:
`virtualenv venv`
or
`virtualenv venv --python=3.6`

#### To Activate `virtualenv`
This will activate your virtual environment.
All `pip install`s inside your project directory
will only affect your virtual environment and not your system.

Mac & Linux:
`source venv/bin/activate`

Windows:
`./venv/Scripts/activate.bat`

### How do I deactivate my project's virtual environment?
#### To Stop/Deactivate `virtualenv`
This will stop your virtual environment session.

While you're inside your project's directory, type the following (Mac/Linux/Windows):
`deactivate`

---

## Testing through `cURL`

### GET INDEX
`curl "https://gw-location-api.herokuapp.com"`

### FIND LOCATION
`curl "https://gw-location-api.herokuapp.com/find/bangkok"`

###  GET ALL LOCATIONS
`curl "https://gw-location-api.herokuapp.com/locations/"`

###  LOCATION BY ID
`curl "https://gw-location-api.herokuapp.com/locations/1"`

###  POST LOCATION (🔐)
`curl -i -X "POST" "https://gw-location-api.herokuapp.com/locations/"`

###  UPDATE LOCATION (🔐)
`curl -i -X "PUT" "https://gw-location-api.herokuapp.com/locations/1"`

###  DELETE LOCATION (🔐)
`curl -i -X "DELETE" "https://gw-location-api.herokuapp.com/locations/1"`

🔐 = Requires authentication (_Create a user inside the generated db-file until added in future versions_).


---

## Running a Unit Test

Run `python tests/model/test_user.py`

---


## Live Sample
https://gw-location-api.herokuapp.com

---

## License

Copyright ©2018 – Roberth Hansson-Tornéus ([R-H-T](https://github.com/R-H-T))
