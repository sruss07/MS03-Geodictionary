# Table of Contents

> - [User Stories](#user-stories)
> - [Code Validation](#code-validation)
> - [Search Function](#search-function)
> - [Manual Site Testing](#manual-site-testing)
> - [Responsive Tests](#responsive-tests)
> - [Deployment](#deployment)  

## User Stories


> [Back to Top](#table-of-contents) 

## Code Validation

### HTML

Passed code through [Nu Html Checker](https://validator.w3.org/#validate_by_uri)by entering the 'Validate by URI method.

### CSS

Passed code through [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) by pasting code in by direct input method

- No errors found
- 1 warning - imported style sheets are not checked in direct input and file upload modes - safely ignored.

![Screenshot of CSS Validation](../testing/css_validation.png)

### JavaScript

Passed code through [JSHint](https://jshint.com/)

- No warning received
- JSHint flags Jquery $ symbol as undefined variable - safely ignored.

![Screenshot of JavaScript Validation](../testing/js_validation.png)

### Python

Autopepe8 installed as a dependency for checking code as written
All Python code passed through [ExtendsClass Python Syntax Checker](https://extendsclass.com/python-tester.html)

- [app.py](../../app.py)

![Screenshot of app.py code validation test](../testing/app_py_validation.png)

> [Back to Top](#table-of-contents) 

## Search Function

The search function for my app is located on the home page. The search function can be used by registered users after they log in to the site, and it can also be used by users without logging on or registering.

- Clicked submit button with no entries in search field - form prompts user to fill in the search field
- Entered valid keyword into search field and page returns relevant result(s)containing that keyword
- Entered invalid keyword and page returns the message: 'No results found'
- Clicked Reset button and this clears the search field to default

![Screenshot of home page search form](../images/search_form.png)

> [Back to Top](#table-of-contents) 

