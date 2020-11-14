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
Website: 
[Trello Board](https://trello.com/b/dubA6cfY/my-project)

### Brief

#### Requirements
The minimum viable product was to create an application that utilises create, read,
update and delete (CRUD) functions using supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training so far. We also had to include:
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
To fulfil these requirements I decided to make an application made for everyone from film 
enthusiasts to movie newbies which allows them to:
* Create genres:
  * Title
  * Description
  * Popularity Rating
* Create films:
  * Title
  * Duration
  * Genre
  * Age Rating
* View and update genres and films
* Delete genres and films

##### Stretch Goals

### Architecture

#### Database Structure
Below is an evolution of my ERD designs
##### ERD Diagram 1
The image below shows my first ERD diagram, I initially wanted my two tables to have a one-to-many
relationship.
![erdfirst](https://github.com/kirankalsi/fundamental_project/blob/main/images/Films-db-Draft1.png)
##### ERD Diagram 2

#### CI Pipeline

### Future Improvements
This application successfully implemented CRUD functionalities. I want to focus more
on TDD
I want to improve the project testing and hope to see the overall coverage increase to at least...
In future, I would love the application to be more user friendly by adding... for example if there was no genres/films
message to prompt to add genre/film
Add order by eg:genre as mentioned in user stories
