#My "personal Cloud API"

A backend REST API built with FastAPI and PostgreSQL, containerised using Docker. 
This project was built as a learning exercise to learn architecture, FastAPI, database integration and the development pipeline. 

Tech Stack - 

FastAPI
PostgreSQL
SQLAlchemy
Docker and Docker Compose
Python

Features - 

Basic REST API with CRUD operations
PostgreSQL database integration
SQLAlchemy ORM models
Dockerised development environment (this took a minute)
-next step will be to cleanup the project structure it's a bit script-y at the moment. 

if you want to clone the repository to test it's : 
git clone git@github.comdevslouchy/pcloud-api.git
cd pcloud-api.git

run this in docker and you will see the API at http://localhost:8000


API Endpoints : 

Health Check : 
GET /health

Items : 
GET /items
POST /items
GET /items/{item_id}
DELETE /items{item_id}


This was all completely new to me. I've done some basic scripting, this is very much a 1st draft. 

Next Steps : 
Cleanup the backend, I know I've made it a bit "all in one" rather than splitting the code into more sections. 
Add authentication
Improve error handling (right now, the only thing it deals with is deleting something that doesn't exist)
Add testing

License : MIT... I mean nobody's going to want this for anything real. 
