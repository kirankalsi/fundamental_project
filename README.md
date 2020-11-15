# The Ultimate Genres and Films Application
## Fundameental Project

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
* Issues
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
server and deployed to a cloud-based virtual machine.

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

##### Stretch Goals

### Architecture

#### Database Structure
I have created entity relationship (ERD) diagrams to show the structure of my database and the relationships taking place between the tables. Below is an evolution of my ERD designs
##### ERD Diagram 1
The image below shows my first ERD diagram, I initially wanted my two tables to have a one-to-many relationship.
![erdfirst](https://github.com/kirankalsi/fundamental_project/blob/main/images/Films-db-Draft1.png)
##### ERD Diagram 200
The next image below shows my final draft ERD diagram, I've changed the relationship to many-to-many.
![erdsecond](https://github.com/kirankalsi/fundamental_project/blob/main/images/Films-db-Draft2.png)
#### CI Pipeline
The image below represents my continuous integration pipeline with the associated frameworks and services related to them. It is a breakdown of the services and tools used to develop and deploy a well-tested, functioning program. The services I have chosen within the pipeline provide the most efficient method of rapid development to be automated and tested.

### Project Tracking
Trello was used to track the progress of the project, from planning to testing and finally to completion. Below is a screenshot of my board.#
You can find the full Trello Board [Here](https://trello.com/b/dubA6cfY/my-project)

### Risk Assessment
Below is a screenshot of my risk assessment for the project. This is where I have outlined potential risks, their impacts and mitigation techniques that I may need.
The full document can be found [here](https://docs.google.com/spreadsheets/d/1RD_fca3jRA9D0HOCS2oe6eftotsjKILWXCJ5MKXBjcs/edit?usp=sharing)

### Testing
I used pytest to run unit tests on my application in which I tested most of my functions.
Unit testing on my application folder came to 81% coverage overall as shown below.
![coverage](https://github.com/kirankalsi/fundamental_project/blob/main/images/coverage.PNG)
Furthermore I used pytest and selenium for my integrated testing. This had completely passed successfully as displayed above.


### Future Improvements
This application successfully implemented CRUD functionalities. I want to focus more
on TDD
I want to improve the project testing and hope to see the overall coverage increase to at least...
In future, I would love the application to be more user friendly by adding... for example if there was no genres/films
message to prompt to add genre/film
Add order by eg:genre as mentioned in user stories
