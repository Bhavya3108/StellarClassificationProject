# Stellar Classification

This project leverages the Stellar Classification SDSS-17 dataset from Kaggle to develop a robust machine learning model for classifying celestial objects. The development pipeline includes comprehensive data preprocessing, exploratory data analysis (EDA) to uncover patterns and relationships within the dataset, and feature selection to enhance model efficiency and accuracy. A machine learning model was trained and validated to ensure reliable predictions. The finalized model was deployed through a Django-based web application, providing an interactive and user-friendly graphical user interface (GUI). This deployment bridges data-driven insights and real-world accessibility, providing a practical tool for stellar classification tasks.

# Prerequisites

Before setting up the project, ensure you have the following installed:

1. Python (version 3.10.6) [ https://www.python.org/downloads/release/python-3106/ ]
2. Git version control [ https://git-scm.com/downloads ]

# Installation

Follow these steps to set up and run the project locally.

### 1. Clone the repository

Use git to clone this repository to your local machine:
```
git clone https://github.com/Bhavya3108/StellarClassificationProject.git
```

Navigate into the project directory:
```
cd StellarClassificationProject
```

### 2. Create and activate a virtual environment

Create a python virtual environment to isolate dependencies:

*For windows*
```
python -m venv myenv
```

*For mac*
```
python3 -m venv myenv
```

Activate the virtual environment:

*For windows*
```
myenv\Scripts\activate
```

*For mac*
```
source myenv/bin/activate
```

### 3. Install dependencies

Install all the required dependencies listed in requirements.txt using pip:
```
pip install -r requirements.txt
```

### 4. Apply migrations

Navigate into the django project directory:
```
cd stellar
```

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
