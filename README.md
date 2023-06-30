# Flavoured Adventures

Flavoured Adventures is an online community where people can gather and share their recipes with each other from around the globe. The site allows user to browse existing recipes as well as the option to register and login in order to upload their own recipes or leave comments on other peoples recipes.

![Responsiveness](/static/images/Responsiveness.JPG)

# User Experience Design


## The Strategy Plane
---

### Site Goals
The site is aimed to be used as a tool for people from all around the world to share their creations from the kitchen be it old or new. It is a place where people can go and browse the existing recipes for inspiration and new experiences. It is a place where people can share their thought and encouragements with other user. It is place for fun tasty adventures.

### Agile Planning
The development of a recipe sharing website requires an organized and efficient approach. Agile methodology provides a flexible and iterative framework that promotes collaboration, adaptability, and continuous improvement. Here is an overview of the Agile plan for creating this recipe sharing website.

The first sprint, "Project Setup," focuses on establishing the project foundation. This includes setting up the repository and version control system, defining project goals and user stories, and creating a basic Django project structure. User registration and authentication functionality are implemented to ensure a secure and personalized experience. Database models for recipes and user profiles are developed, and initial templates are created.

In the second sprint, "Recipe Browsing and Searching," the focus shifts to enhancing the user's ability to discover and explore recipes. Recipe listing functionality is implemented, allowing users to browse recipes based on cuisines. The search functionality is developed, enabling users to find recipes through keywords and ingredients. A detailed recipe view is created, providing users with comprehensive information, including ingredients, methodology and descriptions. Pagination is added to the recipe listing to enhance user experience, enabling them to navigate through numerous recipes efficiently. 

The third sprint, "Recipe Management," allows user to be created and registered, which empowers registered users to contribute to the website by creating and editing their own recipes. The implementation of image upload functionality enhances the visual appeal of recipes. Validation and error handling mechanisms are put in place to ensure accurate and reliable recipe creation and editing. Additionally, a feedback functionality is incorporated, allowing users to provide their thoughts and experiences.

In the fourth sprint, "User Experience Enhancements," the focus shifts towards improving the overall user interface and experience. The website's design is refined to be visually appealing and user-friendly. Search functionality is enhanced with filtering options to facilitate quicker and more accurate recipe discovery.

The final sprint, "Deployment and Final Touches," involves the deployment of the website on Heroku. The code is modified to work on all screen sizes through media quiries. Extensive testing and bug fixing are conducted to ensure a stable and error-free experience.

#### Epics & User Stories
This project consited of 5 main Epics

