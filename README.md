Basic flask app template

This template includes:

flask
template folder
static folder
css folder
js folder
base html template
main html template
base css file
base js file
requirements.txt

you need to create a file (on the same level as readme file) named "env.py" and put these contents in this file for the app to work:

> import os

> os.environ.setdefault("IP", "0.0.0.0") <br>
> os.environ.setdefault("PORT", "5000") <br>
> os.environ.setdefault("SECRET_KEY", "THisIsMySecretKey") <br>


All static files are linked to base html template, main html template inherets from base

to run the live server, run the following command in the terminal:
> python3 app.py


### Tailwind Installation Guide
Tailwind is added with the NPM (Node Package Manager), To be able to use it on your machine you need to have Node.js installed:

Download Node.js [here](https://nodejs.org/en/)

After Node.js is installed, install the Tailwind by running the following command in the terminal from the roof of the project:

> npm install

To compile Tailwind to work during development use command:

> npx tailwindcss -i ./static/src/input.css -o ./static/css/output.css --watch

For faster development, npm script has been added. Run command:

>  npm run watch



# RevFinance

RevFinance was developed as part of the January 2023 Hackathon: New Years Revolutions: Revolutionising finance for 2023! Presented by Code Institute.

## Team Name: <<team_name>>

[View Deployed Project Here](https://moneypot.onrender.com)

## Contents

* [User Experience (UX)](#user-experience)
  * [User Stories](#user-stories)
* [Technology](#technology)
* [Design](#design)
  * [Color Scheme](#color-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)
* [Deployment & Usage](#deployment)
* [Testing](#testing)
* [Credits](#credits)
  * [Code](#code)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)

## About

RevFinance is a social lending platform that allows users to create and manage money pots for saving towards specific goals. Users can create public pots that others can join and contribute to, as well as private pots where only invited users can participate. The platform also allows users to track the progress of their pots, edit the details of their pots, and join other users' public pots. RevFinance is a community-driven platform that makes it easy to save and reach your financial goals.

## User Experience

When designing the user experience for RevFinance, we considered several key paradigms of user experience to ensure that the platform is intuitive, easy to use, and meets the needs of users.

1. Navigation: The platform has a clear and simple navigation system that allows users to easily find and access the features they need.

2. Usability: The platform has been designed with usability in mind, making it easy for users to understand how to use the features and complete tasks.

3. Accessibility: The platform has been designed to be accessible to users of all abilities, including those with disabilities.
  - Contrast and color considerations: The website has a high contrast design, making it easy to read for users with visual impairments, and color schemes have been chosen to ensure that information is conveyed clearly and effectively.
  - Semantic HTML: The website uses semantic HTML which helps users with assistive technologies understand the website's structure and layout.

4. Personalization: The platform allows users to personalize their experience by creating and managing their own money pots, and join other people's pots if public.

5. Security: User's data is kept secure and private, and the platform is designed to protect against unauthorized access.

6. Consistency: The platform maintains a consistent design throughout, making it easy for users to understand the layout and find what they need.

7. Flexibility: the platform allows users to create and manage public and private pots, giving them flexibility to save money for a specific goal with others or privately.

### User stories

As a first time user: 

- I want to be able to create an account so that I can use the platform's features.

- I want to be able to explore the website and understand how it works before creating an account.

- I want to be able to create a public or private money pot easily, so that I can start saving - 
  towards my financial goals.

- I want to be able to join public money pots created by other users, so that I can contribute 
  towards their goals.


As a registered user: 

- I want to be able to easily log in to my account so that I can access my money pots and track my progress.

- I want to be able to view my account details and update my profile information if necessary.

- I want to be able to easily create a new money pot and invite friends and family to join it.

- I want to be able to view all of my money pots and see the progress I'm making towards my goals.

- I want to be able to edit or delete my money pots if necessary.

- I want to be able to join other public money pots created by other users, so that I can contribute towards their goals.

- I want to be able to see the list of people who joined my money pots, and see the contributions they made.

- I want to be able to withdraw my money from the money pot and use it for my goal

- I want to be able to leave a pot if I want to.


## Technology:

<< Detail your techstack here, and why you chose it. >>

<< list your languages & tools below: >>

*  Languages

	* << list the langauge & reason for using it >>
    * HTML - Implemented as markdown language
    * CSS - Implemented to add style and layout of the website.
    * JavaScript - Implemented to add interactivity and secutiry. 
    * Python - 

* Frameworks, Libraries & Programs Used.

  * Tailwind - user as a CSS framework to add style and layout.
  * Flask - 
  * Balsamic - used to generate wireframes.
  * Git - was used for the version control of the website.
  * GitHub - was used to host the code of the website.
  * Chrome DevTools - used to debug the website. 

## Initial MVP idea:

Detail plans and scope of project here....

<< consider talking about how you planned as a team here and what tools were implemented >>

### Actual idea & content:

<< how does you final product/project match up to your initial mvp plans >>

<< detail idea / features / functionality here >>

## Design

### Color Scheme:
<< detail your color palette here >>

### Typography:
<< what font pairings did your team consider and pick? And why? >>

### Imagery:
<< Detail imagery used to compliment your build & theme >>

<< ensure source attribution is maintained, and that you have used copyright free material >>

### Wireframes:

<details>
<summary>- Mobile Wireframes:</summary>

<< put all your mobile wireframes here... >>

<< consider adding some notes to detail the planned components or functionality >>

</details>

<details>
<summary>- Desktop Wireframes:</summary>

<< put all your mobile wireframes here... >>

<< consider adding some notes to detail the planned components or functionality >>

</details>

## Deployment
<< detail deployment methods used here, and any extraneous circumstances to run the project locally >>

## Testing
<< detail testing logs here - any known bugs, and squashed bugs 🐛🐛 >>



## Credits

### Code
<< any and all code that isn't yours...must go here >>

### Content
<< any content, such as facts/references/text that isn't yours...must go here >>

### Media
<< you may have already done this above in the Imagery section, but just in case, please attribute Media acquisition here >>

### Acknowledgements
<< personal thanks and praise 🙌 >>

