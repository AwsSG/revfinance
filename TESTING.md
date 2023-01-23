# TESTING

The usability was evaluated through user acceptance testing, which was conducted by distributing the test to various new users on various devices and browsers to identify and resolve any issues that arose during development.


|             | User Action | Expected result  | Y/N | Comment |
|-------------|-------------|------------------|-----|---------|
|Register      |             |                  |     |         |
|1            | Click  on the Moon icon in the navbar | Dark Mode | Y | Dark Mode active |
|2            | Click REGISTER button in home page | Register page | Y | Register page opens |
|3            | Enter valid name, email, and password + confirmation | User registered | Y | User's account should be created |
|4            | Enter valid name | Error | Y | Should prompt user to enter email and password |
|5            | Enter valid name and email | Error | Y | Should prompt user to enter a valid password |
|6            | Enter valid name, email, and password | Error | Y | Should prompt user to confirm password |
|7            | Click Home link | Home page | Y | User will be redirected to Home page |
|8            | Click Login link | Login page | Y | User will be redirected to Login page |
| Log In      |             |                  |     |         |
|1            | Click on Login button in home page | Login page | Y | Login page opens |
|2            | Enter valid email and password | Logged in | Y | User should be Logged in |
|3            | Enter valid email | Error | Y | Should prompt user to enter password |
|4            | Click Register link | Register page | Y | User will be redirected to Register page |
|Log Out      |             |                  |     |         |
|1            | Click on logout button | Home page | Y | User is logged out |
|Footer  |             |                  |     |         |
|1            | Click on Aws Sabah Gheni | Github page | Y | Aws Sabah Gheni page opens |
|2            | Click on Elisa Sacchelli | Github page | Y | Elisa Sacchelli page opens |   
|3            | Click on Orla Sweeney | Github page | Y | Orla Sweeney page opens |
|4            | Click on Tomasz Ostroga | Github page | Y | Tomasz Ostroga page opens |   
|5            | Click on Adam Chwiulkowski | Github page | Y | Adam Chwiulkowski page opens |
|5            | Click on Kieran | Github page | Y | Kieran page opens |
|6            | Click on Link to GitHub repository | Github page | Y | Project repository page opens |
|7           | Click on Facebook icon | Facebook | Y | Facebook page opens |
|8            | Click on Instagram icon | Instagram | Y | Instagram page opens |   
|9            | Click on Twitter icon | Twitter | Y | Twitter page opens |
|10            | Click on LinkedIn | LinkedIn | Y | LinkedIn page opens | 
|Dashboard |             |                  |     |         |
|1            | Click on Create Pot | Create new pot form | Y | Form opens with instructions |
|2            | Enter title, goal amount, cycle, recurrent payment amount, tick if private | Creates pot on dashboard | Y | Pot should be created |
|3            | Click on Join pot | Join pot | Y | User joins an existing pot |
|3            | Click on Home link | Home page | Y | Home page opens |
|4            | Click on Money Pots | Money Pots | Y | Money Pots opens |


---

## Validator testing

### HTML Validation

- No errors or warnings were found when testing through the official [W3C](https://validator.w3.org/) validator for the following pages:

   - Home page:
* ![Home page html validation report]()

    - Log In page:
* ![Log In page html validation report]()

    - Register page:
* ![Register page html validation report]()

    - Dashboard page:
* ![Profile page html validation report]()

### CSS Validation

- No errors were found when testing through the official [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/#validate_by_uri) validator: 
    * ![CSS validation report]()

### JS Validation
*  JavaScript files were tested by the official [JSHint](https://jshint.com/):
    * ![script.js]();

### Python Validation
[Valentin Bryukhanov's](http://pep8online.com/) was used to ensure that all of the project's Python source code is [Pep 8-compliant](https://legacy.python.org/dev/peps/pep-0008/). This checking was done manually by copying python code and pasting it into the validator.

No errors found:

- **app.py**

![Python Validator]()

## Lighthouse Report

- Home Page:
    ![Home Page]()

- Log In Page:
    ![Log In Page]()

- Register Page:
    ![Register Page]()

- Dashboard Page:
    ![Profile Page]()

## Compatibility:

+ The app was tested on the following browsers: Chrome and Firefox:

  - Chrome:

  ![Home Page](documentation/testing/browser_chrome.png)
  
  - Firefox:

  ![Home Page](documentation/testing/browser_firefox.png)

## Responsiveness:

+ The app was checked with [Responsive Website Design Tester](https://responsivedesignchecker.com/).

  1. Mobile Screens:

     ![Mobile]()

      
  1. Tablets Screens:
        
     ![Tablet]()
      
  1. Desktop Screens:
        
     ![Desktop]()


