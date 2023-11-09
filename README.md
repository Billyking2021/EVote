# Electronic Senate Voting System
The project is to implement a web-based voting system for the Australian Senate. Thistop-secret AEC project will allow a state's AEC Commissioner's delegate(s) to enter the details of thecandidates, including their order within their party grouping. It will allow individual voters to enter theirvotes either above the line, below the line but not both. It will correctly calculate the order in which senatorsshould be elected. It will also allow the state's AEC Commissioner's delegate(s) to manually excludecandidates if a recount should be ordered by the High Court sitting as the Court of Disputed Returns.
## Contributors
Group 12

| StudentId | StudentName                 | Email address                                       |
| --------- | ----------------------------| ----------------------------------------------------|
| A1870016  | Bangyan Ni                  | bangyan.ni@student.adelaide.edu.au                  |
| A1901559  | Bhavesh Dilip Patil         | bhaveshdilip.patil@student.adelaide.edu.au          |
| A1834744  | Xiaochen Wang               | xiaochen.wang01@student.adelaide.edu.au             |
| A1906639  | Dhrumil Chimanbhai Dobariya | dhrumilchimanbhai.dobariya@student.adelaide.edu.au  |


## Project description
Electronic senate voting application, the project to implement a secure and robust web based Voting application for Australian Senate by following the design paradigm, principles and by incorporating the key security elements such as authentication, authorization, audit, confidentiality, integrity and availability.

## Prerequisites
The tools required to run the code of our project are,
Firstly to install conda
The below link will direct to install anaconda3,
https://www.anaconda.com/download
```
conda create --name eVotingEnv django
activate eVotingEnv (source activate eVotingEnv for Mac Users)
cd eVotingApp
```
For Database: 
My SQL is used for the current system,
The below link will direct to install , Once all the frontend tools are installed you can create your own databases for storage
https://dev.mysql.com/downloads/installer/

```
create DATABASE evoting;
```
Also, install the following modules 
```
pip install bcrypt
pip install pillow
pip install django-widget-tweaks
```

## Run
To run the Electronic Senate Voting Application
Environment variables should be saved in the. env file
```
python manage.py runserver
python manage.py migrate
python manage.py makemigrations authentication
```

