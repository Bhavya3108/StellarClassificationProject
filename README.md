# Stellar Classification

## Description

## Prerequisites
Before setting up the project, ensure you have the following installed:
1. Python (version 3.10.6) [ https://www.python.org/downloads/ ]
2. Git version control [ https://git-scm.com/ ]

## Installation
Follow these steps to set up and run the project locally:
### 1. Clone the repository
Use git to clone this repository to your local machine:
```
git clone <repository-url>
```
Navigate into the project directory:
```
cd <project-folder>
```
### 2. Create and activate a virtual environment
Create a python virtual environment to isolate dependencies:   
For windows
```
python -m venv myenv
```
For mac
```
python3 -m venv myenv
```  
Activate the virtual environment:
For windows
```
myenv\Scripts\activate
```
For mac
```
source myenv/bin/activate
```
### 3. Install dependencies
Install all the required dependencies listed in requirements.txt using pip:
```
pip install -r requirements.txt
```
### 4. Apply migrations
Set up the database by applying migrations:
```
python manage.py migrate
```
### 5. Run the development server
Start the Django development server:
```
python manage.py runserver
```
### 6. Access the application
Open your web browser and visit:
```
http://127.0.0.1:8000/
```

## Project Structure