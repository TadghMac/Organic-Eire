![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/f4113577-eee5-4db8-9919-904d704a760f)


**Organic Éire**

Overview

Welcome to Organic Éire, a platform dedicated to promoting organic farming, sustainability, and environmental conservation. This app serves as a hub for farmers, enthusiasts, and experts to share insights, ideas, and experiences related to organic practices and sustainable living. The app is composed of of 3 pages . The articles page, a page for the different farming organisations and a about page which has instructions on how to get a articles published.

Key Features

Community Engagement: Join our community to connect with like-minded individuals passionate about organic farming and environmental conservation.

Knowledge Sharing: Share your expertise, insights, and experiences with others to foster learning and collaboration.

Article Publication: Registered users can publish articles on various topics related to organic farming, sustainability, and environmental conservation once the admin has verified their email address.

Resource Hub: Access useful links, resources, and information to support your journey towards organic farming and sustainable living.

Social Integration: Connect with us on social media platforms to stay updated on the latest news, events, and discussions.

![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/bfe66590-f217-495b-9613-68888a64840c)


Design Ideas for UX

 Organic  Éire is designed with simplicity and ease of use in mind, catering to users with varying levels of computer literacy. I believe in providing a straightforward and intuitive interface that allows users to navigate the application effortlessly.


Key Design Principles:
Minimalistic Interface: I adopt a minimalistic design approach, keeping the user interface clean and clutter-free. This helps reduce cognitive load and makes it easier for users to focus on the essential features of the application.


Intuitive Navigation: Navigation within the application is designed to be intuitive and logical. Users should be able to find the information they need quickly and without confusion.


Clear Communication: I prioritize clear and concise communication throughout the application. This includes using plain language, providing helpful tooltips and instructions, and avoiding technical jargon whenever possible.


Responsive Design: Our application is built with responsive design principles, ensuring that it functions seamlessly across devices of all sizes. Whether users access the application on a desktop computer, tablet, or smartphone, they can expect a consistent and optimal experience.



Initial Design and Planning

In the inital planning , the app was going to have a classifieds section with CRUD funcionality but I chose not to impliment this in this version.
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/5dd1d831-8de0-4de5-8549-ee922bac738c)


![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/8b6087a7-1732-4997-8dd7-9e593602df53)


Concept design design for community page 
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/a05efd9d-07fd-43b4-850f-beaa499ed0fa)



Links page concept
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/f84f1fa9-2b75-40c2-9a4e-cb92574cd0a4)

**Deployment**

The deployment stage of the website should follow the steps below:

 Create the Heroku app:

 Sign up / Log in to Heroku
 
 In Heroku Dashboard page select 'New' and then 'Create New App'
 
 Name a project - I decided on organic-eire (note : the app's name must be unique)
 
 Select EU as that was my region in the moment of creating the app
 
 Select "Create App"
 
 In the "Deploy" tab choose GitHub as the deployment method
 
 Connect your GitHub account/ find and connect your GitHub repository

 Set up enviroment variables

 In the Django app editor create env.py in the top level
 
 In env.py import os
 
 In env.py set up necessary enviroment variables:
 
 add a secret key using: os.environ['SECRET_KEY'] = 'your secret key'
 for the database variable the line should include os.environ['DATABASE_URL']= 'Paste the database link in here'
 
 In settings.py replace value of SECRET_KEY variable with os.environ.get('SECRET_KEY')
 
 In settings.py change the value of DATABASES variable to 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
 
 In Django app's settings.py on top of the file add:


from pathlib import Path
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env


Navigate to the "Settings" tab in Heroku.

Open the "Config Vars" section and add DATABASE_URL as Key and the database link from app's env.py as Value

Add SECRET_KEY for the Key value and the secret key value from env.py as the Value

In the terminal migrate the models over to the new database connection

In settings.py add the STATIC files settings as follows:

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

Change the templates directory in settings.py to: TEMPLARES_DIR = os.path.join(BASE_DIR, 'templates')

In TEMPLATES variable change the 'DIRS' key to look like this: 'DIRS': [TEMPLARES_DIR],

Add Heroku to the ALLOWED_HOSTS list (the format will be your-app-name.herokuapp.com, you can copy it from the Domains section in Settings tab in your Heroku app)

If you haven't done that up to this point, then create in your Django app's code editor new top level folders: static and templates

Create a new file on the top level directory - Procfile, remembering to use a capital letter

the Procfile add following:
web: guincorn PROJECT_NAME.wsgi

In the terminal, add the changed files, commit and push to GitHub
Heroku deployment

In Heroku, navigate to the Deployment tab and deploy the branch manually

Heroku will display a build log- watch the build logs for any errors

Once the build process is completed Heroku displays a message and a link to the app to visit the live site

![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/37183fdf-7916-46b6-a429-0b9b5996430d)


**User Stories**

**User**

1. As a new visitor to the website, I want to be able to easily register for an account so that I can access exclusive content and features.(Done)


**Registered User**

1.As a registered user, I want the website to be visually appealing and easy to navigate on both desktop and mobile devices.(Done)

2.As a registered user interested in specific topics, I want to be able to search for articles by keyword or category(futrue feature)


3.As a registered user, I want to be able to read detailed articles about various aspects of organic farming, including techniques, benefits, challenges, and success stories.(Done)

4.As a registered user interested in engaging with the community, I want to be able to comment on articles and participate in discussions with other users.(Done)

5.As a registered user, I want to be able to log in to my account securely using my email and password.(Done)

6.As a registered user, I want the website to remember my login credentials for convenience.(varies on user device settings)

7.As a registered user, I want to be able to update my profile information, including my name, email address, and profile picture.(futrue feature)

8.As a registered user, I want to be able to view a personalized dashboard that displays the latest organic farming articles, news, and updates.(Done)

9. As a registered user, I want to be able to bookmark articles that I find particularly interesting or useful .(futrue feature)

10. As a registered user, I want to be able to share articles to my other social media accounts (futrue feature)

**Admin**
1.As an administrator of the website, I want to be able to manage user accounts, including approving registrations, resetting passwords, and banning users if necessary.(Done)

2.As an administrator, I want to be able to create, edit, and delete articles to keep the content of the website up to date and relevant.(Done)

3.As an administrator, I want to be able to track website analytics to understand user behavior and improve the website's performance and user experience. (Done)

ERD(original concept design) 

In the initial planning stage the user would of been able to create a profile page. Due to time constriants I removed this feature.
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/3469a47a-a3d5-4601-b988-520a87a15727)

