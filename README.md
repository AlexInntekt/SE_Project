# SE_Project   
Repository for the SE project   
   

## Description approach 1   
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


## Description approach 2

We searched different chatbots aplications for websites. We tried ChatComposer https://www.chatcompose.com/website.html but it has many problems and no documentation. After ChatComposer we tried InstaBot https://instabot.io/ . It has less problems than ChatComposer, but again no documentation. After another try we found ChatBot https://www.chatbot.com/ which seems to fit us best.    

ChatBot is a powerful tool with lots of options and it has a very intuitive way of doing this.    

We start developing using this tool and the final product looks like this: The bot welcomes you with the message:   

"Hello, welcome to FILS ChatBot! 👋 How can I help you?" The user can choose from 4 answers: "Course", "How to apply?", "Open days", "Contact us".     
"How to apply" offers info about registering in the exam fro Bachelor degreee and Master degree.     
"Course" offers info about the curriculum for Undergraduate and Masters. 
"Open Days" offers info about Schedule and Location    
"Contact us" offers info about calling and leaving a message. For Leaving a message the bot will ask for name and email.    
