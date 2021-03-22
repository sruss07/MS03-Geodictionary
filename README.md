# Table of Contents

> - [Overview](#overview)
> - [User Stories](#user-stories)
> - [UX](#ux)
> - [Features](#features)
> - [Technologies Used](#technologies-used)
> - [References for learning](#references-for-learning)
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

