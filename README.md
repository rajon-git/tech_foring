
# Project Management API
## Features
- User authentication (CRUD operations)
- Task management (CRUD operations)
- Commenting on tasks (CRUD operations)
- Project management (CRUD operations)

## Installation Guide

To run this project locally, follow the steps below:

### Prerequisites
Make sure you have the following installed on your machine:
- Python 3.8+ 
- pip (Python package installer)
- Virtual environment (recommended)

### Step 1: Clone the Repository

git clone https://github.com/your-username/project-name.git
cd project-name

Step 2: Set up a Virtual Environment
python -m venv venv
.\venv\Scripts\activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Set up the Database
python manage.py makemigrations
python manage.py migrate

Step 5: Create a Superuser
python manage.py createsuperuser

Step 6: Run the Server
python manage.py runserver
Your project should now be available at http://127.0.0.1:8000/
