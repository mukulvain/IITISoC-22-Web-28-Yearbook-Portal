# IITISoC-22-Web-28-Yearbook-Portal
Mentor-
    Mukul Jain

Memebers - 
    A. Tarun Balaji-210002001  
    Sarthak Nandre 210002067  
    Neha Jadhav 210002054  
    Sana Presswala 210001062  

To run the website locally, follow the following steps -

    1. Clone the repository from github link.
    2. Open the repository in VS Code.
    3. Open new terminal and type 'cd yearbook' and hit enter.
    4. Now, type 'python manage.py runserver' and you can now see the website on local server.

Backend Features -
    1. Students can create profiles by registering. It only accepts valid iiti email id and email verification is required for logging in.
    2. After logging in, students can create their profile by filling the form on the next page.
    3. Students can also edit their details from their profile page.
    4. Students can view the yearbook by choosing the year and the branch.
    5. Students can view profiles of other students and also comment on them.
    6. Comments will be visible to other viewers only if the student approves it.
    7. Students can also see number of pending comments on their profile page.    
    8. Admins can create student profiles. When they do, the login details(username & password) are mailed to the student mail.
    9. Admins can also approve, decline or delete comments on any student.
    10. External Viewers can view the yearbooks and can read the approve comments but cannot comment.
    11. There is also a search option where search results show up based on name.


Footer - 

    You can create 2 users(will require valid emails) and test all the functionalities of the website. We have already created 2 example students(login details mentioned below).

    Admin login details -
        username - 'sarthak'
        password - 'sar'

    Example Students Login Details -
        username - 'student1'
        password - 'example

        username - 'student2'
        password - 'example'

*The backend is not completely integrated with the frontend*