### job_portal file is Django Project 
### jobapp file is django app


### Django REST API Setup
This repository contains a Django project with a RESTful API using Django REST Framework.

#### Prerequisites
- Installed through the requirements.txt file 
### Setup Instructions
#### Create a Virtual Environment:
- virtualenv environmentname
#### Activate Virtual Environment:
- cd environmentname/Scripts
- activate
#### Install Dependencies:
- using the requirements.txt file 
#### Set up a new project 
- django-admin startproject job_portal
- cd job_portal
- django-admin startapp jobapp
#### Setup DataBase for MySQl Database Instead of SQLite 
- in the settings.py database settings
- change the name with your mysql schemas name 
- change the user with your user name 
- change the password with your password 
#### Database migration
- python manage.py makemigrations
- python manage.py migrate
#### how to run a api endpoint:
- first we need to make sure that we migrated the models to database
- then we need to start the server using "python manage.py runserver" command.
- then we need to open another cmd prompt and open virtual environment and activate then open the project folder and provide curl commands or using the Thunder Client .
- make sure Your server is runnig in another cmd prompt
### Testing or Using the API endpoints.
- we can test API endpoints using curl commands or Thunder Client Requests.
#### Create a JobSeeker:
#### using Thunder Client:
- Select the Http Request POST http://127.0.0.1:8000/api/jobseekers/
- in the body write the data {"name":"Your-name" , "mobile":"9999999999"}
- then click on send 
#### using curl:
- curl -X POST http://127.0.0.1:8000/api/jobseekers/ -d "name=your-name&mobile=9999999999"
#### About this API endpoint:
- here this endpoint is used to create a jobseeker by providing the jobseeker details.
#### List all Job Seeker details:
#### using Thunder Client:
- Select the Http Request GET http://127.0.0.1:8000/api/jobseekers/
- then click on send 
#### using curl:
- curl -X GET http://127.0.0.1:8000/api/jobseekers/ 
#### About this API endpoint:
- here this endpoint is used to get the details of jobseekers.
#### Retrieve a specific jobseeker details:
#### using Thunder Client:
- Select the Http Request GET http://127.0.0.1:8000/api/jobseekers/{id}/
- then click on send 
#### using curl:
- curl -X GET http://127.0.0.1:8000/api/jobseekers/{id}/
#### About this API endpoint:
- here this endpoint is used to get the details of jobseeker with id which was mentioned in the command.
### Update a Jobseeker details:
#### PUT method:
#### using Thunder Client:
- Select the Http Request PUT http://127.0.0.1:8000/api/jobseekers/{id}/
- in the body write the data {"name":"Your-updated-name" , "mobile":"88888888888"}
- then click on send 
#### using curl:
#### PUT method:
- curl -X PUT http://127.0.0.1:8000/api/jobseekers/{id}/ -d "name=updated-name&mobile=Updated mobile Number"
#### PATCH method:
#### using Thunder Client:
- Select the Http Request PATCH http://127.0.0.1:8000/api/jobseekers/{id}/
- in the body write the data {"name":"Your-updated-name"}
- then click on send 
#### using curl:
- curl -X PATCH http://127.0.0.1:8000/api/jobseekers/{id}/ -d "name=updated-name"
#### About this API endpoint:
- here this endpoint we have two commands with different http methods (PUT,PATCH).As we have a id in the model the PUT method used to update all the data . The PATCH method is used to update the jobseeker details except id. here PUT handles updates by replacing the entire entity, so it creates a new entity. but where the PATCH handles by only updating the given fields.
#### Delete a jobseeker:
- using curl:
- curl -X DELETE http://127.0.0.1:8000/api/jobseekers/{id}/
#### using THunder Client :
- Select the Http Request DELETE http://127.0.0.1:8000/api/jobseekers/{id}/
- then click on send 
#### About this API endpoint:
- here this endpoint is used to delete the jobseekers with given id.

#### For the Job API TEsting 

