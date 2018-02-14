# GWLocationAPI
An Awesome Python and Flask RESTful API Sample/Bootstrap Project with a Touch of OOP and MVC, Unit Testing, Persistence via SQLAlchemy, Security and Authentication, Mashups and some other cool topics in one single package.

---

## Work in Progress
_This is a work in progress..._

---


## Setup

_Instructions in progress...._

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

## Live Sample
https://gw-location-api.herokuapp.com

---

## License

Copyright ©2018 – Roberth Hansson-Tornéus ([R-H-T](https://github.com/R-H-T))
