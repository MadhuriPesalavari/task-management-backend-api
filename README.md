# Task Management Backend API

A RESTful backend API for managing tasks, built with Flask and PostgreSQL. The API provides endpoints to create, retrieve, update, and delete tasks.

## 🛠️ Technologies Used

* Python
* Flask
* PostgreSQL
* SQLAlchemy
* Flask-Migrate
* REST API
* Git & GitHub

## ✨ Features

* Create new tasks
* Retrieve task details
* Update existing tasks
* Delete tasks
* PostgreSQL database integration
* Database migrations using Flask-Migrate
* Structured backend using models, routes, and utilities

## 📁 Project Structure

```text
task-management-backend-api/
│
├── migrations/
├── models/
├── routes/
├── utils/
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
└── README.md
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/MadhuriPesalavari/task-management-backend-api.git
cd task-management-backend-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

Create a PostgreSQL database and update the database configuration in the project as required.

### 5. Run the application

```bash
python app.py
```

The API will start on the configured local server.

## 🔗 API

The backend exposes RESTful endpoints for task management, including operations for:

* `POST` — Create a task
* `GET` — Retrieve tasks
* `PUT/PATCH` — Update a task
* `DELETE` — Delete a task

## 👩‍💻 Author

**Madhuri Pesalavari**