Link to [user stories](https://github.com/users/Lukasrid/projects/3/views/1)

1. Project Setup
    - As a developer I need to develop a basic structure and layout so that i can easily navigate and edit the website
    - As a developer I need to create templates for each of the different pages of the website so that I can implement different functionality
    - As a developer i need to create a navigation bar so that other users can navigate the website
    - As a developer I need to create models so that I know what information is going to be displayed and can be edited
    - As a developer I need to connect the website to a database so that all the information thats input into the website can be stored somewhere

2. Recipe Browsing and Searching
    - As a user I can browse different cuisines so that it is easier to navigate
    - As a user I can browse through recipes with brief description so that I can get a quick overview of whats available
    - As a user I can search for recipes so that its easy to find specific recipes
    - As a user I can select a specific recipe and get all the information so that I can easily make it myself

3. Recipe Management
    - As a user I can see a picturre of the dish so that I can be furthured inspired to create it
    - As a user I can register/login so that I can keep track of who's recipie is whos
    - As a user I can add a recipe so that I and everyone can see it
    - As a use I can edit and delete recipes that i have posted so that I am in control of my posts
    - As a user I can see peoples individual profile pages so that view their activity on the website
    - As a user I can comment on recipes so that I can provide feedback to the people the community
    - As a user I can delete my comment so that i can control what i write

4. User Experience Enhancements
    - As a developer I want the site to be visually pleasing so that people will want to return
    - As a user I can get result for searches with partial/incomplete words so that it makes searching easier

5. Deployment and Final Touches
    - As a developer I need the website to be available to the public so that people can use it
    - As a user I can use the website on all my electronic devices so that I can access it anywhere I am
    - As a user I am provided with a stable and bug free environment so that I can browse through the website with ease


## The Scope Plane
- Responsive design - Site should function on all standard modern devices 
- CRUD functionality should be available to perform of recipes and comments
- Access to CRUD should only be available to registered  users
- Homepage should have an overview of recent activity
- All recipes should be able to be filtered by cuisine
- Profile pages should only have the users activity
## The Structure Plane
---
### Features
#### **All Pages**
- *Favicon*
    
    A favicon of the home logo was added so that the tab will always show what website you are on.

    ![Favicon](/static/images/Favicon%20Snip.JPG)
- *Navigation Bar*

    The navigation bar is located at the top of every page on the websit. It is used to help navigate the websitefrom any page. 

    ![Navigation Bar](/static/images/Navbar.JPG)

    - Logo/Header -> Visual representations of the website and also works as a links back to homepage.
    - Login/Logout -> A button located in the top right hand corner that allows user to navigate to the login page or log out of their current account. Text underneath the button tells user if they are not logged in or who they are logged in as.
    - Create Recipe -> The Create Recipe text is a link to the page where users can create their own recipes. 
    - Search Bar -> The search bar located under the logo is where users can search for recipie names, cuisines, ingredients or descriptions. This search bar is activated when the eneter button is pressed on the keyboard.

#### **Homepage**
- *Browse Cuisines*

    On the homepage a Browse Cuisine list can be found which enables user to click on any of the available cuisines and be redirected to a page where only events and recipes related to that cuisine can be found.

    ![Browse Cuisines](/static/images/Browse%20Cuisines.JPG)

- *Main Feed*

    In the middle of the homepage a feed of the most recent recipes will come up in order of the creation or edited timestamp.

    ![Main Feed](/static/images/Main%20feed.JPG)

    - A recipe counter in the top right shows how many recipes are avilable.
    - Each recipe shown gives a cuisine, dish name, author name, description and an optional image.
    - If the user viewing the recipe is also the author an Edit/Delete option will show up on the recipe.
    - The cuisine, dish name, edit/delete and author name are all links that can be clicked and will direct the user to the appropriate page.

- *Recent Activity Feed*

    The Recent Activity feed can be found on the right hand side of the homepage that shows the most recent comments made on recipes.

    ![Recent Activity Feed](/static/images/Activity%20feed.JPG)

    - Only shows comments (for now).
    - A user can see who, when and on what was commented on as well as the actual comment.
    - A user viewing their own comment will be presented with a Delete option that removes the users comment.

#### **Cuisine Page**

    Same as Homepage but the 'main feed' and 'recent activity feed' only show activity related to that cuisine.

#### **Profile Page**

    Same as Homepage but the 'main feed' and 'recent activity feed' only show activity related to the user. Their name is also printed out at the top of the 'main feed'

![Profile Page](/static/images/Profile.JPG)



#### **Create Recipe Page**

![Create Recipe](/static/images/Create%20Recipe.JPG)

- *Dish*

    The user can enter a name for the recipe.

- *Cuisine*

    The user can select a cuisine the dish belongs to from a dropdown menu. The user is unable to create their own unique cuisines.

- *Description*

    The user can write a breif description of the recipe.

- *Ingredients*

    The user can write down a list of ingredients for the recipe.

- *Method*

    The user can write down instructions on how to prepare the recipe.

- *Image*

    The user can choose to include an image of the completed dish. (Optional)

- *Submit*

    The user then can click submit to send off the information to be stored in a PostgreSQL database to then be presented on the website. 

#### **Delete Page**
    When a a user tries to delete a recipe that they have created, they are redirected to the delete page where they are asked if they are sure about their choice. They then have the option to cancel by pressing 'Go Back' or to delete it by pressing 'Confirm'.

![Delete Page](/static/images/Delete%20page.JPG)

#### **Login Page**

    The user can enter their email and password in the fields provided and then click sign in. If they however do not have an account they can press the 'Sign up!' button to be redirected to the Register Page.

![Login](/static/images/Login%20Box.JPG)
 

#### **Register Page**

    The user can fill in the required fields and click the 'Register' button to register themselves as a member. They are also prompted with a 'Login' button at the bottom incase they already have an account.

![Register Box](/static/images/Register%20Box.JPG)

### Future Features
- The registration form and the create recipe form will be stylized better (ran out of time to figure out how to do this).
- A footer is to be added.
- Users will be able to make a contact list of people they like.
- Users will be able to save and favourite recipes.
- Direct private messaging to other user will be implented.
- Emails will be added so that admin can contact users.
- Users will be able to request new cuisines at admin approval.
- Users will be able to search for other usersand not only recipes.
- Screen responsiveness will be improved.
- Activity feed will include more than just comments.
- Sweet and savoury catagories will be added for easier navigation.
- Users will be able to add a profile picture and customize their profile page more.
- A heading will be added at the top for when browing a specific cuisine.
- The number of recipies available from a user will be displayed at the top of a profile page like it does for the homepage and cuisine catagories.
- Users will be able to delete their account
- Users will be able to report or flag inappropriate content.


## The Surface Plane
### Design
#### Color Scheme
The main color schmemes used on the wbsite was a grey (#e0e0e0) for the background a kind of red (#800000) for highlighting important words and features. Rest of the text is black.
#### Typography
A font called "Cougette" was used as the main title and other key titles. The rest of the text id "Open Sans". The back up fonts are "Tahoma" and "Sans-Serif".
#### Imagery
The logo image was made using [freelogodesign.org](https://www.freelogodesign.org/).

All other images were taken from [Pexels](https://www.pexels.com/).

# Technologies

- HTML
  - The structure of the Website was developed using HTML as the main language.
- CSS
  - The Website was styled using custom CSS in an external file.
- JavaScript
  - JavaScript was used to insert icons.
- Python
  - Python was the main programming language used for the application using the Django Framework.
- PostgreSQL
    - The database where all data is stored that is put into the website.
- Cloudinary
    - Where all the images that get uploaded are stored
- Visual Studio Code
  - The website was developed using Visual Studio Code IDE
- GitHub
  - Source code is hosted on GitHub
- Git
  - Used to commit and push code during the development of the Website
- Font Awesome
  - This was used for icons throughout the site
- Favicon.io
  - favicon files were created at https://favicon.io/favicon-converter/

### External Python Modules
- asgiref==3.7.2
- cloudinary==1.33.0
- dj-database-url==0.5.0
- dj3-cloudinary-storage==0.0.6
- Django==3.2.3
- gunicorn==20.1.0
- Pillow==9.5.0
- psycopg2==2.9.6
- pytz==2023.3
- sqlparse==0.4.4
- urllib3==1.26.16
- whitenoise==6.5.0


# Testing
## Functionality Testing
The website has been thoroughly tested to see if it work, these include:

- All processed information gets stored in the linked up PostgreSQL database.
- All uploaded images get stored and viewd via Cloudinary.
- All links are working and take you to the right destination.
- All no information can be submitted without the right content and the required fields filled in.
- Non-registered users do not have access to features.
- Registered users do have access to features.
- Activity shows up in the correct order of when created/edited on all pages.
- Only relavant information shows up when viewing specific cuisines or profile pages.

## Validator Testing
### HTML Validator
The website was run through [W# HTML Validator](https://validator.w3.org/)

![HTML Validator](/static/images/HTML%20checker.JPG)

### Lighthouse
The lighthouse report showed decent results with areas of improvement in SEO and Best Practices.

![Lighthouse results](/static/images/lighthouse%20results.JPG)


# Development
### Version Control

The site was created using the Visual Studio Code editor and pushed to github to the remote repository ‘recipe-tracker’.

The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.

```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.

```git push``` - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (This should already exist with add on of postgres)
  - EMAIL_HOST_USER: (email address)
  - EMAIL_HOST_PASS: (email app password)
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy

The app should now be deployed.

The live link can be found here: [Live Site](https://sizzle-and-steak.onrender.com/)

### Run Locally

Navigate to the GitHub Repository you want to clone to use locally:

- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal

The project will now have been cloned on your local machine for use.

### Fork Project

Most commonly, forks are used to either propose changes to someone else's project or to use someone else's project as a starting point for your own idea.

- Navigate to the GitHub Repository you want to fork.

- On the top right of the page under the header, click the fork button.

- This will create a duplicate of the full project in your GitHub Repository.


# Credits

 ## Content

 ## Acknoledgements
