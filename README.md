# LINC Programming Round

## Installing the dependencies [Flask REST JSONAPI](http://flask-rest-jsonapi.readthedocs.io/)

> This app has been tested on Python 3.5.2, hence docs are as per same version.

```
virtualenv -p python3 venv

source venv/bin/activate

pip install -r requirements.txt

```

## Database Setup (POSTGRESQL)

```
sudo -u postgres psql

```

```sql
CREATE USER john WITH PASSWORD 'start';
CREATE DATABASE linc_flask WITH OWNER john;
```

## Running the app

```
cp env.example .env

python server.py

```

## APIs 

1. UserList (GET / POST) : `/users`
2. UserDetail (GET / PATCH / DELETE) : `/users/<int:id>`, `/experience/<int:experience_id>/user`
3. UserRelationship (GET / DELETE) : `/users/<int:id>/relationships/experiences`

4. ExperienceList (GET / POST) : `/experiences`, `/users/<int:id>/experiences`
5. ExperienceDetail (GET / PATCH / DELETE) : `/experiences/<int:id>`
6. ExperienceRelationship (GET / DELETE) : `/experiences/<int:id>/relationships/user`


## Request Body of UserList (POST) : 

```
{
  "data": {
    "attributes": {
      "city": "Mumbai",
       "name": "Anand",
       "date_of_birth": "1996-10-19",
       "primary_email": "anand@example.com",
       "secondary_email": null,
       "primary_phone": 123456780,
       "secondary_phone": 12345678,
       "full_address": "234 ABC Nagar, Navi Mumbai"
   },
    "type": "user"
  }
}
```

## Request Body of ExperienceList (POST) : 

```
{
  "data": {
    "attributes": {
      "city": "New Delhi",
       "company": "Infosys",
       "start_date": "2015-02-01",
       "end_date": "2018-01-30",
       "type": "Full-Time",
       "designation": "System Engineer",
       "role_description": "Worked on Software Development"
    },
    "type": "experience"
  }
}
```
