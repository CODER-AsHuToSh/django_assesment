# Django To-Do Web API

This Django project implements a To-Do Web API allowing users to manage their tasks.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python (3.12 or higher)
- Django (3.x)
- (Optional) Virtual environment tool like `virtualenv` or `pipenv`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/CODER-AsHuToSh/django_assesment.git
   cd django_assesment
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   # Using virtualenv
   virtualenv venv
   source venv/bin/activate

   # Using pipenv
   pipenv install
   pipenv shell
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:

   ```bash
   python manage.py migrate
   ```

## Usage

1. Start the development server:

   ```bash
   python manage.py runserver
   ```

2. Access the API endpoints:

   - To create a To-Do item: `POST /create/`
   - To retrieve all To-Do items: `GET /all/`
   - To retrieve a specific To-Do item: `GET /<id>/`
   - To update a To-Do item: `PUT /update/<id>/`
   - To delete a To-Do item: `DELETE /delete/<id>/`


## Examples 
   - Results of GET Request
   ```json
       {
        "id": 23,
        "tags": [
            {
                "name": "TagG22AAQW2dd2"
            },
            {
                "name": "TagG23AA1W1dd22"
            }
        ],
        "timestamp": "2023-12-05T16:16:47.948006Z",
        "title": "New Todo Item",
        "description": "Description for the new todo",
        "due_date": "2023-12-31",
        "status": "WORKING"
       }
   ```
   
   - A POST Request
   ```json
       {
         "title": "New Todo Item",
         "description": "Description for the new todo",
         "status": "WORKING",
         "due_date": "2023-12-31",
         "tags": [
            {"name": "TagG22AAQW2dd2"},
            {"name": "TagG22AAQW2dd2"},
            {"name": "TagG23AA1W1dd22"}
            ]
        }
   ```
## Coverage Report

![Coverage Report Screenshot](ss.png)


## Contact

For any inquiries or support, please contact [Ashutosh Gupta](ashutosh.gupta.civ20@iitbhu.ac.in).
