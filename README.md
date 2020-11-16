# The Ultimate Genres and Films Application
## Fundamental Project

Contents
* Resources
* Breif
  * Requirements
  * My Approach
* Architecture
  * Database Structure
  * CI Pipeline
* Project Tracking
* Risk Assessment
* Testing
* Front-End Design
* Future Improvements


### Resources
[Trello Board](https://trello.com/b/dubA6cfY/my-project)  
[Risk Assessment](https://docs.google.com/spreadsheets/d/1RD_fca3jRA9D0HOCS2oe6eftotsjKILWXCJ5MKXBjcs/edit?usp=sharing)

### Brief

#### Requirements
The minimum viable product was to create an application that utilises create, read, update and delete (CRUD) functions using supporting tools,
methodologies and technologies that encapsulate all core modules covered during training so far. We also had to include:
* A Trello board with full expansion
on user stories, use cases and tasks needed to complete the project.
* A relational database used to store data persistently for the
project
* Documentation from a design phase describing the application architecture
and a detailed Risk Assessment
* A functional CRUD application created in Python, following best
practices and design principles
* Fully designed test suites for the application, as
well as automated tests for validation of the application
* A functioning front-end website and integrated API's, using Flask
* Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine

#### My Approach
To fulfil these requirements I decided to make an application made for everyone from film enthusiasts to movie newbies which allows them to:
* Create genres that stores a:
  * Title
  * Description
  * Popularity Rating
* Create films that stores a:
  * Title
  * Duration
  * Genre
  * Age Rating
* View and update genres and films
* Delete genres and films

### Architecture

#### Database Structure
I have created entity relationship (ERD) diagrams to show the structure of my database and the relationships taking place between the tables. Below is an evolution of my ERD designs.
##### ERD Diagram 1
The image below shows my first ERD diagram, I initially wanted my two tables to have a one-to-many relationship.
![erdfirst](https://github.com/kirankalsi/fundamental_project/blob/main/images/Films-db-Draft1.png)
##### ERD Diagram 2
The next image below shows my final draft ERD diagram, I've changed the relationship to many-to-many. Including an intermediate table.  
![erdsecond](https://github.com/kirankalsi/fundamental_project/blob/main/images/Films-db-Draft2.png)
#### CI Pipeline
The image below represents my continuous integration pipeline with the associated frameworks and services related to them. It is a breakdown of the services and tools used to develop and deploy a well-tested, functioning program. The services I have chosen within the pipeline provide the most efficient method of rapid development to be tested.
![CIpipeline](https://github.com/kirankalsi/fundamental_project/blob/main/images/CIpipeline.PNG)

### Project Tracking
Following agile methodologies, Trello was used to track the progress of the project and to demonstrate my workflow, from planning to testing and finally to completion. Below is a screenshot of my board.
You can find the full Trello Board [Here](https://trello.com/b/dubA6cfY/my-project).
![trello](https://github.com/kirankalsi/fundamental_project/blob/main/images/trello.PNG)

### Risk Assessment
Below is a screenshot of my risk assessment for the project. This is where I have outlined potential risks, their impacts and mitigation techniques that I may need.
The full document can be found [here](https://docs.google.com/spreadsheets/d/1RD_fca3jRA9D0HOCS2oe6eftotsjKILWXCJ5MKXBjcs/edit?usp=sharing).
![riskassessment](https://github.com/kirankalsi/fundamental_project/blob/main/images/risk_assessment_ss.PNG)

### Testing
I used pytest to run unit tests on my application in which I tested most of my functions.
Unit testing on my application folder came to 81% coverage overall as shown below.
![coverage](https://github.com/kirankalsi/fundamental_project/blob/main/images/coverage.PNG)
Furthermore I used pytest and selenium for my integrated testing.
Integrated Testing instructions:
sudo apt-get install -y unzip
sudo apt-get install -y chromium-browser
wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
* When writing the test_int.py make sure to fill in the correct path to chromedriver
This had completely passed successfully as displayed above. When running pytest --cov --cov-report term-missing I can see which parts of my application that are not tested. This is displayed below.
![pytestmissingterm](https://github.com/kirankalsi/fundamental_project/blob/main/images/pytest.PNG)

### Front-End Design
My front-end design is still in its early stages as it is built using basic HTML. However it meets the MVP
and I am happy with its functionality. Below is the homepage which gives a brief description of what the application is about.
It also gives the user choices within the navigation bar to go to different areas of the application, which will be extended to every page.  
![homepage](https://github.com/kirankalsi/fundamental_project/blob/main/images/homepage.PNG)  
Navigating to the 'Add genre' page allows users to input data into the fields below and add a genre to the genre list.  
![addgenre](https://github.com/kirankalsi/fundamental_project/blob/main/images/addgenre.PNG)  
I expect the genre list to display the genres added, including update and delete buttons.  
![genrelist](https://github.com/kirankalsi/fundamental_project/blob/main/images/genrelist.PNG)  
The film list works in the same manner. Similar to the genre list, if there is a film already inputted with the same name the application will display an error message, as shown below.  
![filmexists](https://github.com/kirankalsi/fundamental_project/blob/main/images/filmexists.PNG)  

### Future Improvements
This application successfully implemented CRUD functionalities. However there are a number of improvements I would like to implement:
* Make relationship between tables as drafted (many-to-many), use SelectMultipleField in forms
* Improve the project testing, overall coverage should increase and be closer to 100%
* Currently I have to manually build in Jenkins, I want this process to be automated
* Have more valiadators, as described in the risk assessment
* Make the application more user friendly to improve the overall user experience (eg: present data in tables)
* Add a filter which orders genres and films by IDs, most recent and alphabetically
* Update the ratings system to show a thumbs up when above and thumbs down when below a certain number

### Author
**Kiran Kalsi**
