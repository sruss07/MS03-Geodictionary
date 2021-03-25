# Table of Contents

> - [Overview](#overview)
> - [User Stories](#user-stories)
> - [UX](#ux)
> - [Features](#features)
> - [Technologies Used](#technologies-used)
> - [Resources for learning](#resources)
> - [Testing](#testing)
> - [Project barriers and solutions](#project-barriers-and-solutions)
> - [Code validity](#code-validity)
> - [Version Control](#version-control)
> - [Deployment](#deployment)
> - [Credits](#credits)
> - [Acknowledgments](#acknowledgments)
> - [Support](#support)

Site deployed on Heroku [HERE](https://XXXXX.herokuapp.com/)

**Please note: To open any links in this document in a new browser tab, please press `CTRL + Click`.**

## Overview

The aim of this project is to create and provide a comprehensive geology and earth sciences dictionary that provides a resource that is accessible and visually appealing to all experience levels from geology experts, to experienced amateurs, through to complete beginners. Interested users can register with the site, allowing them to add new terrms and definitions and edit their own entries. A search facility allows users to search existing terms and definitions

> [Back to Top](#table-of-contents) 

## User Stories

### New Users

- As a new user I want to be presented with a simple, enjoyable and easy to use site, that is also visually appealing
- As a new user I want to be able to navigate around the site with ease
- As a new user I want to be able to easily find the geological term I am looking for, via an alphabetical ordering system
- As a new user I would like the option to add to the dictionary of geological terms
- As a new user I want to have access to the geological terms/definitions that I have previously created and have the option to edit them
- As a new user I want to enjoy using the site enough to want to return

### Returning Users

- As a returning user I want all the requirements of a new user
- As a returning user I want to be able to see any new geological terms that have been added in a logical order

### Frequent Users

- As a frequent user I want all the requirements of a new and returning user
- As a frequent user, going forward I would like to be able to interact with other users on the site on a social level
- As a frequent user, going forward I would like to be able to see recommendations for geological themed merchandise, trips etc

### Admin Users

- As an admin I would like the ability to **log into an admin account**, so that I can curate and maintain the contents of the site
- As an admin user I would like the ability to track the activity of registered users so I can monitor the suitability of information being added to the dictionary
- As an admin I would like to be able to delete user accounts, so that I can maintain control of user accounts
- As an admin I would like to be able to update all terms and definitions so that I can ensure the site is kept relevant, factually correct and visually appealing for all users

## UX

This website project will target geology enthisiasts of all levels. The main focus is on providing a fluid and structured dictionary of as many geology and earth science terms and definitions as possible

### 1. Strategy

#### Project and User Goals

- Provide an easy to navigate dictionary for cataloguing geology and earth science terms and associated definitions

- Provide new user accounts to enable users to login and access the dictionary
- Provide an admin account to enable an admin to login and manage the site
- Design backend functionality focussed on defensive design

- Design frontend UX for:
  - Clean and intuitive navigation
  - Responsiveness for use on mobile phone and tablet devices

### 2. Scope

- Project utilises my current coding skill-set of HTML, CSS, JavaScript, Python, Flask and MongoDB
- Allow users to add new content
- Allow users to amend content which they added
- Allow users to search existing content
- Allow users to read existing content
- Allow Admin to create, Read, Update and Delete content

### 3. Structure

The overall structure is designed for ease of navigation to each section

- Top navigation menu containing Home, Login, Add Term and Profile links
- Side navigation menu on smaller screens containing the same links as the top navigation menu
- Once logged in users will see Profile and Logout links

### 4. Skeleton

- Navigation bar - menu with links pointing to each page
- Home Page - intro headline, alphabet menu and alphabetically sorted terms
- Register Page - form with fields to create new user and user password
- Login Page - form with fields for user and password
- Add Term Page - form with 'Add Term' and 'Add Definition' fields
- Edit Term Page - form allowing users to edit their own dictionary entries
- Profile Page - banner showing user name of currently logged in user

### 5. Surface

The overall UX is clean and consistent and offers the user a site which should be easy to navigate and a pleasure to use, encouraging users to return multiple times

#### Colours

The colour pallette was chosen to reflect colours which are typical within the matrix of geological features and rocks 

#### Typography

- "Barlow" font (with fall-back font of Sans-Serif) is used for heading and body content

#### Images

- I have chosen to only use a single image with this project. The image has been utilised as a background image for each page

#### Design Choices

- As the project developed, the look and layout began to deviate slightly away from my initial wireframe designs. The core design is still similar with extra links, pages etc added

> [Back to Top](#table-of-contents)

## Features

### Existing Features

- Designed with HTML5, CSS3, JavaScript, Python3, Flask, MongoDB and Materialize
- Responsive Materialize Bootstrap Navigation bar
- Home/Landing page with redirection links to Register page and Login page

### Features Left to Implement

- Integrate functionality to the Add Terms form to allow users to upload photographs when submitting new terms and definitions
- Add social channels to allow communication between users
- Add links to merchandise and trip websites

> [Back to Top](#table-of-contents) 

## Technologies Used

### 1. Languages

![Image](https://res.cloudinary.com/dpagr3dzw/image/upload/t_media_lib_thumb/v1616406417/logos/HTML5_Logo.jpg) [HTML5](https://en.wikipedia.org/wiki/HTML5)

![Image](https://res.cloudinary.com/dpagr3dzw/image/upload/t_media_lib_thumb/v1616406447/logos/CSS3_logo.png) [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)

![Image](https://res.cloudinary.com/dpagr3dzw/image/upload/t_media_lib_thumb/v1616406494/logos/javascript-logo.jpg) [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

![Image](https://res.cloudinary.com/dpagr3dzw/image/upload/t_media_lib_thumb/v1616406515/logos/Python-logo.png) [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### 2. Integration

![Image](https://res.cloudinary.com/dpagr3dzw/image/upload/t_media_lib_thumb/v1616406555/logos/materialize-logo.png) [Materialize](https://materializecss.com/) - by linking via [Materialize CDN](https://materializecss.com/getting-started.html) to HTML Doc

![Image](https://res.cloudinary.com/dpagr3dzw/image/upload/t_media_lib_thumb/v1616406583/logos/font_awesome_logo.png) [FontAwesome](https://fontawesome.com/) Icons for Social Media links

![Image](https://res.cloudinary.com/dpagr3dzw/image/upload/t_media_lib_thumb/v1616406609/logos/google-fonts-logo.jpg) [Google Fonts](https://fonts.google.com/) - Overall Typography import

![Image](https://res.cloudinary.com/dpagr3dzw/image/upload/t_media_lib_thumb/v1616406635/logos/jquery.logo.jpg) [jQuery](https://jquery.com/) - JavaScript library

![Image](https://res.cloudinary.com/dpagr3dzw/image/upload/t_media_lib_thumb/v1616408528/logos/Flask-logo-01.jpg) [Flask](https://flask.palletsprojects.com/en/1.1.x/) Micro web framework written in Python

![Image](https://res.cloudinary.com/dpagr3dzw/image/upload/t_media_lib_thumb/v1616406685/logos/mongodb-logo.png) [MongoDB](https://www.mongodb.com/) NoSQL database program, using JSON-like documents

### 3. Dependencies

- [Pymongo](https://pypi.org/project/pymongo/) and [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) To connect Python and Flask to the MongoDB database
- [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) WSGI (Web Server Gateway Interface) for Python
- [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/) Templating language for Python
- [dnspython](https://www.dnspython.org/) DNS toolkit for Python
- [autopep8](https://pypi.org/project/autopep8/) Python Code formatter

### 4. Workspace, Version Control, Repository storage and Deployment

![Image](https://res.cloudinary.com/dpagr3dzw/image/upload/t_media_lib_thumb/v1616409081/logos/gitpod_logo.png) [Gitpod](https://www.gitpod.io/) - Main workspace

![Image](https://res.cloudinary.com/dpagr3dzw/image/upload/t_media_lib_thumb/v1616409188/Git-logo.png) [Git](https://git-scm.com/) - Distributed Version Control tool to store versions of files and track changes

![Image](https://res.cloudinary.com/dpagr3dzw/image/upload/t_media_lib_thumb/v1616409143/logos/GitHub-logo.png) [GitHub](https://github.com/) - A cloud-based hosting service to manage Git repositories

![Image](https://res.cloudinary.com/dpagr3dzw/image/upload/t_media_lib_thumb/v1616409243/logos/heroku_logo.png) [Heroku](https://heroku.com) - Container-based cloud platform for deployment and running of apps

### 5. IDE Extensions used

- Auto Close Tag
- Auto Rename Nametag
- Bracket Pair Colorizer 2
- Code Spellchecker
- Beautify - Code Formatter
- Indent-Rainbow
- Markdown Lint
- Python
- JSHint

> [Back to Top](#table-of-contents) 

## Resources for Learning

- [Code Institute Course Content](https://courses.codeinstitute.net/) - Main source of fundamental HTML, CSS, Javascript, Python, MongoDB and Heroku knowledge.
- Code Institute **SLACK Community** - Main source of assistance
- [Stack Overflow](https://stackoverflow.com/) - General resource.
- [Youtube](https://www.youtube.com/) - General resource.
- [CSS-Tricks](https://css-tricks.com/) - General resource.
- [W3.CSS](https://www.w3schools.com/w3css/4/w3.css) - General resource.
- [CommonMark](https://commonmark.org/help/) - For Markdown language reference.
- [Coolors.co](https://coolors.co/) - Colour pallette generator
- [TinyPNG](https://tinypng.com/) - Efficient compression of images for site.
- [Am I Responsive](http://ami.responsivedesign.is/) - Responsive website mockup image generator.
- [Balsamiq](https://balsamiq.com/wireframes/) - Wireframing design tool.

> [Back to Top](#table-of-contents) 

## Testing

Testing documentation can be found on a separate document [HERE](static/testing/TESTING.md)

## Project barriers and solutions



> [Back to Top](#table-of-contents) 

## Code validity

- HTML - [W3C](https://validator.w3.org/) - Markup Validation
- CSS - [W3C](https://jigsaw.w3.org/css-validator/) - Jigsaw CSS Validation
- JavaScript - [JSHINT](https://jshint.com/) - JavaScript code warning & error check
- Python - [Pyton Tester](https://extendsclass.com/python-tester.html) Python code syntax checker
- TAGS - [Closing Tag Checker for HTML5](https://www.aliciaramirez.com/closing-tags-checker/) - Validates all tags are opening and closing correctly.

## Version Control

- Used Git for version control.

### IDE

- All code was written on [Gitpod](https://www.gitpod.io/)
- The code was then pushed to GitHub where it is stored in my [Repository](https://github.com/sruss07/MS03-Geodictionary).

> [Back to Top](#table-of-contents) 

## Deployment

### Local Installation

#### 1. Cloning the project

- The code can be run locally through clone or download from the repository on [GitHub](https://github.com/sruss07/MS03-Geodictionary).
- You can do this by opening the repository, clicking on the Code' button and selecting either 'clone or download'.

    ![Image](static/images/clone_project.png)
- The Clone option provides a URL, which you can use on your CLI with `git clone <paste url>`.
- The Download ZIP option provides a link to download a ZIP file which can be unzipped on your local machine. The files can then be uploaded to your IDE.

#### 2. Create a Virtual Environment

In the Terminal window:

- Navigate to the folder of the installed files with `cd <path>`
- Create the virtual environment folder with `python -m venv venv`
- Activate the virtual environment with `venv\Scripts\activate.bat`

*Note: The above commands were used on Gitpod on Mac OS. For other IDE's and Linux, please refer to [Creation of Virtual Environments](https://docs.python.org/3/library/venv.html)*

#### 3. Create Environmental Variables

- Create an env.py file in the the **config** folder. In this file enter the Environmental Variables (**replace values with your own**) as follows:

```python
        import os

        os.environ.setdefault("IP", "IP_ADDRESS")
        os.environ.setdefault("PORT", "PORT")
        os.environ.setdefault("SECRET_KEY", "SECRET_KEY")
        os.environ.setdefault("MONGO_URI", "MONGO_URI")
        os.environ.setdefault("MONGO_DBNAME", "MONGO_DBNAME")
```

#### 4. Create a .gitignore file

- Create a file called **.gitignore** in the root directory and ensure it contains the following git exclusions:

```json
            env.py
            __pycache__/
```

#### 5. Install project dependencies

- Install project requirements by typing `pip install -r requirements.txt`

#### 6. Create a database on MongoDB

Register for a free account with [MongoDB](https://account.mongodb.com/account/register)

- Create a new Project and call it 'MS03_Geodictionary'
- Creater a Cluster, choose the free tier option and select your region
- Create a new database and call it 'geoDictionary'
- Create two Collections named 'geoTerms' and 'users' an enter key/values as follows:

- **geoTerms** collection

```json
            _id: <ObjectId>
            geology_term: "<string>"
            definition: "<string>"
            created_by: "<string>"
```
- **users** collection

```json
            _id: <ObjectId>
            username: "<string>"
            password: "<string>"
```
#### 7. Deploy locally

- To run the project locally, in the terminal type `python app.py`
- This will open a localhost address, which is provided in the CLI.
- Either copy and paste the url shown below into a new browser tab, or hover over it and click *follow link*

#### 8. Remote Deployment on Heroku

[Heroku](https://www.heroku.com) is a Cloud Application Platform that enables developers to build, run, and operate applications in the cloud.

Deployment process is as follows:

Create a **requirements.txt** file to store depenecies of installed packages for the project. In the CLI type `pip freeze --local > requirements.txt`.

Create a file named **Procfile** to declare what commands are run by the application's dynos on the Heroku platform. For this project, run by the app.py file, the Procfile should contain:`web: python app.py`

- Register for a free account on the Heroku [Signup](https://signup.heroku.com/login) page.
- On the Dashboard, click the 'New' button and select 'Create new app'.
- Choose a name and region.
- Under the 'Settings' tab, click on 'Config Vars' to add Configuration Variables from the env.py file (As shown in step **3. Create Environmental Variables** above). Remember to use your own credentials.
- In your CLI terminal install Heroku by typing `npm install -g heroku`
- Select the 'Deploy' option from the menu.
- Under 'Deployment method' select the GitHub option to connect to your GitHub repository. Ensure GitHub Username is selected and use the search function to find the relevant repository. It is recommended using a 'main' branch as default, due to GitHub depreciating the 'master' branch name.
- Select Automatic deploys from the main branch and click 'Deploy Branch'.
- Click on the 'Open App' button on the top-right to open the deployed app.
- There is no difference between the deployed version and the development version.

> [Back to Top](#table-of-contents) 

