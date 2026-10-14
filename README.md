# Student CRUD API using FastAPI and SQLite

## Project Overview

The Student CRUD API is a beginner-friendly backend project developed using Python, FastAPI, and SQLite. It allows users to create, read, update, and delete student records through REST API endpoints.

The project uses SQLite to store student information and Swagger UI to test the API endpoints.

## Technologies Used

- Python
- FastAPI
- SQLite
- Uvicorn
- Pydantic
- Git and GitHub
- Swagger UI

## Features

- Create a new student record
- Retrieve all student records
- Retrieve a student by ID
- Update student information
- Delete a student record
- Validate student input using Pydantic
- Handle duplicate email errors
- Store student records in an SQLite database
- Test APIs using Swagger UI

## Student Information

The student table contains the following fields:

| Field | Description |
|---|---|
| id | Unique student ID |
| name | Student's name |
| email | Student's email address |
| age | Student's age |
| course | Student's course |

## Project Structure

```text
stud_CRUD/
├── main.py
├── students.db
├── requirements.txt
├── README.md
└── .gitignore
```

The `venv/` folder contains the virtual environment and is excluded from GitHub.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Payal-chevale/Student-CRUD-API.git
cd Student-CRUD-API
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m uvicorn main:app --reload
```

## API Documentation

After starting the application, open the following URL in your browser:

http://127.0.0.1:8000/docs

Swagger UI allows you to interactively test the available API endpoints.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/students` | Create a student |
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| PUT | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |

## Learning Outcomes

Through this project, I practiced building REST APIs, working with SQLite databases, validating request data, handling errors, testing endpoints using Swagger UI, and managing source code with Git and GitHub.

## Author

**Payal Chevale**

GitHub: https://github.com/Payal-chevale
