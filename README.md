# SE_Project   
Repository for the SE project   
   
## Description    
Django web server project which provides interface through ORM to a database (can be switched from a SQLlite file to a Postgres db) and a RESTfull API with POST and GET operations.    
  
### How to install:  
Go to the implementation_approach1 directory and create a virtual environment:  

`python3 -m venv env`  

Add the settings module to the env/activate:

`export DJANGO_SETTINGS_MODULE="se.settings.base"`

Run the migration modules (this means structuring the database with the models specified with the ORM):     

`python3 src/manage.py migrate`    

Run the web server on the desired IP (local or loopback address) and port:  
`python3 src/manage.py runserver 127.0.0.1:8000`

### Available endpoints

### GET
```
*/api/v1/languages  
*/api/v1/subjects  
*/api/v1/faculties  
*/api/v1/departments  
*/api/v1/professors  
*/api/v1/teaching_hours  
```
 
Example:  
`127.0.0.1:8000/api/api/v1/faculties`   


### POST 
```
*/api/v1/add_language  
*/api/v1/add_subject  
*/api/v1/add_facultie  
*/api/v1/add_department  
*/api/v1/add_professor  
*/api/v1/add_teaching_hour  
```

Example:  
url:  
`127.0.0.1:8000/api/api/v1/add_language `   
  
body: 
``` 
{
"name": "Romanian",
"abrv": "RO"
}
```