My Custom Model
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/8a52df81-77db-47f9-92fd-679e2ffe84ab)

**Users Permissions**
A visiting user can read articles , can access all links but can not comment 
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/da63b1d6-4c0e-4eeb-af8d-aeca6f703e1c)



**registered users**
Can commment on articles ,can also post articles once they have been verified by the admin . 



**Testing**
Admin feature testing 

users cant log in to admin
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/65287d96-8871-4f6a-942e-f84c23212589)

A list of completetd actions proving CRUD functionality 

![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/6a490969-d6a1-489d-aa1a-646882210f5c)

Creating in my custom model
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/1f0ae21f-f527-4938-b974-a485524787d1)


Edit 

![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/3c8360b9-4caf-4434-90e5-8cda7c2b894a)


Delete 

![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/3cda1c60-321d-46f0-af49-8b155fe2b2c6)



**Articles ,Signed Up In/Out Test**
In the following I created a new user (Billy). 

![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/cbb07623-d6f1-4b31-aeb2-89f37a1a21a4)

![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/312bd00d-4c36-4e4b-8341-49a818972d1e)

Users can delete ,edit and successfuly post comments . However the comment counter doesnt change until the page has been refreshed.
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/a523c054-4215-4b7b-a9e2-856e48149da6)

comment count after a page reload
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/f01547f6-871c-4d35-a0db-6dec613ffd86)

Updating a comment
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/83d9b846-1567-40e5-8fe2-f9e27949ffc2)

comment updated succesfully
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/31eaa145-0124-40b2-843b-64fb6937da7c)

deleting a comment 

![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/ea01d148-8bd5-4d9b-b80e-b0c36bb87929)


comment successfully deleted
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/586c0e95-b4b5-45d8-8292-e913a9680364)

Links Page test 


All links are responsive, opens the link on a new window

![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/9ad1d466-b348-4e3d-8764-15ec4f103f17)


WAVE test:


NOTE:Error in the test , the links actually work  

![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/4d10ff9e-8d5e-42e9-b7b4-39084e8674e7)

Article and comment section

The Alerts here are for extra headings , In future versions this could be a option , the error is for low contrst in the comment counter
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/3ef04d50-70f8-49ba-af52-28c623c135e2)


Lighthouse test on articles page

![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/fc4ff515-6e1e-4f54-a1af-f1beb9dfb570)


Lighthouse test Links Page

![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/b7d96fda-aec7-46df-be12-daad7a7abe0f)

Lighthouse test Articles page

![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/8367a357-7d9c-481d-a456-5a69886f5b5f)

I changed to footer to green which then improved the score 

![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/5c8e6532-8e4c-447d-8241-d1b852ad4389)



"" BUGS/ERRORS ""
Having to reload the page to add to the comment count

CORS errror:
A CORS (Cross-Origin Resource Sharing) error occurs when a web application tries to make a request to a resource from a different origin (domain, protocol, or port) than the one that served the initial web page. This security feature is enforced by web browsers to prevent malicious websites from accessing sensitive data. . Originally I fixed this iusse in my local environment and it appreared to disapear . When testing close to the deadline I felt it safer submititng with errors rather then risk breaking a deployed version.
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/0150a4be-ed68-4e89-8a9a-fd1090cdaf59)


**Future features**
In future versions  Id like to impliment the following:
 -search bar: for users to serch for articles and other users more easily

-profile page: I think users would enjoy having theor own custom profile page where they can see their list of posts , similar to what you see on other social media sites

-classifieds section: A section for users to buy, sell , look for goods and services associates with organics.

-take the content box out of my custom model : This field is not necessery but when I removed it the model broke so I chose to leave it for this version

-CSS : I chose a basic color scheme and layouts, had I allocated more time for this I could have experimented with different color combinations to find the most harmonious palette for the page.

