# Django Lab Project - Full Stack Development

A comprehensive Django project containing 9 lab exercises demonstrating various database operations, form handling, and CRUD functionalities.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Lab Modules](#lab-modules)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Usage](#usage)
- [Database Schema](#database-schema)

## 🎯 Project Overview

This project is a collection of 9 Django applications, each demonstrating different aspects of web development and database management. The labs cover topics ranging from basic CRUD operations to filtering, updating, and deleting records.

**Author**: mdsamimreza 
**Repository**: fds_lab  
**Django Version**: 5.2.8  
**Database**: SQLite3

## 🛠 Technologies Used

- **Backend**: Django 5.2.8
- **Database**: SQLite3
- **Frontend**: HTML (Django Templates)
- **Python**: 3.x

## 📁 Project Structure

```
labproject/
├── manage.py
├── db.sqlite3
├── labproject/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── lab1/                # Lab 1: Biodata Management
├── lab2/                # Lab 2: Student CIE Marks
├── lab3/                # Lab 3: Exam Fee Management
├── lab4/                # Lab 4: Employee Details
├── lab5/                # Lab 5: Exam Student Grades
├── lab6/                # Lab 6: Placement Records
├── lab7/                # Lab 7: Faculty Management
├── lab8/                # Lab 8: Grade Updates
└── lab9/                # Lab 9: Employee CRUD Operations
```

## 📚 Lab Modules

### Lab 1: Biodata Management (q1)
**URL**: `/q1/`  
**Purpose**: Create and display basic biodata information

**Model Fields**:
- Name (CharField)
- Age (IntegerField)
- Email (EmailField)

**Features**:
- Add new biodata records
- Display all biodata entries

---

### Lab 2: Student CIE Marks (q2)
**URL**: `/q2/`  
**Purpose**: Manage student CIE marks and identify low performers

**Model Fields**:
- USN (CharField)
- Name (CharField)
- Subject Code (CharField)
- CIE Marks (IntegerField)

**Features**:
- Add student CIE records
- Display all students
- Filter and display students with CIE marks < 20

---

### Lab 3: Exam Fee Management (q3)
**URL**: `/q3/`  
**Purpose**: Track exam fee payments and manage unpaid students

**Model Fields**:
- Name (CharField)
- USN (CharField)
- Semester (IntegerField)
- Exam Fee (IntegerField)

**Features**:
- Add exam fee records
- Display all fee records
- Delete unpaid students (exam_fee = 0)

---

### Lab 4: Employee Details (q4)
**URL**: `/q4/`  
**Purpose**: Manage employee information and filter by salary

**Model Fields**:
- Name (CharField)
- Email (EmailField)
- Phone (CharField)
- Hired Date (DateField)
- Job Title (CharField)
- Salary (IntegerField)

**Features**:
- Add employee records
- Display all employees
- Filter employees with salary > 50,000

---

### Lab 5: Exam Student Grades (q5)
**URL**: `/q5/`  
**Purpose**: Manage student exam grades and filter by performance

**Model Fields**:
- Name (CharField)
- USN (CharField)
- Grade (CharField)

**Features**:
- Add student grade records
- Display all students
- Filter students with 'O' grade

---

### Lab 6: Placement Records (q6)
**URL**: `/q6/`  
**Purpose**: Track student placement details

**Model Fields**:
- USN (CharField)
- Name (CharField)
- Company Name (CharField)

**Features**:
- Add placement records
- Display all placements
- Filter students placed at Amazon

---

### Lab 7: Faculty Management (q7)
**URL**: `/q7/`  
**Purpose**: Manage faculty information with advanced filtering

**Model Fields**:
- Faculty ID (CharField)
- Title (CharField)
- Name (CharField)
- Branch (CharField)

**Features**:
- Add faculty records
- Display all faculty
- Filter CSE branch Professors

---

### Lab 8: Grade Update System (q8)
**URL**: `/q8/`  
**Purpose**: Advanced grade management with update functionality

**Model Fields**:
- Name (CharField)
- USN (CharField)
- Department (CharField)
- Grade (CharField)

**Features**:
- Add new student records
- Display all students
- Update student grades by name

---

### Lab 9: Employee CRUD Operations (q9)
**URL**: `/q9/`  
**Purpose**: Complete CRUD implementation for employee management

**Model Fields**:
- Name (CharField)
- Email (EmailField)
- Salary (IntegerField)
- Department (CharField)

**Features**:
- Create new employees
- Read/List all employees
- Update employee details
- Delete employee records

**Routes**:
- `/q9/` - List all employees
- `/q9/create/` - Add new employee
- `/q9/update/<pk>/` - Update employee
- `/q9/delete/<pk>/` - Delete employee

---

## 🚀 Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/mdsamimrrza/fds_lab.git
cd "lab programs/labproject"
```

### Step 2: Create Virtual Environment (Recommended)
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### Step 3: Install Dependencies
```bash
pip install django
```

### Step 4: Run Migrations
```bash
python manage.py migrate
```

### Step 5: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

## ▶️ Running the Project

Start the development server:
```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

### Access Points
- **Admin Panel**: `http://127.0.0.1:8000/admin/`
- **Lab 1**: `http://127.0.0.1:8000/q1/`
- **Lab 2**: `http://127.0.0.1:8000/q2/`
- **Lab 3**: `http://127.0.0.1:8000/q3/`
- **Lab 4**: `http://127.0.0.1:8000/q4/`
- **Lab 5**: `http://127.0.0.1:8000/q5/`
- **Lab 6**: `http://127.0.0.1:8000/q6/`
- **Lab 7**: `http://127.0.0.1:8000/q7/`
- **Lab 8**: `http://127.0.0.1:8000/q8/`
- **Lab 9**: `http://127.0.0.1:8000/q9/`

## 💡 Usage

Each lab module is independent and can be accessed through its respective URL pattern. Navigate to the URL endpoints listed above to interact with different lab exercises.

### Common Operations

#### Adding Records
1. Navigate to the respective lab URL
2. Fill in the form with required information
3. Submit the form to add a new record

#### Viewing Records
All records are automatically displayed on the respective lab pages after submission.

#### Filtering Records
Labs 2, 4, 5, 6, and 7 include automatic filtering based on specific criteria (e.g., low marks, high salary, specific companies).

#### Updating Records (Lab 8 & 9)
- Lab 8: Use the update form to change grades by student name
- Lab 9: Click on update links in the employee list

#### Deleting Records
- Lab 3: Delete unpaid students using the delete button
- Lab 9: Click delete links in the employee list

## 🗄 Database Schema

All applications use SQLite3 database (`db.sqlite3`). Below are the key models:

| Lab | Model Name | Primary Purpose |
|-----|------------|-----------------|
| Lab 1 | biodata | Personal information storage |
| Lab 2 | studentCIE | CIE marks tracking |
| Lab 3 | examfeemodel | Fee payment management |
| Lab 4 | employeeDetail | Employee records |
| Lab 5 | ExamStudent | Grade management |
| Lab 6 | Placement | Placement tracking |
| Lab 7 | Faculty | Faculty information |
| Lab 8 | GradeStudent | Grade updates |
| Lab 9 | Employee | Full CRUD operations |

## 🔧 Development

### Making Migrations
After modifying any models:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Accessing Django Shell
```bash
python manage.py shell
```

### Clearing Database
To reset the database:
```bash
del db.sqlite3  # Windows
python manage.py migrate
```

## 📝 Notes

- The project uses Django's built-in SQLite database
- All forms are generated using Django ModelForms
- Templates follow Django template inheritance pattern
- Each lab has its own URL configuration included in the main project

## 🤝 Contributing

This is an academic project for Full Stack Development coursework. Feel free to fork and experiment!

## 📄 License

This project is created for educational purposes.

---

**Last Updated**: November 30, 2025  
**Course**: Full Stack Development (7th Semester)
