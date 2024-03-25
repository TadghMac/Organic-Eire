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


**User Stories**

**User**

1. As a new visitor to the website, I want to be able to easily register for an account so that I can access exclusive content and features.


**Registered User**

1.As a registered user, I want the website to be visually appealing and easy to navigate on both desktop and mobile devices.

2.As a registered user interested in specific topics, I want to be able to search for articles by keyword or category.

3.As a registered user, I want to be able to read detailed articles about various aspects of organic farming, including techniques, benefits, challenges, and success stories.

4.As a registered user interested in engaging with the community, I want to be able to comment on articles and participate in discussions with other users.

5.As a registered user, I want to be able to log in to my account securely using my email and password.

6.As a registered user, I want the website to remember my login credentials for convenience.

7.As a registered user, I want to be able to update my profile information, including my name, email address, and profile picture.

8.As a registered user, I want to be able to view a personalized dashboard that displays the latest organic farming articles, news, and updates.

9. As a registered user, I want to be able to bookmark articles that I find particularly interesting or useful .

10. As a registered user, I want to be able to share articles to my other social media accounts 

**Admin**
1.As an administrator of the website, I want to be able to manage user accounts, including approving registrations, resetting passwords, and banning users if necessary.

2.As an administrator, I want to be able to create, edit, and delete articles to keep the content of the website up to date and relevant.

3.As an administrator, I want to be able to track website analytics to understand user behavior and improve the website's performance and user experience. 

ERD(original concept design) 

In the initial planning stage the user would of been able to create a profile page. Due to time constriants I removed this feature.
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/3469a47a-a3d5-4601-b988-520a87a15727)

My Custom Model
![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/8a52df81-77db-47f9-92fd-679e2ffe84ab)

**Users Permissions**
A visiting user can read articles , can access all links but can not comment 

**registered users**
Can commment on articles ,can also post articles once they have been verified by the admin . 

![image](https://github.com/TadghMac/Organic-Eire/assets/152603370/da63b1d6-4c0e-4eeb-af8d-aeca6f703e1c)


Testing


**Signed Up In/Out Test**
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