#### Create a Job:
#### using Thunder Client:
- Select the Http Request POST http://127.0.0.1:8000/api/job/
- in the body write the data {"job_title":"Job Title" , "job_description":"description"}
- then click on send 
#### using curl:
- curl -X POST http://127.0.0.1:8000/api/jobs/ -d "job_title=your-job&job_description=description"
#### About this API endpoint:
- here this endpoint is used to create a job by providing the jobs details.
#### List all Job details:
#### using Thunder Client:
- Select the Http Request GET http://127.0.0.1:8000/api/jobs/
- then click on send 
#### using curl:
- curl -X GET http://127.0.0.1:8000/api/jobs/ 
#### About this API endpoint:
- here this endpoint is used to get the details of jobs.
#### Retrieve a specific jobs details:
#### using Thunder Client:
- Select the Http Request GET http://127.0.0.1:8000/api/jobs/{id}/
- then click on send 
#### using curl:
- curl -X GET http://127.0.0.1:8000/api/jobs/{id}/
#### About this API endpoint:
- here this endpoint is used to get the details of jobs with id which was mentioned in the command.
### Update a Jobs details:
#### PUT method:
#### using Thunder Client:
- Select the Http Request PUT http://127.0.0.1:8000/api/jobs/{id}/
- in the body write the data {"job_title":"Your-updated-title" , "job_description":"updated description"}
- then click on send 
#### using curl:
#### PUT method:
- curl -X PUT http://127.0.0.1:8000/api/jobs/{id}/ -d "job_title=updated-title&job_description=Updated description"
#### PATCH method:
#### using Thunder Client:
- Select the Http Request PATCH http://127.0.0.1:8000/api/jobs/{id}/
- in the body write the data {"job_title":"Your-updated-title"}
- then click on send 
#### using curl:
- curl -X PATCH http://127.0.0.1:8000/api/jobs/{id}/ -d "job_title=updated-title"
#### About this API endpoint:
- here this endpoint we have two commands with different http methods (PUT,PATCH).As we have a id in the model the PUT method used to update all the data . The PATCH method is used to update the jobs details except id. here PUT handles updates by replacing the entire entity, so it creates a new entity. but where the PATCH handles by only updating the given fields.
#### Delete a jobs:
- using curl:
- curl -X DELETE http://127.0.0.1:8000/api/jobs/{id}/
#### using THunder Client :
- Select the Http Request DELETE http://127.0.0.1:8000/api/jobs/{id}/
- then click on send 
#### About this API endpoint:
- here this endpoint is used to delete the jobs with given id.

#### Perform Operations on AdminUser Model 

#### Create a AdminUser:
#### using Thunder Client:
- Select the Http Request POST http://127.0.0.1:8000/api/adminusers/
- in the body write the data {"name":"Your-name" , "email":"youremail@gmail.com"}
- then click on send 
#### using curl:
- curl -X POST http://127.0.0.1:8000/api/adminusers/ -d "name=your-name&email=youremail@gmail.com"
#### About this API endpoint:
- here this endpoint is used to create a adminusers by providing the adminusers details.
#### List all adminusers details:
#### using Thunder Client:
- Select the Http Request GET http://127.0.0.1:8000/api/adminusers/
- then click on send 
#### using curl:
- curl -X GET http://127.0.0.1:8000/api/adminusers/ 
#### About this API endpoint:
- here this endpoint is used to get the details of adminusers.
#### Retrieve a specific adminusers details:
#### using Thunder Client:
- Select the Http Request GET http://127.0.0.1:8000/api/adminusers/{id}/
- then click on send 
#### using curl:
- curl -X GET http://127.0.0.1:8000/api/adminusers/{id}/
#### About this API endpoint:
- here this endpoint is used to get the details of adminusers with id which was mentioned in the command.
### Update a Jobseeker details:
#### PUT method:
#### using Thunder Client:
- Select the Http Request PUT http://127.0.0.1:8000/api/adminusers/{id}/
- in the body write the data {"name":"Your-updated-name" , "email":"updatedemail@gmail.com"}
- then click on send 
#### using curl:
#### PUT method:
- curl -X PUT http://127.0.0.1:8000/api/adminusers/{id}/ -d "name=updated-name&email=updatedemail@gmail.com"
#### PATCH method:
#### using Thunder Client:
- Select the Http Request PATCH http://127.0.0.1:8000/api/adminusers/{id}/
- in the body write the data {"name":"Your-updated-name"}
- then click on send 
#### using curl:
- curl -X PATCH http://127.0.0.1:8000/api/adminusers/{id}/ -d "name=updated-name"
#### About this API endpoint:
- here this endpoint we have two commands with different http methods (PUT,PATCH).As we have a id in the model the PUT method used to update all the data . The PATCH method is used to update the adminusers details except id. here PUT handles updates by replacing the entire entity, so it creates a new entity. but where the PATCH handles by only updating the given fields.
#### Delete a adminusers:
- using curl:
- curl -X DELETE http://127.0.0.1:8000/api/adminusers/{id}/
#### using THunder Client :
- Select the Http Request DELETE http://127.0.0.1:8000/api/adminusers/{id}/
- then click on send 
#### About this API endpoint:
- here this endpoint is used to delete the adminusers with given id.

#### Additionally 
#### See the Data from APILog Models 

- we can only see the apilog models data that save through the custom middleware that i have created 
#### using Thunder Client:
- Select the Http Request GET http://127.0.0.1:8000/api/apilogs/
- then click on send 
#### using curl:
- curl -X GET http://127.0.0.1:8000/api/apilogs/ 
